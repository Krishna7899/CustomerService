from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AgentSerialize
from .models import AgentTable
from rest_framework import status
from django.contrib.auth.models import User
"""class AgentViewSet(viewsets.ModelViewSet):
	queryset = AgentTable.objects.all() #what to retrive
	serializer_class = AgentSerialize #which should obj holds the response


@api_view(["GET"])
@csrf_exempt
def getAgents(request):
    # get the data

    agents = AgentTable.objects.all()
    # wrap to serializer
    serializer = AgentSerialize(agents, many=True, context={
        'request': request,
    })

    # add to json response
    return JsonResponse({'agents': serializer.data}, safe=False, status=status.HTTP_200_OK)"""

class AgentImageAPIView(APIView):
    serializer_class=AgentSerialize

    def get_queryset(self):
        agentImages=AgentTable.objects.all()
        return  agentImages

    def get(self,request,*args,**kwargs):
        try:
            id=request.query_params["id"]
            if id != None:
                agentImage=AgentTable.objects.get(id=id)
                serializer=AgentSerialize(agentImage)

        except:
            agentImages=self.get_queryset()
            serializer=AgentSerialize(agentImages,many=True)
        return Response(serializer.data)

