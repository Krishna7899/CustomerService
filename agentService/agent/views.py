# Create your views here.
import datetime

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from .DButils import *
from django.contrib.auth import logout
from .forms import AgentForm, ImageForm, RequestsForm, DepartmentForm
from django.shortcuts import render, redirect
from .models import Department, LogTable
from .commons import url_dict


# Create your views here.

# To show home page###
def index(request):
    return render(request, 'index.html', {})
def search(request):
    last_login = getLastLoginTime(request.session["id"])
    myId = request.session['id']
    agent_detail_obj = getLoggedInUserObject(myId)
    if request.method == "POST":
        search_key=request.POST["search"]
        search_value_list = []
        #keys_list =[val for key, val in url_dict.items() if search_key in key]
        keys_list_dict = dict(filter(lambda item: search_key in item[0], url_dict.items()))
        for key in keys_list_dict.keys():
            search_value_list.append(key)
        if len(search_value_list)>1:
            return render(request, 'agentDetails.html',
                      {"agentProfile": agent_detail_obj, "usertype": request.session["usertype"],
                       "last_login": last_login, "search_value_list": search_value_list})
        else:
            for key in url_dict.keys():
                if key==search_key:
                   view_name=url_dict[key]
                   return redirect('/agent/%s' % view_name)

                else:
                    continue

#agent login
def handleShowAgent(request):
    return render(request, 'agentLogin.html', {})


# Handling Login page of a Agent
def agentLogin(request):
    if request.method == 'GET':
        return render(request, "agentLogin.html", {})

    if request.method == 'POST':
        # Get the username and password from template
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            # Call function getAgentLoginValidation() from DB utils
            agent_Obj = getAgentLoginValidation(request, username, password)
            request.session["id"] = agent_Obj.id
            request.session["firstName"] = agent_Obj.firstName
            request.session["lastName"] = agent_Obj.lastName
            request.session["usertype"] = agent_Obj.usertype
            last_login=getLastLoginTime(request.session["id"])
            saveLoginTime(agent_Obj.id)
            return render(request, 'agentDetails.html', {"agentProfile": agent_Obj,"usertype":request.session["usertype"],"last_login":last_login})
        except ServiceException as ex:
            return render(request, "agentLogin.html", {"msg": ex.errorMessage})
# Registration of agent by supervisor only
def handleAgent(request):
    last_login = getLastLoginTime(request.session["id"])
    usertype = request.session["usertype"]
    if request.method == "GET":
        form = AgentForm()
        return render(request, 'agentRegistration.html', {'form': form,"usertype":usertype,"last_login":last_login})
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
    form = AgentForm(request.POST, request.FILES)
    try:

        createEmployeeValidation(request, email, username)
        if form.is_valid():
            form.save()
            return render(request, 'agentRegistration.html', {'form': form, 'message': 'success',"last_login":last_login})
    except ServiceException as ex:
        return render(request, 'agentRegistration.html', {'form': form, 'message': ex.errorMessage})


# Show all  agents when supervisor want the details
def showAgents(request):
    if request.method == "GET":
        show_agent_obj = showAllAgentsMethod()
        paginator = Paginator(show_agent_obj, 10)  # Show 10 agents per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if show_agent_obj:
            last_login = getLastLoginTime(request.session["id"])
            return render(request, "showAgents.html", {"show_agent_obj": show_agent_obj, "page_obj": page_obj,"last_login":last_login})

# Search agent details by using Id or username
def searchByAgent(request):
    usertype = request.session["usertype"]
    last_login = getLastLoginTime(request.session["id"])
    if request.method == "GET":
        form = AgentForm()
        return render(request, "searchAgent.html", {"form": form, "usertype": usertype,"last_login":last_login})
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            form = AgentForm(request.POST, request.FILES)
            search_by_name = getDetailsByName(username)
            if search_by_name:
                return render(request, "searchAgent.html",
                              {"search_by_name": search_by_name, "usertype": usertype, "form": form,"last_login":last_login})
        except:
            return render(request, "searchAgent.html",
                          {"usertype": usertype, "form": form, "msg": "No data Found"})

