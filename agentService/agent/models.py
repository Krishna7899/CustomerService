from django import forms
from django.db import models
from django.utils import timezone

# Create your models here.
# Model class

class AgentTable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=8, default="")
    lastName = models.CharField(max_length=30)
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    dept = models.CharField(max_length=30, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=20, unique=True, default="", null=False)
    image = models.ImageField(blank=True, null=True, default='0')
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=30, null=True)
    #confirmPassword = models.CharField(max_length=20, null=False, default='')
    count = models.IntegerField(blank=True, default=0)
    usertype = models.CharField(max_length=30,default='')

    def __str__(self):
        return self.username


class Department(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)

    deptName = models.CharField(max_length=30, null=True)
    createdBy = models.ForeignKey(AgentTable, on_delete=models.CASCADE, default='')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.deptName


"""class Request(models.Model):
    requestedBy=models.ForeignKey(AgentTable,on_delete=models.CASCADE)
    requestedDate=models.DateTimeField(default=timezone.now)
    approvedBy=models.CharField(max_length=30,default='',null=True)
    approvedDate=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=30,null=True)
    description=models.CharField(max_length=200,null=True)
    requestType=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.requestedBy"""


class Requests(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    requestedUserName = models.CharField(max_length=30, null=True)
    requestedBy = models.ForeignKey(AgentTable,null=True, blank=True, on_delete=models.CASCADE)
    requestedDate = models.DateTimeField(default=timezone.now)
    approvedBy = models.CharField(max_length=30, default='', null=True)
    approvedDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=200, null=True)
    requestType = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.requestedBy

class LogTable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    loginTime=models.DateTimeField()
    logoutTime=models.DateTimeField(null=True)
    sessionId=models.IntegerField(default='')
    agentId=models.IntegerField(default=0)
    def __str__(self):
        return self.loginTime
