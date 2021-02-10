from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .import views, restviews
from rest_framework import routers


# rest web services
from .restviews import AgentImageAPIView

router = routers.DefaultRouter()


urlpatterns=[
    path('rest/', include(router.urls)),
    path('rest/getAgents/photo', AgentImageAPIView.as_view(),name="getagent-page"),
    path('', views.handleShowAgent, name="agent-page"),
    path('index/', views.index, name="index-page"),
    path('search/', views.search, name="search"),
    path('register/', views.handleAgent, name="register-page"),
    path('showAgents/', views.showAgents, name="showAgents-page"),
    path('searchByAgent/', views.searchByAgent, name="searchAgents-page"),
    path('agentLogin/', views.agentLogin, name="login-page"),
    path('agentLogout/', views.agentLogout, name="logout-page"),
    path('upload/', views.imageUpload,name="upload-page"),
    #path('supervisorImageUpload/', views.supervisorImageUpload,name="superUserImageUpload-page"),
    path('agentProfile/', views.agentDetails, name="profile-page"),
    path('editProfile/', views.editProfile, name="edit-page"),
    path('changePassword/', views.changePassword, name="changePassword-page"),
    path('createDepartment/', views.createDepartment, name="createDepartment-page"),
    path('showAllDepartments/', views.showAllDepartments, name="createDepartment-page"),
    path('createRequest/', views.createRequest, name="createRequest-page"),
    path('showRequests/', views.showRequests, name="showRequests-page"),
    #path('supervisorDetails/', views.supervisorDetails, name="showSupervisor-page"),
    path('advSearchByAgent/', views.advSearchByAgent, name="advSearchByAgent-page"),
    path('<requestedBy>/unlockRequest/', views.unlockRequest, name="unlockRequest"),
    path('<int:id>/imageData/', views.imageData, name="imageData"),
    path('<dept>/deptData/', views.deptData, name="deptData"),
    path('searchbydepartment/',views.searchbydepartment,name="searchbydepartment-page"),

    #path('showAllDepartments/', views.showAllDepartments, name="showAllDepartments-page"),
    #path('searchByDepartment/', views.searchByDepartment, name="showAllDepartments-page"),
]
