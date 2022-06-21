from django.shortcuts import render, redirect,Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from neighborhood.forms import UserUpdateForm, ProfileUpdateForm,LocationForm,HoodForm,ProfileForm,BusinessForm
from neighborhood.models import Location,UserHood,UserProfile,Business,MyUser,UserPost,Chama,PoliceDept,HealthDept
from neighborhood.api.serializers import PoliceSerializer,HealthSerializer
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
			location.user = current_user
			location.save()
			return redirect('hood')
	else:
		locform = LocationForm()
	return render(request,'user/location.html',{"locform":locform})

@login_required
def hood(request):
	user = request.user
	if request.method == 'POST':
		hoodform = HoodForm(request.POST)
		if hoodform.is_valid():
			print('valid!')
			name = hoodform.cleaned_data['name']
			hood = UserHood(name=name)
			hood.user = user
			hood.save()
			return redirect('profile',user.id)
	else:
		hoodform = HoodForm()
	return render(request,'user/hood.html',{"hoodform":hoodform})

@login_required
def profile(request,id):
	profile = UserProfile.objects.all().filter(id=id)
	location = Location.objects.all().filter(id=id)
	user = request.user
	if request.method == 'POST':
		profileform = ProfileForm(request.POST, request.FILES)
		if profileform.is_valid():
			print('valid!')
			bio = profileform.cleaned_data['bio']
			profile = UserProfile(bio=bio,)
			# profile.user = user
			profile.save()
		return redirect('profile',user.id)
	else:
		profileform = ProfileForm

	return render(request,'user/profile.html',{"profileform":profileform,"profile":profile,"location":location})

@login_required
def biz(request):
	if request.method == 'POST':
		bizform = BusinessForm(request.POST)
		if bizform.is_valid():
			print('valid!')
			name = bizform.cleaned_data['name']
			description = bizform.cleaned_data['description']
			hood_name = bizform.cleaned_data['hood_name']
			email = bizform.cleaned_data['email']
			phone = bizform.cleaned_data['phone']
			biz = Business(name=name,description=description,hood_name=hood_name,email=email,phone=phone)
			biz.save()
			return redirect('biz')
	else:
		bizform = BusinessForm

	return render(request,'hood/business.html',{"bizform":bizform})

def search(request):

	if 'business' in request.GET and request.GET["business"]:
		hood_name = request.GET.get("business")
		searched_businesses = Business.search_by_location(hood_name)
		message = f"{hood_name}"

		return render(request,'hood/search_results.html',{"message":message,"businesses":searched_businesses})
	else:
		message = "You haven't searched for an image yet"

		return render(request,'projects/search_results.html',{"message":message})

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

class NearbyPoliceDepts(APIView):
	def get(self,request, format=None):
		police = PoliceDept.objects.all()
		serializers = PoliceSerializer(police,many=True)
		return Response(serializers.data)

class NearbyHealthDepts(APIView):
	def get(self,request, format=None):
		health = HealthDept.objects.all()
		serializers = HealthSerializer(health,many=True)
		return Response(serializers.data)