from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from neighborhood.forms import MyUserRegForm, MyLoginForm
from django.views import View


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
