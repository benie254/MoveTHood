from django.contrib.auth.models import AbstractBaseUser,User, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image
from django_google_maps import fields as map_fields
from django.core.validators import MaxValueValidator, MinValueValidator


# auth models--to override django's registration
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
    display_name = models.CharField(_('Display name'),max_length=40,unique=True,default='')
    email = models.EmailField(_('Email'),max_length=150,unique=True,default='')
    username = models.CharField(_('Username'),max_length=150,unique=True,default='')
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


# content models below
class Location(models.Model):
    address = map_fields.AddressField(max_length=200,default='')
    geolocation = map_fields.GeoLocationField(max_length=100,default='')


class UserHood(models.Model):
    name = models.CharField(max_length=40,default='')

    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)


class UserProfile(models.Model):
    bio = models.TextField(default='')
    avatar = models.ImageField(default='tester.png')
    created = models.DateTimeField(auto_now_add=True, null=True)

    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING)
    hood = models.ForeignKey(UserHood,on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.avatar

    def save(self,*args,**kwargs):
        super().save()

        image = Image.open(self.avatar.path)
        if image.height > 100 or image.width > 100:
            new_image = (100,100)
            image.thumbnail(new_image)
            image.save(self.avatar.path)


class UserPost(models.Model):
    title = models.CharField(max_length=60,null=False,default='')
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True,null=True)

    author = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    hood = models.ForeignKey(UserHood,on_delete=models.DO_NOTHING)


class Business(models.Model):
    name = models.CharField(max_length=40,default='')
    description = models.TextField()
    email = models.EmailField(max_length=150)
    phone = models.PositiveIntegerField(default=254,validators=[MinValueValidator(1),MaxValueValidator(10)])
    published = models.DateTimeField(auto_now_add=True, null=True)

    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    hood = models.ForeignKey(UserHood,on_delete=models.DO_NOTHING)


class Chama(models.Model):
    name = models.CharField(max_length=60,default='')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    member = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    hood = models.ForeignKey(UserHood,on_delete=models.DO_NOTHING)


class PoliceChief(models.Model):
    name = models.CharField(max_length=60,default='')
    age = models.PositiveSmallIntegerField(default=35,validators=[MinValueValidator(1),MaxValueValidator(75)])
    email = models.EmailField(max_length=150)
    added = models.DateTimeField(auto_now_add=True, null=True)

    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    hood = models.ForeignKey(UserHood,on_delete=models.DO_NOTHING)


class PoliceDept(models.Model):
    name = models.CharField(max_length=60,default='')
    email = models.EmailField(max_length=150)
    phone = models.PositiveIntegerField(default=254,validators=[MinValueValidator(1),MaxValueValidator(10)])
    created = models.DateTimeField(auto_now_add=True,null=True)

    chief = models.ForeignKey(PoliceChief, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    hood = models.ForeignKey(UserHood,on_delete=models.DO_NOTHING)


class HealthDept(models.Model):
    name = models.CharField(max_length=60,default='')
    email = models.EmailField(max_length=150)
    phone = models.PositiveIntegerField(default=254, validators=[MinValueValidator(1), MaxValueValidator(10)])
    created = models.DateTimeField(auto_now_add=True, null=True)

    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    hood = models.ForeignKey(UserHood, on_delete=models.DO_NOTHING)
