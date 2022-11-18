from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.api.serializer import UserSerializer, TestUserSerializer
from users.models import User


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

@api_view(['GET','POST'])
def user_api_view(request):

    #list
    if request.method == 'GET':
        #queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        
        # Testing de serializer
        # test_data = {
        #     'name': 'sefsefsef',
        #     'email': 'thtf@gmial.com'
        # }
        # test_user = TestUserSerializer(data= test_data, context= test_data)
        # if test_user.is_valid():
        #     pass
        #     # user_instance = test_user.save()
        #     # print(user_instance)
        #     # print('successfully validations')
        # else:
        #     print(test_user.errors)

        return Response(users_serializer.data, status.HTTP_200_OK)

    #create
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)
        
        #validations
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({'message': 'user created successfully'}, status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk=None):
    #queryset
    user = User.objects.filter(id = pk).first()

    #validate
    if user:

        #retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status.HTTP_200_OK)

        #update
        elif request.method == 'PUT':
            users_serializer = UserSerializer(user, data = request.data)
            if users_serializer.is_valid():
                users_serializer.save()
                return Response(users_serializer.data, status.HTTP_200_OK)
            return Response(users_serializer.errors, status.HTTP_400_BAD_REQUEST)

        #delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'user deleted successfully'}, status.HTTP_200_OK)

    return Response({'message': 'user data not found'}, status.HTTP_400_BAD_REQUEST)


