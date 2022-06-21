"""Hood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path as url
from django.contrib.auth import views as auth_views
from neighborhood.auth.views import MyRegView,MyLoginView
from neighborhood.views import home,profile,location,hood
from neighborhood.forms import MyLoginForm
from neighborhood import views
from neighborhood.views import biz,search,post,update_hood,update_location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('hood/post/add/',post,name='post'),
    path('hood/business/add/',biz,name='biz'),
    path('search/term/',search,name='search'),
    path('user/info/locale/',location,name='location'),
    path('user/info/location/update',update_location,name='update-loc'),
    path('user/info/hood/update/',update_hood,name='update-hood'),
    path('user/info/hood/',hood,name='hood'),
    path('user/<int:id>/profile/',profile,name='profile'),
    path('user/register/',MyRegView.as_view(),name='register'),
    path('user/login/',MyLoginView.as_view(redirect_authenticated_user=True,template_name='auth/login.html',authentication_form=MyLoginForm),name='login'),
    path('user/logout/',auth_views.LogoutView.as_view(template_name='auth/login.html'),name='logout'),
    url(r'^oauth/',include('social_django.urls',namespace='social')),
    path('api/hood/police/nearby/', views.NearbyPoliceDepts.as_view()),
    path('api/hood/health/nearby/', views.NearbyHealthDepts.as_view()),
]
