from rest_framework import serializers
from .models import AgentTable

class AgentSerialize(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AgentTable
		fields = ["image"]

class SearchSerialize(serializers.HyperlinkedModelSerializer):
	url_dict_Key=serializers.CharField()
	url_dict_value=serializers.CharField()