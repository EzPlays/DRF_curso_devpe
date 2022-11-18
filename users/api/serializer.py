from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def validate_name(self, value):
        #custom validation
        if 'dev' in value:
            raise serializers.ValidationError('Error, can not exists user whit username')
        return value

    def validate_email(self, value):
        #custom validate
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('el email no puedo contener el nombre')
        if value == '':
            raise serializers.ValidationError('Error, write a validate email')
        return value

    def validate(self, data):
        
        return data

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance)
