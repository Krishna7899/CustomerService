from rest_framework import serializers
from .models import AgentTable

class AgentSerialize(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AgentTable
		fields = ["image"]