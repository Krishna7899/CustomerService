from rest_framework import serializers
from .models import AgentTable,Partner

class AgentSerialize(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AgentTable
		fields = ["image"]

class SearchSerialize(serializers.HyperlinkedModelSerializer):
	url_dict_Key=serializers.CharField()
	url_dict_value=serializers.CharField()


class PartnerSerialize(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Partner
		fields = ["name"]