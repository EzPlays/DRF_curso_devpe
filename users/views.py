from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.serializer import (
    CustomTokenObtainPairSerializer, CustomUserSerializer
)
from users.models import User



class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)


# from django.contrib.sessions.models import Session
# from datetime import datetime

# from rest_framework.views import APIView
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.response import Response
# from rest_framework import status
# from users.api.serializer import UserTokenSerializer
# from rest_framework.authtoken.models import Token

# class Login(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         login_serializer = self.serializer_class(data = request.data, context = {'request': request })
#         if login_serializer.is_valid():
#             # print(login_serializer.validated_data['user'])
#             user = login_serializer.validated_data['user']
#             if user.is_active:
#                 token,created = Token.objects.get_or_create(user = user)
#                 user_serializer = UserTokenSerializer(user)
#                 if created:
#                     return Response({
#                         'token': token.key, 
#                         'user':user_serializer.data,
#                         'message': 'login succesfully.'
#                     }, status.HTTP_201_CREATED)
#                 else:
#                     # all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
#                     # if all_sessions.exists():
#                     #     for session in all_sessions:
#                     #         session_data = session.get_decoded()
#                     #         if user.id == int(session_data.get('_auth_user_id')):
#                     #             session.delete() 
#                     # token.delete()
#                     # token = Token.objects.create(user = user)
#                     # return Response({
#                     #     'token': token.key, 
#                     #     'user':user_serializer.data,
#                     #     'message': 'login succesfully.'
#                     # }, status.HTTP_201_CREATED)
#                     token.delete()
#                     return Response({
#                         'error': 'Ya se ha iniciado sesion con este usuario.'
#                     }, status.HTTP_409_CONFLICT)
#             else:
#                 return Response({'message':'user is inactive'}, status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({'error':'username or password incorrect'}, status.HTTP_400_BAD_REQUEST)
#         return Response({'message': 'response'}, status.HTTP_200_OK)


# class Logout(APIView):

#     def get(self, request):
#         pass



