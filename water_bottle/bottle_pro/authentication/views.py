# from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import Userserializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser

class SignupView(APIView):
    
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = Userserializer(data= request.data)
        if serializer.is_valid():
            email=serializer.validated_data["email"]
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'This EmailId already taken'}, status=status.HTTP_400_BAD_REQUEST)
            user=serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()

            refresh= RefreshToken.for_user(user)
            user_data=Userserializer(user).data
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'usre':user_data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
   
