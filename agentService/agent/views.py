# Create your views here.
import datetime
from re import search
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.urls import reverse
from .DButils import *
from django.contrib.auth import logout
from .forms import AgentForm, ImageForm, RequestsForm, DepartmentForm, AddressForm
from django.shortcuts import render, redirect
from .models import Department, LogTable, AddressTable
from .commons import url_dict
from django.http import HttpResponse
import json


# Create your views here.

def getKey(request):
    search_value_list = list()
    if 'term' in request.GET:
        search_value = request.GET.get('term')
        for key in url_dict.keys():
            if search_value.lower() in key.lower():
                search_value_list.append(key)
        if search_value_list:
            return JsonResponse(search_value_list, safe=False)
        else:
            mesg = ["No Data Found"]
            return JsonResponse(mesg, safe=False)


def search_url(request):
    if request.method == "GET":
        search_url = request.GET.get("myInput")
        if search_url in url_dict.keys():
            view_name = url_dict[search_url]
            return redirect('/agent/%s' % view_name)


# agent login
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
            pAddr=showPermanentAddressMethod()
            tAddr = showTemporaryAddressMethod()
            request.session["id"] = agent_Obj.id
            request.session["firstName"] = agent_Obj.firstName
            request.session["lastName"] = agent_Obj.lastName
            request.session["usertype"] = agent_Obj.usertype
            last_login = getLastLoginTime(request.session["id"])
            saveLoginTime(agent_Obj.id)
            # addrObj=Address.objects.filter(agent_id=request.session["id"])
            addressForm = AddressForm()

            return render(request, 'agentDetails.html', {"agentProfile": agent_Obj, "pAddr": pAddr, "tAddr": tAddr,
                                                         "AddressForm": addressForm,"last_login": last_login,"myProfile":"active"})

        except ServiceException as ex:
            return render(request, "agentLogin.html", {"msg": ex.errorMessage})


# Registration of agent by supervisor only
def handleAgent(request):
    last_login = getLastLoginTime(request.session["id"])
    if request.method == "GET":
        form = AgentForm()
        addressForm = AddressForm()
        return render(request, 'agentRegistration.html',
                      {'form': form, "AddressForm": addressForm, "last_login": last_login})
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
    form = AgentForm(request.POST, request.FILES)
    try:
        createAgent_Obj=createEmployeeValidation(request, email, username,form)
        if createAgent_Obj:
            return render(request, 'agentRegistration.html',
                          {'form': form, 'message': 'success', "last_login": last_login})
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
            return render(request, "showAgents.html",
                          {"show_agent_obj": show_agent_obj, "page_obj": page_obj,"last_login": last_login})


# Search agent details by using Id or username
def searchByAgent(request):
    usertype = request.session["usertype"]
    last_login = getLastLoginTime(request.session["id"])
    if request.method == "GET":
        form = AgentForm()
        return render(request, "searchAgent.html", {"form": form,"last_login": last_login,"search":"active"})
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            form = AgentForm(request.POST, request.FILES)
            search_by_name = getDetailsByName(username)
            if search_by_name:
                return render(request, "searchAgent.html",
                              {"search_by_name": search_by_name,"form": form,
                               "last_login": last_login,"search":"active"})
        except:
            return render(request, "searchAgent.html",
                          {"usertype": usertype, "form": form, "msg": "No data Found","search":"active"})
