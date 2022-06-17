from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from neighborhood.forms import UserUpdateForm, ProfileUpdateForm


# Create your views here.
@login_required
def home(request):
	return render(request, 'hood/index.html')


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

