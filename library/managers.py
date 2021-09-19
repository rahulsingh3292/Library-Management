from django.contrib.auth.base_user import BaseUserManager 
from django.db import models 
from django.contrib.auth.models import AbstractUser

class UserManager(BaseUserManager):
  use_in_migrations = True 
  
  def create_user(self,email,password=None,**extra_fileds):
    if not email:
      raise ValueError("Email is required")
      
    extra_fileds.setdefault("is_superuser",False)
    extra_fileds.setdefault("is_staff",False)
    email = self.normalize_email(email)
    user = self.model(email=email,**extra_fileds)
    user.set_password(password)
    user.save(using=self._db)
    return user 
  
  def create_superuser(self,email,password=None,**extra_fileds):
    if not email:
      raise ValueError("Email is required")
    extra_fileds.setdefault("is_staff",True)
    extra_fileds.setdefault("is_superuser",True)
    
    return self.create_user(email,password,**extra_fileds)

class User(AbstractUser):
  username = None 
  email = models.EmailField(max_length=200,unique=True)
  requested_admin_ac = models.BooleanField(default=False)
  is_admin_user = models.BooleanField(default=False)
  objects = UserManager()
  EMAIL_FIELD = "email"
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS =[]
  
  def __str__(self):
    return self.email
  
 