def advSearchByAgent(request):
    usertype = request.session["usertype"]
    if 'firstName' in request.GET:
        firstName = request.GET["firstName"]
    if 'lastName' in request.GET:
        lastName = request.GET["lastName"]
    if 'username' in request.GET:
        username = request.GET["username"]
    #adv_search_obj = AgentTable.objects.filter(Q(firstName=firstName) | Q(lastName=lastName) | Q(username=username))
    adv_search_obj = advancedSearchMethod(firstName, lastName, username)
    paginator = Paginator(adv_search_obj, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    GET_params = request.GET.copy()

    if adv_search_obj:
        last_login = getLastLoginTime(request.session["id"])
        return render(request, "searchAgent.html",
            {"adv_search_obj": adv_search_obj, "usertype": usertype, 'page_obj': page_obj,'GET_params':GET_params,"last_login":last_login})

    else:
        return render(request, "searchAgent.html", {"usertype": usertype})

# Once Login as Supervisor show below page
'''def supervisorDetails(request):
    myId = request.session['id']
    agentProfile = getLoggedInUserObject(myId)
    last_login = getLastLoginTime(request.session["id"])
    return render(request, "agentDetails.html", {"agentProfile": agentProfile, "msg": "MY Image","last_login":last_login})'''


# Handling Logout activity
def agentLogout(request):
    sessionId = request.session["id"]
    saveLogoutTime(sessionId)
    '''logoutTime = datetime.datetime.now()
    LogTable.objects.filter(sessionId=sessionId).update(logoutTime=logoutTime)'''
    logout(request)
    #saveLogoutTime(sessionId)
    return render(request, "agentLogin.html", {})
    del request.session["username"]
    del request.session["password"]


# here we upload agent profile image

def imageUpload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        myId = request.session["id"]
        image_uploadObj = getLoggedInUserObject(myId)
        last_login = getLastLoginTime(request.session["id"])
        if form.is_valid():
            image_uploadObj.image = form.cleaned_data['image']
            image_uploadObj.save()
            return render(request, 'agentDetails.html', {"agentProfile": image_uploadObj, "msg": "MY Image","last_login":last_login})

# Navigate to  Agent details page when we click on myprofile
def agentDetails(request):
    usertype = request.session["usertype"]
    if request.method == 'GET':
        myId = request.session['id']
        agent_detail_obj = getLoggedInUserObject(myId)
        last_login = getLastLoginTime(request.session["id"])
        return render(request, 'agentDetails.html', {"agentProfile": agent_detail_obj,"usertype":usertype, "msg": "MY Image","last_login":last_login})

# Editing profile of agent when agent login only
def editProfile(request):
    myId = request.session['id']
    edit_obj = getLoggedInUserObject(myId)
    if request.method == 'GET':
        return render(request, 'editProfile.html', {"agentProfile": edit_obj})
    if request.method == 'POST':
        myId = request.session['id']
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        try:
            agent_detail_obj = editLoggedInAgentProfile(request, firstName, lastName, email,myId)
            last_login = getLastLoginTime(request.session["id"])
            if agent_detail_obj:
                return render(request, 'agentDetails.html', {"agentProfile": agent_detail_obj, "msg": "MY Image","last_login":last_login})
        except ServiceException as ex:
            return render(request, 'agentDetails.html', {"errorMsg": ex.errorMessage})


# Changing password of agent when by agent only
def changePassword(request):
    last_login = getLastLoginTime(request.session["id"])
    if request.method == 'GET':
        myId = request.session["id"]
        change_obj = getLoggedInUserObject(myId)
        return render(request, 'changePassword.html', {"agentProfile": change_obj,"last_login":last_login})

    if request.method == 'POST':
        myId = request.session['id']
        oldPassword = request.POST["old-password"]
        newPassword = request.POST["new-password"]

    try:

        change_obj = passwordChangeObject(request, oldPassword,newPassword,myId)

        if (change_obj):
            return render(request, 'agentDetails.html', {"agentProfile": change_obj,"last_login":last_login})
    except ServiceException as ex:
        return render(request, 'agentDetails.html', {"changeMsg": ex.errorMessage})


# Department creation by supervisor
def createDepartment(request):
    usertype = request.session["usertype"]
    last_login = getLastLoginTime(request.session["id"])
    if request.method == "GET":
        form = DepartmentForm()
        return render(request, "createDepartment.html", {"form": form,"usertype":usertype,"last_login":last_login})
    if request.method == "POST":
        deptName = request.POST["deptName"]
        createdBy_id = request.session["id"]
        # deptName=AgentTable.objects.get(dept=deptName_Id)
        if Department.objects.filter(deptName=deptName).exists():
            return render(request, "createDepartment.html", {"usertype":usertype,"msg": "department name is already in use"})
        else:
            Department.objects.create(deptName=deptName, createdBy_id=createdBy_id)
            form = DepartmentForm(request.POST, request.FILES)
            return render(request, "createDepartment.html",
                          {"form": form,"usertype":usertype,"last_login":last_login,"msg": "Success",})


# Showing all departments by supervisor
def showAllDepartments(request):
    usertype = request.session["usertype"]
    if request.method == "GET":
        show_Dept_Obj = Department.objects.all()
        paginator = Paginator(show_Dept_Obj, 5)  # Show 8 agents per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        last_login = getLastLoginTime(request.session["id"])
        return render(request, "showAllDepartments.html", {"show_Dept_Obj": show_Dept_Obj,"usertype":usertype, "page_obj": page_obj,"last_login":last_login})


# When Account is locked ,request for unlock displayed in unlock
def createRequest(request):
    if request.method == "GET":
        form = RequestsForm()
        return render(request, "createRequest.html", {"form": form})
    if request.method == "POST":
        username = request.POST.get("requestedUserName")
        description = request.POST.get("description")
        requestType = request.POST.get("requestType")

        requestedBy_id = getIdByUserName(username)
        request_post_obj = createRequestMethod(requestedBy_id, username, description, requestType)
        form = RequestsForm(request.POST, request.FILES)

        if request_post_obj:
            return render(request, "createRequest.html", {"form": form, "message": "RequestPosted"})


# show requests to supervisor
def showRequests(request):
    usertype = request.session["usertype"]
    if request.method == "GET":
        show_req_obj = showAllRequestsMethod()
        last_login = getLastLoginTime(request.session["id"])
        if show_req_obj:
            return render(request, "showRequest.html", {"show_req_obj": show_req_obj,"usertype":usertype, "last_login":last_login})
        else:
            return render(request, "showRequest.html",{ "last_login": last_login,"usertype":usertype,"message":"no data found"})
def unlockRequest(request,requestedBy):
    #requestedBy = request.POST.get('requestedBy')
    count_obj = AgentTable.objects.get(username=requestedBy)
    if count_obj.count>= 5:
       AgentTable.objects.filter(username=requestedBy).update(count=0)
       Requests.objects.filter(requestedUserName=requestedBy).update(status="Approved")
       return render(request, "showRequest.html", {"message": "unlock success"})
    else:
        Requests.objects.filter(requestedUserName=requestedBy).update(status="Approved")
        return render(request, "showRequest.html", {"message": "Approved Already"})

def imageData(request, id):
    image_details = getAgentDetailsImageClick(id)
    # image_details=AgentTable.objects.get(id=id)
    usertype = request.session["usertype"]
    last_login = getLastLoginTime(request.session["id"])
    try:
        if image_details:
            return render(request, "showDetailImageClick.html", {"show_image_obj": image_details, "usertype": usertype,"last_login":last_login})

    except:
        return render(request, "showDetailImageClick.html", {"msg": "No details Found"})


def deptData(request, dept):
    usertype = request.session["usertype"]
    deptDetails = getDepartmentDetails(dept)
    # deptDetails=Department.objects.filter(deptName=dept)
    last_login = getLastLoginTime(request.session["id"])
    try:
        if deptDetails:
            return render(request, "showDeptDetailsClick.html", {"deptDetails": deptDetails, "usertype": usertype,"last_login":last_login})

    except:
        return render(request, "showDeptDetailsClick.html", {"msg": "No details Found"})

def searchByDepartment(request):
    usertype=request.session['usertype']
    if request.method=='GET':
        form=DepartmentForm()
        return render(request,"searchdepartment.html",{'form':form,"usertype":usertype})
    if request.method == "POST":
        department=request.POST["department"]
        form = DepartmentForm(request.POST)
        try:
            search_by_department = getdetailsbyDepartment(department)
            if search_by_department:
                return render(request,"searchdepartment.html",{"search_by_department":search_by_department,"usertype":usertype,'form':form})
        except:
            return render(request,"searchdepartment.html",{"usertype":usertype,"form":form ,"msg":"No details found"})