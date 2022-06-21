from django.contrib.auth.models import AbstractBaseUser,User, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
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


class UserHood(models.Model):
    name = map_fields.AddressField(max_length=200,default='')
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,null=True)

    def create_hood(self):
        self.hood = UserHood(name=self.name)
        self.hood.save()

    def save_hood(self):
        self.save()

    def update_hood(self):
        self.updated_hood = UserHood.objects.filter(id=self.pk).update(name=self.name)
        self.updated_hood.save()

    @classmethod
    def get_by_id(cls, id):
        hood = cls.objects.filter(id=id)
        return hood

    def delete_hood(self):
        self.delete()


class UserProfile(models.Model):
    bio = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING,null=True)

    def save(self,*args,**kwargs):
        super().save()

    def update_occupant(self):
        updated_occupants = UserProfile.objects.filter(id=self.pk).update(bio=self.bio)
        updated_occupants.save()


class Location(models.Model):
    address = map_fields.AddressField(max_length=200, default='')
    user = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING, null=True)
    occupants = models.ForeignKey(UserProfile,on_delete=models.DO_NOTHING,null=True)


class UserPost(models.Model):
    title = models.CharField(max_length=60,null=False,default='')
    description = models.TextField(default='')
    published = models.DateTimeField(auto_now_add=True,null=True)
    author = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING,null=True)


class Business(models.Model):
    name = models.CharField(max_length=40,default='')
    description = models.TextField()
    hood_name = map_fields.AddressField(max_length=200, default='')
    email = models.EmailField(max_length=150)
    phone = models.PositiveIntegerField(default=254,)
    published = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(MyUser,on_delete=models.DO_NOTHING,null=True)
    hood = models.ForeignKey(UserHood,on_delete=models.DO_NOTHING, null=True)

    def create_business(self):
        self.business = Business(name=self.name, description=self.description,hood_name=self.hood_name,email=self.email,phone=self.phone)
        self.business.save()

    def save_business(self):
        self.save()

    def update_business(self):
        self.updated_biz = Business.objects.filter(id=self.pk).update(name=self.name, description=self.description,hood_name=self.hood_name,email=self.email,phone=self.phone)
        self.updated_biz.save()

    @classmethod
    def search_by_location(cls, hood_name):
        businesses = cls.objects.filter(hood_name__icontains=hood_name)
        return businesses

    @classmethod
    def get_by_id(cls, id):
        business = cls.objects.filter(id=id)
        return business

    def delete_business(self):
        self.delete()


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
    hood = map_fields.AddressField(max_length=200, default='')
    police_chief = models.CharField(max_length=60,default='')
    created = models.DateTimeField(auto_now_add=True,null=True)


class HealthDept(models.Model):
    name = models.CharField(max_length=60,default='')
    email = models.EmailField(max_length=150)
    phone = models.PositiveIntegerField(default=254, validators=[MinValueValidator(1), MaxValueValidator(10)])
    address = map_fields.AddressField(max_length=200, default='')
    hood = map_fields.AddressField(max_length=200, default='')
    created = models.DateTimeField(auto_now_add=True,null=True)


class Quote:
    author = models.CharField(max_length=300,null=True)
    quote = models.CharField(max_length=300,null=True)


class LocationUpdate(models.Model):
    new_address = map_fields.AddressField(max_length=200, default='')

class HoodUpdate(models.Model):
    new_hood_name = map_fields.AddressField(max_length=200, default='')