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
    path('', views.handleShowAgent, name="agentLoginHome"),
    path(url_dict["index"], views.index, name="index"),
    path('search/', views.search, name="search"),
    path(url_dict["register"], views.handleAgent, name="register"),
    path(url_dict["showAgents"], views.showAgents, name="showAgents"),
    path(url_dict["searchAgent"], views.searchByAgent, name="searchAgent"),
    path(url_dict["advSearch"], views.advSearchByAgent, name="advSearch"),
    path(url_dict["loginResult"], views.agentLogin, name="loginResult"),
    path('agentLogout/', views.agentLogout, name="logout-page"),
    path(url_dict["imageUpload"], views.imageUpload,name="imageUpload"),
    #path('supervisorImageUpload/', views.supervisorImageUpload,name="superUserImageUpload-page"),
    path(url_dict["agentDetails"], views.agentDetails, name="agentDetails"),
    path('editProfile/', views.editProfile, name="edit-page"),
    path('changePassword/', views.changePassword, name="changePassword-page"),
    path(url_dict["createDepartment"], views.createDepartment, name="createDepartment"),
    path(url_dict["showDepartments"], views.showAllDepartments, name="showDepartments"),
    path(url_dict["createRequest"], views.createRequest, name="createRequest"),
    path(url_dict["showRequests"], views.showRequests, name="showRequests"),
    #path('supervisorDetails/', views.supervisorDetails, name="showSupervisor-page"),

    path(url_dict["unlockRequest"], views.unlockRequest, name="unlockRequest"),
    path(url_dict["imageData"], views.imageData, name="imageData"),
    path(url_dict["deptData"], views.deptData, name="deptData"),
    path(url_dict["searchBydepartment"],views.searchByDepartment,name="searchBydepartment"),

    #path('showAllDepartments/', views.showAllDepartments, name="showAllDepartments-page"),
    #path('searchByDepartment/', views.searchByDepartment, name="showAllDepartments-page"),
]
