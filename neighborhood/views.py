from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from neighborhood.forms import UserUpdateForm, ProfileUpdateForm,LocationForm,HoodForm,ProfileForm
from neighborhood.models import Location,UserHood,UserProfile,Business
from neighborhood.api.serializers import BizSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
@login_required
def home(request):
	return render(request, 'hood/index.html')

@login_required
def location(request):
	current_user = request.user
	if request.method == 'POST':
		locform = LocationForm(request.POST)
		if locform.is_valid():
			print('valid!')
			address = locform.cleaned_data['address']
			location = Location(address=address)
			# location.creator = current_user
			location.save()
			return redirect('hood')
	else:
		locform = LocationForm()
	return render(request,'user/location.html',{"locform":locform})

@login_required
def hood(request):
	current_user = request.user
	if request.method == 'POST':
		hoodform = HoodForm(request.POST)
		if hoodform.is_valid():
			print('valid!')
			name = hoodform.cleaned_data['name']
			hood = UserHood(name=name)
			# location.creator = current_user
			hood.save()
			return redirect('profile')
	else:
		hoodform = HoodForm()
	return render(request,'user/hood.html',{"hoodform":hoodform})

@login_required
def profile(request):
	current_user = request.user
	if request.method == 'POST':
		profileform = ProfileForm(request.POST, request.FILES)
		if profileform.is_valid():
			print('valid!')
			bio = profileform.cleaned_data['bio']
			avatar = profileform.cleaned_data['avatar']
			profile = UserProfile(bio=bio, avatar=avatar)
			profile.user = current_user
			profile.save()
		return redirect('profile')
	else:
		profileform = ProfileForm

	return render(request,'user/profile.html',{"profileform":profileform})


# @login_required
# def profile(request):
# 	title = 'Profile'
# 	update_user_form = UserUpdateForm
# 	update_profile_form = ProfileUpdateForm
# 	if request.method == 'POST':
# 		update_user_form = UserUpdateForm(request.POST,instance=request.user)
# 		update_profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.userprofile)
# 		if update_user_form.is_valid() and update_profile_form.is_valid():
# 			update_user_form.save()
# 			update_profile_form.save()
# 			messages.success(request,'Profile successfully updated!')
# 			return redirect(to='profile')
# 		else:
# 			update_user_form = UserUpdateForm(instance=request.user)
# 			update_profile_form = ProfileUpdateForm(instance=request.user.profile)
# 		return render(request,'user/profile.html',{'update_user_form':update_user_form,'update_profile_form':update_profile_form})
# 	return render(request,'user/profile.html',{"title":title,'update_user_form':update_user_form,'update_profile_form':update_profile_form})
#

class BusinessList(APIView):
	def get(self,request,format='None'):
		current_user = request.user
		user_location = Location.objects.filter(pk=current_user.id)
		businesses = Business.objects.filter(location=user_location)
		serializers = BizSerializer(businesses,many=True)
		return Response(serializers.data)
