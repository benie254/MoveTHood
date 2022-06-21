from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from neighborhood.forms import LocationForm,HoodForm,ProfileForm,BusinessForm,PostForm,UpdateLocation,UpdateHood
from neighborhood.models import Location,UserHood,UserProfile,Business,UserPost,PoliceDept,HealthDept,LocationUpdate,HoodUpdate
from neighborhood.api.serializers import PoliceSerializer,HealthSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from neighborhood.requests import get_quotes


# Create your views here.
@login_required
def home(request):
	user = request.user
	userloc = UserHood.objects.get(id=user.id)
	posts = UserPost.objects.all()
	print(user)
	print(userloc)
	print(posts)
	return render(request, 'hood/index.html',{"posts":posts,"userloc":userloc})


@login_required
def post(request):
	if request.method == 'POST':
		postform = PostForm(request.POST)
		if postform.is_valid():
			print('valid!')
			title = postform.cleaned_data['title']
			description = postform.cleaned_data['description']
			post = UserPost(title=title,description=description)
			post.save()
			return redirect('home')
	else:
		postform = PostForm()
	return render(request,'hood/post.html',{"postform":postform})


@login_required
def location(request):
	if request.method == 'POST':
		locform = LocationForm(request.POST)
		if locform.is_valid():
			print('valid!')
			address = locform.cleaned_data['address']
			location = Location(address=address)
			# location.user = current_user
			location.save()
			return redirect('hood')
	else:
		locform = LocationForm()
	return render(request,'user/location.html',{"locform":locform})


@login_required
def update_location(request):
	user = request.user
	if request.method == 'POST':
		updateloc = UpdateLocation(request.POST)
		if updateloc.is_valid():
			print('valid!')
			new_address = updateloc.cleaned_data['new_address']
			new_location = LocationUpdate(new_address=new_address)
			# new_location.user = current_user
			new_location.save()
			return redirect('profile',user.id)
	else:
		updateloc = UpdateLocation()
	return render(request,'user/update_location.html',{"updateloc":updateloc})


@login_required
def hood(request):
	user = request.user
	if request.method == 'POST':
		hoodform = HoodForm(request.POST)
		if hoodform.is_valid():
			print('valid!')
			name = hoodform.cleaned_data['name']
			hood = UserHood(name=name)
			# hood.user = user
			hood.save()
			return redirect('profile',user.id)
	else:
		hoodform = HoodForm()
	return render(request,'user/hood.html',{"hoodform":hoodform})


@login_required
def update_hood(request):
	user = request.user
	if request.method == 'POST':
		updatehood = UpdateHood(request.POST)
		if updatehood.is_valid():
			print('valid!')
			new_hood_name = updatehood.cleaned_data['new_hood_name']
			new_hood = HoodUpdate(new_hood_name=new_hood_name)
			# new_hood.user = user
			new_hood.save()
			return redirect('profile',user.id)
	else:
		updatehood = UpdateHood()
	return render(request,'user/update_hood.html',{"updatehood":updatehood})


@login_required
def profile(request,id):
	userhood = UserHood.objects.filter(id=id)
	userloc = Location.objects.filter(id=id)
	updatedloc = LocationUpdate.objects.all().last()
	updatedhood = HoodUpdate.objects.all().last()
	profile = UserProfile.objects.filter(id=id)
	businesses = Business.objects.all().filter(id=id)
	posts = UserPost.objects.all().filter(id=id)
	quotes = get_quotes()
	print(quotes)
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
	return render(request,'user/profile.html',{"profileform":profileform,"profile":profile,"userloc":userloc,"businesses":businesses,"posts":posts,"quotes":quotes,"userhood":userhood,"updatedloc":updatedloc,"updatedhood":updatedhood})


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
			return redirect('home')
	else:
		bizform = BusinessForm
	return render(request,'hood/business.html',{"bizform":bizform})


def search(request):
	user = request.user
	userloc = Location.objects.filter(id=user.id)
	print(userloc)

	if 'business' in request.GET and request.GET["business"]:
		hood_name = request.GET.get("business")
		searched_businesses = Business.search_by_location(hood_name)
		message = f"{hood_name}"

		return render(request,'hood/search_results.html',{"message":message,"businesses":searched_businesses,"userloc":userloc})
	else:
		message = "You haven't searched for an image yet"

		return render(request,'projects/search_results.html',{"message":message})


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
