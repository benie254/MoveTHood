from rest_framework import serializers
from neighborhood.models import HealthDept,PoliceDept


class PoliceSerializer(serializers.ModelSerializer):
	class Meta:
		model = PoliceDept
		fields = ('id','name','email','address','email','phone',)


class HealthSerializer(serializers.ModelSerializer):
	class Meta:
		model = HealthDept
		fields = ('id','name','address','email','phone',)
