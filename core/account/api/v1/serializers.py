from rest_framework import serializers
from account.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class UserListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password','user_permissions','groups']

class UserRegisterSerilizer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=250)
    class Meta:
        model = User
        fields = ['email','password','password1']
    
    def validate(self,attrs):

        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError('passwords does not match.')
        else:
            return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("password1", None)
        return User.objects.create_user(**validated_data)

class ChangePasswordSerialier(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError({"detail": "passswords doesnt match"})

        try:
            validate_password(attrs.get("new_password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})

        return super().validate(attrs)