from django.contrib import admin
from .models import MyUser,UserProfile,Location,Business


# class ImageAdmin(admin.ModelAdmin):
#     # filter_horizontal=('tag',)


# Register your models here.
admin.site.register(MyUser)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Location)