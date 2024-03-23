from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Usermanager(BaseUserManager):
    
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("the email must be set"))
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,passwords,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('is_staff must be True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('is_superuser must be True'))
        return self.create_user(email,passwords,**extra_fields)
        

class User(AbstractBaseUser,PermissionsMixin):
    '''
    Custom user model for our app
    '''
    email= models.EmailField(max_length=250,unique=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    first_name=models.CharField(max_length=250)
    REQUIRED_FIELDS=[]
    objects=Usermanager()
    
    def __str__(self):
        
       return self.email