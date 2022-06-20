from django.contrib.auth.models import AbstractBaseUser,User, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image
from django_google_maps import fields as map_fields
from django.core.validators import MaxValueValidator, MinValueValidator


# auth models--to override django's registration
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,username=username,first_name=first_name,last_name=last_name,**other_fields)
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email'),max_length=150,unique=True,default='')
    username = models.CharField(_('Username'),max_length=150,unique=True,default='')
    first_name = models.CharField(max_length=150,default='')
    last_name = models.CharField(max_length=150,default='')
    reg_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']

    def __str_(self):
        return self.first_name


# content models below
class Location(models.Model):
    address = map_fields.AddressField(max_length=200,default='')
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, null=True)


class UserHood(models.Model):
    name = map_fields.AddressField(max_length=200,default='')

    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,null=True)


class UserProfile(models.Model):
    display_name = models.CharField(max_length=60,null=False,default='')
    bio = models.TextField(default='')
    avatar = models.ImageField(default='tester.png')
    created = models.DateTimeField(auto_now_add=True, null=True)

    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,null=True)

    def save(self,*args,**kwargs):
        super().save()


class UserPost(models.Model):
    title = models.CharField(max_length=60,null=False,default='')
    description = models.TextField(default='')
    published = models.DateTimeField(auto_now_add=True,null=True)
    address = map_fields.AddressField(max_length=200, default='')


    author = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING,null=True)


class Business(models.Model):
    name = models.CharField(max_length=40,default='')
    description = models.TextField()
    hood_name = map_fields.AddressField(max_length=200, default='')
    email = models.EmailField(max_length=150)
    phone = models.PositiveIntegerField(default=254,validators=[MinValueValidator(1),MaxValueValidator(10)])
    published = models.DateTimeField(auto_now_add=True, null=True)

    user = models.OneToOneField(MyUser,on_delete=models.DO_NOTHING,null=True)
    hood = models.ForeignKey(UserHood,on_delete=models.DO_NOTHING, null=True)

    @classmethod
    def search_by_location(cls, location_term):
        businesses = cls.objects.filter(location__location=location_term)
        return businesses


class Chama(models.Model):
    name = models.CharField(max_length=60,default='')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    address = map_fields.AddressField(max_length=200, default='')

    member = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING,null=True)


class PoliceDept(models.Model):
    name = models.CharField(max_length=60,default='')
    email = models.EmailField(max_length=150)
    phone = models.PositiveIntegerField(default=254,validators=[MinValueValidator(1),MaxValueValidator(10)])
    address = map_fields.AddressField(max_length=200, default='')
    policechief = models.CharField(max_length=60,default='')
    created = models.DateTimeField(auto_now_add=True,null=True)


class HealthDept(models.Model):
    name = models.CharField(max_length=60,default='')
    email = models.EmailField(max_length=150)
    phone = models.PositiveIntegerField(default=254, validators=[MinValueValidator(1), MaxValueValidator(10)])
    address = map_fields.AddressField(max_length=200, default='')
    created = models.DateTimeField(auto_now_add=True,null=True)
