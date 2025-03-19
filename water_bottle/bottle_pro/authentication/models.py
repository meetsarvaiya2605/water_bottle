from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# Create your models here.


class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=50,unique=False)
    
    groups = models.ManyToManyField(Group,related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission,related_name='custom_user_permissions', blank=True) 
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    
    def __str__(self):
        return self.email
    
