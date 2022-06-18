from rest_framework import serializers
from neighborhood.models import Business


class BizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Business
		fields = ('name','description','location','email','phone')
