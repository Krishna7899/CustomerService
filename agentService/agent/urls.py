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
    path(dict["index"], views.index, name="index"),
    path('search/', views.search, name="search"),
    path(dict["register"], views.handleAgent, name="register"),
    path(dict["showAgents"], views.showAgents, name="showAgents"),
    path(dict["searchAgent"], views.searchByAgent, name="searchAgent"),
    path(dict["advSearch"], views.advSearchByAgent, name="advSearch"),
    path(dict["loginResult"], views.agentLogin, name="loginResult"),
    path('agentLogout/', views.agentLogout, name="logout-page"),
    path(dict["imageUpload"], views.imageUpload,name="imageUpload"),
    #path('supervisorImageUpload/', views.supervisorImageUpload,name="superUserImageUpload-page"),
    path(dict["agentDetails"], views.agentDetails, name="agentDetails"),
    path('editProfile/', views.editProfile, name="edit-page"),
    path('changePassword/', views.changePassword, name="changePassword-page"),
    path(dict["createDepartment"], views.createDepartment, name="createDepartment"),
    path(dict["showDepartments"], views.showAllDepartments, name="showDepartments"),
    path(dict["createRequest"], views.createRequest, name="createRequest"),
    path(dict["showRequests"], views.showRequests, name="showRequests"),
    #path('supervisorDetails/', views.supervisorDetails, name="showSupervisor-page"),

    path(dict["unlockRequest"], views.unlockRequest, name="unlockRequest"),
    path(dict["imageData"], views.imageData, name="imageData"),
    path(dict["deptData"], views.deptData, name="deptData"),
    path(dict["searchBydepartment"],views.searchByDepartment,name="searchBydepartment"),

    #path('showAllDepartments/', views.showAllDepartments, name="showAllDepartments-page"),
    #path('searchByDepartment/', views.searchByDepartment, name="showAllDepartments-page"),
]
