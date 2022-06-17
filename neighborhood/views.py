from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, authenticate
from neighborhood.forms import MyUserRegForm, MyLoginForm, UserUpdateForm, ProfileUpdateForm
from neighborhood.models import MyUser
from django.views import View


# Create your views here.
@login_required
def home(request):
	return render(request, 'hood/index.html')


class MyRegView(View):
	form_class = MyUserRegForm
	initial = {'key': 'value'}
	template_name = 'auth/signup.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(to='/user/profile/')

		return super(MyRegView, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		regform = self.form_class(initial=self.initial)
		return render(request, self.template_name, {"regform": regform})

	def post(self, request, *args, **kwargs):
		regform = self.form_class(request.POST)

		if regform.is_valid():
			regform.save()

			username = regform.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')

			return redirect(to='/user/profile/')

		return render(request, self.template_name, {"regform": regform})

class MyLoginView(LoginView):
	form_class = MyLoginForm

	def form_valid(self, form):
		remember_me = form.cleaned_data.get('remember_me')

		if not remember_me:
			self.request.session.set_expiry(0)
			self.request.session.modified = True

		return super(MyLoginView, self).form_valid(form)

class ResetPassView(SuccessMessageMixin, PasswordResetView):
	template_name = 'auth/password_reset.html'
	email_template_name = 'auth/password_reset_email.html'
	subject_template_name = 'auth/password_reset_subject'
	success_message = 'Please check your email for your password reset instructions. If you do not receive an ' \
						'email from us, please confirm that the details you submitted are correct or check your spam ' \
						'folder. '
	success_url = reverse_lazy('home')

class ChangePassView(SuccessMessageMixin,PasswordChangeView):
	template_name = 'auth/change_password.html'
	success_message = 'Password successfully updated!'
	success_url = reverse_lazy('home')

@login_required
def profile(request):
	title = 'Profile'
	if request.method == 'POST':
		update_user_form = UserUpdateForm(request.POST,instance=request.user)
		update_profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

		if update_user_form.is_valid() and update_profile_form.is_valid():
			update_user_form.save()
			update_profile_form.save()
			messages.success(request,'Profile successfully updated!')
			return redirect(to='profile')

		else:
			update_user_form = UserUpdateForm(instance=request.user)
			update_profile_form = ProfileUpdateForm(instance=request.user.profile)
		return render(request,'user/profile.html',{'update_user_form':update_user_form,'update_profile_form':update_profile_form})

	return render(request,'user/profile.html',{"title":title})

