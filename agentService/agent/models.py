from django import forms
from django.db import models
from django.utils import timezone

# Create your models here.
# Model class

AddressOptions = (('PermanentAddress', 'PermanentAddress'), ('TemporaryAddress', "TemporaryAddress"))

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

class AddressBase(models.Model):
    Dno = models.CharField(max_length=10,default='')
    Street = models.CharField(max_length=20,default='')
    City = models.CharField(max_length=20,default='')
    State = models.CharField(max_length=20,default='')
    Country=models.CharField(max_length=20,default='')
    Pincode = models.CharField(max_length=6,default='')

    class Meta:
        abstract = True
        ordering = ['Dno','Street','City','State','Country','Pincode']

class Partner(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name =models.CharField(max_length=40,default='')
    code =models.CharField(max_length=40,default='')
    GSTCode = models.CharField(max_length=40,default='')
    IGST = models.CharField(max_length=40, default='', null=True)
    CGST = models.CharField(max_length=40, default='', null=True)
    createdBy = models.ForeignKey(AgentTable, on_delete=models.CASCADE, default='')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Branch(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    BranchName =models.CharField(max_length=40,default='')
    BranchCode =models.CharField(max_length=40,default='')
    GSTid = models.CharField(max_length=40,default='')
    igst = models.CharField(max_length=40, default='', null=True)
    cgst = models.CharField(max_length=40, default='', null=True)
    createdBy = models.ForeignKey(AgentTable, on_delete=models.CASCADE, default='')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.BranchName

class MyAddressTable(AddressBase):
    id = models.AutoField(auto_created=True, primary_key=True)
    agent_id = models.ForeignKey(AgentTable, on_delete=models.CASCADE, default='',blank=True,null=True)
    AddressType = models.CharField(max_length=30, choices=AddressOptions,blank=True,null=True)
    partner_id= models.ForeignKey(Partner,on_delete=models.CASCADE, default='',blank=True,null=True)
    branch_id= models.ForeignKey(Branch, on_delete=models.CASCADE, default='',blank=True,null=True)

    def __str__(self):
        return self.Dno

class InvoiceProduct(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    Description = models.CharField(max_length=40, default='')
    HSNCode = models.CharField(max_length=40, default='', null=True)
    UOM = models.CharField(max_length=40, default='', null=True)
    QtyPerKg = models.CharField(max_length=40, default='')
    RatePerKg = models.CharField(max_length=40, default='')
    TotalQtyCost = models.CharField(max_length=40, default='')
    TotalTax = models.CharField(max_length=40, default='', null=True)

class Invoice(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    invoiceSummary = models.CharField(max_length=200, default='')
    invoiceNumber = models.CharField(max_length=40, default='')
    partner = models.CharField(max_length=40, default='')
    branch = models.CharField(max_length=40, default='')
    created_date = models.DateTimeField(default=timezone.now)
    TransportCharges = models.CharField(max_length=40, default='', null=True)
    TotalTaxAmount = models.CharField(max_length=40, default='', null=True)
    TotalCost = models.CharField(max_length=40, default='', null=True)
    status = models.CharField(max_length=40, default='',null=True)
    invoiceProduct = models.ForeignKey(InvoiceProduct, on_delete=models.CASCADE, default='', blank=True, null=True)



