from django.contrib.auth.models import AbstractBaseUser,User, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image



class MyAccountManager(BaseUserManager):
    def create_user(self,display_name,email,username,first_name,last_name,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,display_name=display_name,username=username,first_name=first_name,last_name=last_name,**other_fields)
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser,PermissionsMixin):
    display_name = models.CharField(_('Display name'), max_length=40,unique=True,default='')
    email = models.EmailField(_('Email'), max_length=150,unique=True,default='')
    username = models.CharField(_('Username'), max_length=150,unique=True,default='')
    first_name = models.CharField(max_length=150,default='')
    last_name = models.CharField(max_length=150,default='')
    reg_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['display_name','email','first_name','last_name']

    def __str_(self):
        return self.display_name


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    avatar = models.ImageField(default='tester.png')
    bio = models.TextField()

    def __str__(self):
        return self.avatar

    def save(self,*args,**kwargs):
        super().save()

        image = Image.open(self.avatar.path)
        if image.height > 100 or image.width > 100:
            new_image = (100,100)
            image.thumbnail(new_image)
            image.save(self.avatar.path)