def advSearchByAgent(request):
    usertype = request.session["usertype"]
    if 'firstName' in request.GET:
        firstName = request.GET["firstName"]
    if 'lastName' in request.GET:
        lastName = request.GET["lastName"]
    if 'username' in request.GET:
        username = request.GET["username"]
    # adv_search_obj = AgentTable.objects.filter(Q(firstName=firstName) | Q(lastName=lastName) | Q(username=username))
    adv_search_obj = advancedSearchMethod(firstName, lastName, username)
    paginator = Paginator(adv_search_obj, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    GET_params = request.GET.copy()

    if adv_search_obj:
        last_login = getLastLoginTime(request.session["id"])
        return render(request, "searchAgent.html",
                      {"adv_search_obj": adv_search_obj,'page_obj': page_obj,
                       'GET_params': GET_params, "last_login": last_login,"advancedSearch":"active"})

    else:
        return render(request, "searchAgent.html", {"usertype": usertype,"advSearchMsg":"No Data Found","advancedSearch":"active"})


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
    # saveLogoutTime(sessionId)
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
            return render(request, 'agentDetails.html',
                          {"agentProfile": image_uploadObj, "last_login": last_login})


# Navigate to  Agent details page when we click on myprofile
def agentDetails(request):
    usertype = request.session["usertype"]
    if request.method == 'GET':
        myId = request.session['id']
        agent_detail_obj = getLoggedInUserObject(myId)
        last_login = getLastLoginTime(request.session["id"])
        addressForm = AddressForm()
        pAddr = AddressTable.objects.get(AddressType="PermanentAddress")
        tAddr = AddressTable.objects.get(AddressType="TemporaryAddress")
        if pAddr and tAddr:
            return render(request, 'agentDetails.html',
                          {"agentProfile": agent_detail_obj, "pAddr": pAddr, "tAddr": tAddr, "AddressForm": addressForm,
                           "last_login": last_login,"myProfile":"active"})


# Editing profile of agent when agent login only
def editProfile(request):
    myId = request.session['id']
    edit_obj = getLoggedInUserObject(myId)
    usertype=request.session["usertype"]
    pAddr = AddressTable.objects.get(AddressType="PermanentAddress")
    tAddr = AddressTable.objects.get(AddressType="TemporaryAddress")
    if request.method == 'GET':
        return render(request, 'editProfile.html', {"agentProfile": edit_obj})
    if request.method == 'POST':
        myId = request.session['id']
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        last_login = getLastLoginTime(request.session["id"])
        try:
            agent_detail_obj = editLoggedInAgentProfile(request, firstName, lastName, email, myId)
            if agent_detail_obj:
                return render(request, 'agentDetails.html',
                              {"agentProfile": agent_detail_obj,"pAddr": pAddr,"tAddr": tAddr,"last_login": last_login,"updateProfile":"active"})
        except ServiceException as ex:
            return render(request, 'agentDetails.html', {"agentProfile":edit_obj,"pAddr": pAddr,"tAddr": tAddr,"last_login": last_login,"usertype":usertype,"updateProfile":"active","errorMsg": ex.errorMessage})


# Changing password of agent when by agent only
def changePassword(request):
    last_login = getLastLoginTime(request.session["id"])
    pAddr = AddressTable.objects.get(AddressType="PermanentAddress")
    tAddr = AddressTable.objects.get(AddressType="TemporaryAddress")
    usertype=request.session["usertype"]
    myId=request.session["id"]
    edit_obj = getLoggedInUserObject(myId)
    '''if request.method == 'GET':
        myId = request.session["id"]
        change_obj = getLoggedInUserObject(myId)
        return render(request, 'changePassword.html', {"agentProfile": edit_obj, "last_login": last_login})
'''
    if request.method == 'POST':
        myId = request.session['id']
        oldPassword = request.POST["old-password"]
        newPassword = request.POST["new-password"]

    try:

        change_obj = passwordChangeObject(request, oldPassword, newPassword, myId)

        if (change_obj):
            return render(request, 'agentDetails.html', {"agentProfile": change_obj,"usertype":usertype,"pAddr": pAddr,"tAddr": tAddr, "last_login": last_login,"changePassword":"active"})
    except ServiceException as ex:
        return render(request, 'agentDetails.html', {"agentProfile": edit_obj,"usertype":usertype,"pAddr": pAddr,"tAddr": tAddr,"changeMsg": ex.errorMessage,"last_login": last_login,"changePassword":"active"})


# Department creation by supervisor
def createDepartment(request):
    usertype = request.session["usertype"]
    last_login = getLastLoginTime(request.session["id"])
    if request.method == "GET":
        form = DepartmentForm()
        return render(request, "createDepartment.html", {"form": form, "usertype": usertype, "last_login": last_login})
    if request.method == "POST":
        deptName = request.POST["deptName"]
        createdBy_id = request.session["id"]
        form = DepartmentForm(request.POST, request.FILES)
        try:
            create_deptObj=createDepartmentMethod(deptName,createdBy_id)

            if create_deptObj:
                return render(request, "createDepartment.html",
                              {"form": form, "last_login": last_login, "msg": "Success"})
        except ServiceException as ex:
               return render(request, "createDepartment.html",
                      {"usertype": usertype, "msg":ex.errorMessage})

# Showing all departments by supervisor
def showAllDepartments(request):
    usertype = request.session["usertype"]
    if request.method == "GET":
        show_Dept_Obj = Department.objects.all()
        paginator = Paginator(show_Dept_Obj, 5)  # Show 5 agents per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        last_login = getLastLoginTime(request.session["id"])
        return render(request, "showAllDepartments.html",
                      {"show_Dept_Obj": show_Dept_Obj,"page_obj": page_obj,
                       "last_login": last_login})


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
            return render(request, "showRequest.html",
                          {"show_req_obj": show_req_obj, "last_login": last_login})
        else:
            return render(request, "showRequest.html",
                          {"last_login": last_login, "message": "no data found"})

def unlockRequest(request, requestedBy):
    # requestedBy = request.POST.get('requestedBy')
    try:
        unlock_obj=unlockRequestMethod(requestedBy)
        #count_obj = AgentTable.objects.get(username=requestedBy)
        if unlock_obj:
           return render(request, "showRequest.html", {"message": "unlock success"})
    except ServiceException as ex:
           return render(request, "showRequest.html", {"message": ex.errorMessage})

def imageData(request, id):
    image_details = getAgentDetailsImageClick(id)
    last_login = getLastLoginTime(request.session["id"])
    try:
        if image_details:
            return render(request, "showDetailImageClick.html",{"show_image_obj": image_details,"last_login": last_login})

    except:
        return render(request, "showDetailImageClick.html", {"msg": "No details Found"})


def deptData(request, dept):
    deptDetails = getDepartmentDetails(dept)
    last_login = getLastLoginTime(request.session["id"])
    try:
        if deptDetails:
            return render(request, "showDeptDetailsClick.html",
                          {"deptDetails": deptDetails,"last_login": last_login})
    except:
        return render(request, "showDeptDetailsClick.html", {"msg": "No details Found"})


def searchByDepartment(request):
    last_login = getLastLoginTime(request.session["id"])
    if request.method == 'GET':
        form = DepartmentForm()
        return render(request, "searchDepartment.html", {'form': form,"last_login":last_login})
    if request.method == "POST":
        department = request.POST["department"]
        form = DepartmentForm(request.POST)
        try:
            search_by_department = getdetailsbyDepartment(department)
            if search_by_department:
                return render(request, "searchDepartment.html",
                              {"search_by_department": search_by_department,'form': form})
        except:
            return render(request, "searchDepartment.html",{"form": form, "msg": "No details found"})


def createAddress(request):
    last_login = getLastLoginTime(request.session["id"])
    addressForm = AddressForm()
    form = AgentForm()
    if request.method == "GET":
        return render(request, 'agentRegistration.html',{"form": form, 'AddressForm': addressForm, "last_login": last_login})
    if request.method == 'POST':
        addressForm = AddressForm(request.POST,request.FILES)
        Dno = request.POST["Dno"]
        Street = request.POST["Street"]
        City = request.POST["City"]
        State = request.POST["State"]
        Pincode = request.POST["Pincode"]
        Agent = request.session["id"]
        Agent_id = Agent
        AddressType = request.POST["AddressType"]
        create_addr_obj=createAddressMethod(Dno,Street,City,State,Pincode,Agent_id,AddressType)
        """AddressTable.objects.create(Dno=Dno, Street=Street, City=City, State=State, Pincode=Pincode, Agent_id=Agent_id,
                                    AddressType=AddressType)"""
        if create_addr_obj:
            return render(request, 'agentRegistration.html', {"form": form, 'pAddressForm': addressForm,
                                                          "last_login": last_login,
                                                          "addressMsg": " address inserted"})
def pAddressUpdate(request):
    if request.method == "POST":
       addressType=request.POST["AddrType"]
       doorNo=request.POST["DoorNo"]
       street=request.POST["Street"]
       city=request.POST["City"]
       state=request.POST["State"]
       pincode=request.POST["Pincode"]
       if addressType == "PermanentAddress":
            pAddr=AddressTable.objects.filter(Q(Agent_id=request.session["id"] ) & Q(AddressType="PermanentAddress")).update(Dno=doorNo,Street=street,City=city,State=state,Pincode=pincode)
            return render(request,"agentDetails.html",{"pAddr":pAddr})
       if addressType == "TemporaryAddress":
           tAddr = AddressTable.objects.filter(Q(Agent_id=request.session["id"]) & Q(AddressType="TemporaryAddress")).update(Dno=doorNo, Street=street,City=city, State=state,Pincode=pincode)
           return render(request, "agentDetails.html", {"tAddr": tAddr})
