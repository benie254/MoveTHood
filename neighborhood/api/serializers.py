from rest_framework import serializers
from neighborhood.models import Business,UserPost,Chama,HealthDept,PoliceDept


class BizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Business
		fields = ('id','name','description','address','email','phone',)

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserPost
		fields = ('id','title','description','address')

class ChamaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chama
		fields = ('id','name','description','address')

class PoliceSerializer(serializers.ModelSerializer):
	class Meta:
		model = PoliceDept
		fields = ('id','name','email','address','email','phone',)

class HealthSerializer(serializers.ModelSerializer):
	class Meta:
		model = HealthDept
		fields = ('id','name','address','email','phone',)
