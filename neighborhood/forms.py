from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from neighborhood.models import MyUser,UserProfile,Location,UserHood,Business
from django import forms


class MyUserRegForm(RegistrationForm):

    class Meta:
        model = MyUser
        fields = ('first_name','last_name','username','email',)

class MyLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False )
    class Meta:
        model = MyUser
        fields = ('username',)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('username','email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio',)

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('address',)

class HoodForm(forms.ModelForm):
    class Meta:
        model = UserHood
        fields = ('name',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio',)

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name','description','hood_name','email','phone',)
