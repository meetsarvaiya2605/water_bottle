from django.contrib import admin
from django.urls import path
from .views import SignupView,CustomTokenObtainPairView

urlpatterns = [
   path('signup/',SignupView.as_view(),name="signup" ),
   path('signin/', CustomTokenObtainPairView.as_view(), name="signin"),

]

