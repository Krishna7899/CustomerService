from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AgentSerialize,SearchSerialize
from .models import AgentTable
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from .commons import url_dict
from .DButils import *
import json
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

#@api_view(['GET', 'POST'])
'''def getKey(request):
    search_value_list=()
    last_login = getLastLoginTime(request.session["id"])
    myId = request.session['id']
    agent_detail_obj = getLoggedInUserObject(myId)
    if 'search_key' in request.GET:
        search_key=request.GET.get('search_key')
        keys_list_dict = dict(filter(lambda item: search_key in item[0], url_dict.items()))
        for key in keys_list_dict.keys():
            search_value_list.append(key)
        return JsonResponse(search_value_list,safe=False)
    return render(request, 'agentDetails.html',
                  {"agentProfile": agent_detail_obj, "usertype": request.session["usertype"],
                   "last_login": last_login, "search_value_list": search_value_list})
'''
def search(request):
    return render(request, 'index.html')
#@api_view(['GET', 'POST'])
'''def auto_search(request):
    #if 'term' in request.GET:
        search_key="show"
        keys_list_dict = dict(filter(lambda item: search_key in item[0], url_dict.items()))
        #search_value_list = list()
        for key in keys_list_dict.keys():
            search_value_list.append(key)
        #print(search_value_list)
        return JsonResponse(keys_list_dict)*/
    #return render(request, 'index.html')'''

@api_view(['GET', 'POST'])
def auto_search(request):
    if 'term' in request.GET:
        search_value = request.GET.get('term')
        keys_list_dict = dict(filter(lambda item: search_value in item[0], url_dict.items()))
        results =SearchSerialize(keys_list_dict, many=True).data
    return Response(results)

def oldPasswordValidate(request):
    oldPassword = request.GET.get('old-password', None)
    data = {
        'is_taken': User.objects.filter(password__iexact=oldPassword).exists()
    }
    return JsonResponse(data)

#@api_view(['GET', 'POST'])
def partnerLiveSearch(request):
     partner_list = []
     if "name" in request.GET:
        search_name=request.GET.get("name")
        part_obj=getPartnerNames(search_name)
        for list in part_obj:
            partner_list.append(list.name)
        if partner_list:
            return JsonResponse(partner_list,safe=False)
        else:
            mesg=["No Data Found"]
            return JsonResponse(mesg,safe=False)