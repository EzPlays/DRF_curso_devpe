from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from users.api.serializer import UserSerializer, UserListSerializer, UpdateUserSerializer, PasswordSerializer
from users.models import User


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects\
                            .filter(is_active=True)\
                            .values('id', 'username', 'email', 'name')
        return self.queryset

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': 'Contraseña actualizada correctamente'
            })
        return Response({
            'message': 'Hay errores en la información enviada',
            'errors': password_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario registrado correctamente.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)







# clase APIView

# class UserApiView(APIView):
    
#     def get(self, request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many = True)
#         return Response(users_serializer.data)


# decoradores

# @api_view(['GET','POST'])
# def user_api_view(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many = True)
#         return Response(users_serializer.data)
#     elif request.method == 'POST':
#         users_serializer = UserSerializer(data = request.data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return Response(users_serializer.data)
#         return Response(users_serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def user_detail_view(request, pk=None):

#     if request.method == 'GET':
#         user = User.objects.filter(id = pk).first()
#         user_serializer = UserSerializer(user)
#         return Response(user_serializer.data)

#     elif request.method == 'PUT':
#         user = User.objects.filter(id = pk).first()
#         users_serializer = UserSerializer(user, data = request.data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return Response(users_serializer.data)
#         return Response(users_serializer.errors)

#     elif request.method == 'DELETE':
#         user = User.objects.filter(id = pk).first()
#         user.delete()
#         return Response('Eliminado')


# response con status code

# @api_view(['GET','POST'])
# def user_api_view(request):

#     #list
#     if request.method == 'GET':
#         #queryset
#         # users = User.objects.all()
#         users = User.objects.all().values('id','username','email','password')
#         users_serializer = UserListSerializer(users, many = True)
        
#         # Testing de serializer
#         # test_data = {
#         #     'name': 'sefsefsef',
#         #     'email': 'thtf@gmial.com'
#         # }
#         # test_user = TestUserSerializer(data= test_data, context= test_data)
#         # if test_user.is_valid():
#         #     pass
#         #     # user_instance = test_user.save()
#         #     # print(user_instance)
#         #     # print('successfully validations')
#         # else:
#         #     print(test_user.errors)

#         return Response(users_serializer.data, status.HTTP_200_OK)

#     #create
#     elif request.method == 'POST':
#         users_serializer = UserSerializer(data = request.data)
        
#         #validations
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return Response({'message': 'user created successfully'}, status.HTTP_201_CREATED)
#         return Response(users_serializer.errors, status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def user_detail_view(request, pk=None):
#     #queryset
#     user = User.objects.filter(id = pk).first()

#     #validate
#     if user:

#         #retrieve
#         if request.method == 'GET':
#             user_serializer = UserSerializer(user)
#             return Response(user_serializer.data, status.HTTP_200_OK)

#         #update
#         elif request.method == 'PUT':
#             users_serializer = UserSerializer(user, data = request.data)
#             if users_serializer.is_valid():
#                 users_serializer.save()
#                 return Response(users_serializer.data, status.HTTP_200_OK)
#             return Response(users_serializer.errors, status.HTTP_400_BAD_REQUEST)

#         #delete
#         elif request.method == 'DELETE':
#             user.delete()
#             return Response({'message': 'user deleted successfully'}, status.HTTP_200_OK)

#     return Response({'message': 'user data not found'}, status.HTTP_400_BAD_REQUEST)


