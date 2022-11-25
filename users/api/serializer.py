from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','last_name')

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
    def to_representation(self, instance):
        #con values en la consulta
        return {
            'id': instance['id'],
            'name': instance['name'],
            'username': instance['username'],
            'email': instance['email'],
        }
        #con all() en la consulta
        # return {
        #     'id': instance.id,
        #     'username': instance.username,
        #     'email': instance.email,
        #     'password': instance.password,
        # }



# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()

#     def validate_name(self, value):
#         #custom validation
#         if 'dev' in value:
#             raise serializers.ValidationError('Error, can not exists user whit username')
#         return value

#     def validate_email(self, value):
#         #custom validate
#         # if self.validate_name(self.context['name']) in value:
#         #     raise serializers.ValidationError('el email no puedo contener el nombre')
#         if value == '':
#             raise serializers.ValidationError('Error, write a validate email')
#         return value

#     def validate(self, data):
        
#         return data

#     def create(self, validated_data):
#         print(validated_data)
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance

#     # def save(self):
#     #     print(self.validated_data)
#     #     send_email()

