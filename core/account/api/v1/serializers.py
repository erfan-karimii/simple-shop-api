from rest_framework import serializers
from account.models import User

class UserListSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password','user_permissions','groups']

class UserRegisterSerilizers(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=250)
    class Meta:
        model = User
        fields = ['email','password','password2']
    
    def validate(self,obj):
        if obj.get('password')== obj.get('password2'):
            password2 = obj.pop('password2')
            print(obj,'fjisdhfiohfihaifhauihfdsuiafhduio')
            return obj
        else:
            raise serializers.ValidationError('passwords does not match.')