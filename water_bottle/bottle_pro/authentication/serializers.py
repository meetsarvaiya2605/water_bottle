from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email','username','first_name','last_name','password']    
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        
        return token 