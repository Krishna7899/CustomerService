from .models import AgentTable, Requests, Department, LogTable
from django.db.models import Q
from .exceptions import ServiceException
import datetime


# Login Validations
def getAgentLoginValidation(request, username, password):
    agent_Obj = AgentTable.objects.filter(Q(username__iexact=username) | Q(email__iexact=username))
    if agent_Obj:
        a = agent_Obj.first()
        if a.password == password:
            if a.count >= 5:
                raise ServiceException('Account Locked')

            if a.count != 0:
                a.count = 0
                a.save()

            return a
        elif a.password != password:
            if a.count >= 5:
                raise ServiceException('Account Locked')
            else:
                a.count = a.count + 1
                a.save()
                raise ServiceException('Invalid Login')
        else:
            raise ServiceException('Invalid Login')
    else:
        raise ServiceException('Invalid Login')


# Save login time
def saveLoginTime(agentId):
    loginTime = datetime.datetime.now().replace(microsecond=0).isoformat(' ')
    loginTime = loginTime.replace(',', '.')
    LogTable.objects.create(loginTime=loginTime, sessionId=agentId, agentId=agentId)


# save logout time
def saveLogoutTime(sessionId):
    logoutTime = datetime.datetime.now().replace(microsecond=0).isoformat(' ')
    logoutTime = logoutTime.replace(',', '.')
    LogTable.objects.filter(sessionId=sessionId).update(logoutTime=logoutTime)


# This method returns last successful login time
def getLastLoginTime(sessionId):
    loginTimeList = []
    log_obj = LogTable.objects.filter(sessionId=sessionId).values_list('loginTime', flat=True)
    if log_obj:
        for last_login_time in log_obj:
            loginTimeList.append(last_login_time)
        loginTimeList.sort(reverse=True)
        if len(loginTimeList) >= 2:
            return loginTimeList[1]
        else:
            return loginTimeList[0]
    else:
        return datetime.datetime.now()


# method to get object of logged in user
def getLoggedInUserObject(myId):
    return AgentTable.objects.get(id=myId)


# Create Agent or supervisor username and email check
def createEmployeeValidation(request, email, username):
    if AgentTable.objects.filter(username=username).exists():
        raise ServiceException('UserName Already Exists')

    if AgentTable.objects.filter(email=email).exists():
        raise ServiceException('Email Already Exists')


# editing logged in user
def editLoggedInAgentProfile(request, firstName, lastName, email, myId):
    if AgentTable.objects.filter(email=email).exists():
        raise ServiceException('Email Already Exists')
    else:
        AgentTable.objects.filter(id=myId).update(firstName=firstName, lastName=lastName, email=email)
        return AgentTable.objects.get(id=myId)


# changing password of agent by agent
def passwordChangeObject(request, oldPassword, newPassword, myId):
    change_obj = AgentTable.objects.get(id=myId)
    if change_obj.password == oldPassword:
        change_obj.password = newPassword
        change_obj.save()
        return change_obj

    else:
        raise ServiceException('Old Password did not exist')


# method to post request for account unlock
def createRequestMethod(requestedBy_id, username, description, requestType):
    Requests.objects.create(requestedBy_id=requestedBy_id, requestedUserName=username, description=description,
                            requestType=requestType)
    return True


# method to get id by using username
def getIdByUserName(username):
    obj = AgentTable.objects.get(username=username)
    myId = obj.id
    return myId


# method to show all requests posted by agents
def showAllRequestsMethod():
    req_obj= Requests.objects.exclude(status="Approved")
    if req_obj:
        return req_obj

# method to show all agents
def showAllAgentsMethod():
    return AgentTable.objects.all()


# method to get details by using username or id
def getDetailsByName(username):
    return AgentTable.objects.get(Q(username__iexact=username) | Q(id__iexact=username))


def advancedSearchMethod(firstName, lastName, username):
    return AgentTable.objects.filter(Q(firstName=firstName) | Q(lastName=lastName) | Q(username=username))


#
# method to get user type by using logged in username to display corresponding profile pages
'''def getUserType(username):
    usertype = AgentTable.objects.get(username=username)
    if usertype.usertype == "agent" or usertype.usertype == '':
        return usertype'''


# Method to get details of agent while clicking on image ,in Agents List
def getAgentDetailsImageClick(id):
    return AgentTable.objects.get(id=id)

def getDepartmentDetails(dept):
    return Department.objects.get(deptName=dept)

def getdetailsbyDepartment(department):
    return Department.objects.get(deptName=department)
