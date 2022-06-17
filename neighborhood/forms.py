from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from neighborhood.models import MyUser,Profile
from django import forms


class MyUserRegForm(RegistrationForm):

    class Meta:
        model = MyUser
        fields = ('display_name','first_name','last_name','username','email',)

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
        model = Profile
        fields = ('avatar','bio')
