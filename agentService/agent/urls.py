from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .import views, restviews
from rest_framework import routers
from .commons import *

# rest web services
from .restviews import AgentImageAPIView

router = routers.DefaultRouter()

urlpatterns=[
    path('rest/', include(router.urls)),
    path('rest/getAgents/photo', AgentImageAPIView.as_view(),name="getagent-page"),
    path('rest/search/', restviews.search,name="search"),
    path('rest/auto_search/', restviews.auto_search,name="auto_search"),
    path('getKey/', views.getKey, name="getKey"),
    path('', views.handleShowAgent, name="agentLoginHome"),
    path(url_dict["index"], views.index, name="index"),
    path('search/', views.search, name="search"),
    path(url_dict["register"], views.handleAgent, name="register"),
    path(url_dict["showAgents"], views.showAgents, name="showAgents"),
    path(url_dict["searchByAgent"], views.searchByAgent, name="searchAgent"),
    path(url_dict["advSearch"], views.advSearchByAgent, name="advSearch"),
    path('agentLogin/', views.agentLogin, name="agentLogin"),
    path('agentLogout/', views.agentLogout, name="logout-page"),
    path(url_dict["imageUpload"], views.imageUpload,name="imageUpload"),
    #path('supervisorImageUpload/', views.supervisorImageUpload,name="superUserImageUpload-page"),
    path(url_dict["agentDetails"], views.agentDetails, name="agentDetails"),
    path('editProfile/', views.editProfile, name="edit-page"),
    path('changePassword/', views.changePassword, name="changePassword-page"),
    path(url_dict["createDepartment"], views.createDepartment, name="createDepartment"),
    path(url_dict["showDepartments"], views.showAllDepartments, name="showDepartments"),
    path('createRequest/', views.createRequest, name="createRequest"),
    path(url_dict["showRequests"], views.showRequests, name="showRequests"),
    #path('supervisorDetails/', views.supervisorDetails, name="showSupervisor-page"),

    path('<requestedBy>/unlockRequest/', views.unlockRequest, name="unlockRequest"),
    path(url_dict["imageData"], views.imageData, name="imageData"),
    path(url_dict["deptData"], views.deptData, name="deptData"),
    path(url_dict["searchByDepartment"],views.searchByDepartment,name="searchBydepartment"),
    path('createAddress/', views.createAddress, name="createAddress"),
    #path('showAllDepartments/', views.showAllDepartments, name="showAllDepartments-page"),
    #path('searchByDepartment/', views.searchByDepartment, name="showAllDepartments-page"),
]
