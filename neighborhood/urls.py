from django.urls import path,re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.home,name='home'),
    path('api/hood/business/',views.BusinessList.as_view()),
    # path('api/',views.api,name='api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
