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
    path('rest/auto_search/',restviews.auto_search ,name="auto_search"),
    path('getKey/', views.getKey, name="getKey"),
    path('', views.handleShowAgent, name="agentLoginHome"),
    #path(url_dict["index"], views.index, name="index"),
    path('search_url/', views.search_url, name="search_url"),
    path(url_dict["Create Agent"], views.handleAgent, name="Create Agent"),
    path(url_dict["Show Agents"], views.showAgents, name="Show Agents"),
    path(url_dict["Search Agent"], views.searchByAgent, name="Search Agent"),
    path(url_dict["advSearch"], views.advSearchByAgent, name="advSearch"),
    path('agentLogin/', views.agentLogin, name="agentLogin"),
    path('agentLogout/', views.agentLogout, name="logout-page"),
    path('imageUpload/', views.imageUpload,name="imageUpload"),
    #path('supervisorImageUpload/', views.supervisorImageUpload,name="superUserImageUpload-page"),
    path(url_dict["MY Profile"], views.agentDetails, name="MY Profile"),
    path('editProfile/', views.editProfile, name="edit-page"),
    path('changePassword/', views.changePassword, name="changePassword-page"),
    path(url_dict["Create Department"], views.createDepartment, name="createDepartment"),
    path(url_dict["Show Departments"], views.showAllDepartments, name="Show Departments"),
    path('createRequest/', views.createRequest, name="createRequest"),
    path(url_dict["Show Requests"], views.showRequests, name="Show Requests"),
    #path('supervisorDetails/', views.supervisorDetails, name="showSupervisor-page"),

    path('<requestedBy>/unlockRequest/', views.unlockRequest, name="unlockRequest"),
    path('<int:id>/imageData/', views.imageData, name="imageData"),
    path('<dept>/deptData/', views.deptData, name="deptData"),
    path(url_dict["Search Department"],views.searchByDepartment,name="Search Department"),
    path('createAddress/', views.createAddress, name="createAddress"),
    path('pAddressUpdate/', views.pAddressUpdate, name="pAddressUpdate"),
    path(url_dict["Create Partner"], views.partnerCreate, name="createPartner"),
    path(url_dict["Search Partner"], views.partnerSearch, name="partnerSearch"),
    path(url_dict["Update Partner"], views.partnerUpdate, name="partnerUpdate"),
    path('partnerUpdateSubmit/', views.partnerUpdateSubmit, name="partnerUpdateSubmit"),
    path('partnerLiveSearch/',views.partnerLiveSearch,name="partnerLiveSearch"),
    path('showPartners/',views.showPartners,name="showPartners"),
    path('createbranch/',views.createbranch,name="createbranch-page"),
    path('searchbranch/',views.searchbranch,name="searchbranch-page"),
    path('branchUpdate/',views.branchUpdate,name="branchUpdate-page"),
    path('branchUpdateSubmit/',views.branchUpdateSubmit,name="branchUpdateSubmit-page"),
    path('branchLiveSearch/',views.branchLiveSearch,name="branchLiveSearch-page"),
    path('invoiceSelect/',views.invoiceSelect,name="invoiceSelect"),
    path('invoiceCreate/',views.invoiceCreate,name="invoiceCreate"),

    #path('partnerAdvSearch/', views.partnerAdvSearch, name="partnerAdvSearch"),
    #path('createTaddress/', views.createTaddress, name="createTaddress"),
    #path('showAllDepartments/', views.showAllDepartments, name="showAllDepartments-page"),
    #path('searchByDepartment/', views.searchByDepartment, name="showAllDepartments-page"),
]
