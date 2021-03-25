from django.forms import ModelForm
from .models import AgentTable, Requests, Department, MyAddressTable, Partner, Branch
from django import forms


from django.core.exceptions import NON_FIELD_ERRORS


# ModelForm class
OPTIONS = (("agent", "agent"), ("supervisor", "supervisor"),("sales manager","sales manager"))
class AgentForm(forms.ModelForm):

    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'firstName','id': 'firstName'}),required=True)
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'lastName','id': 'lastName'}),required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'email', 'id': 'email'}),required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username','id': 'username' ,'placeholder': ''}),required=True)
    password = forms.CharField(widget=forms.PasswordInput (attrs={'class': 'password', 'id': 'password'}),required=True)
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'confirmPassword', 'id': 'confirmPassword'}),required=True)
    dept=forms.ModelChoiceField(queryset=Department.objects.all(), initial=0,widget=forms.Select(attrs={'class':'dept-select'}),required=True)
    usertype=forms.ChoiceField(choices=OPTIONS,widget=forms.Select(attrs={'class':'usertype-select'}),required=True)
    # specify the name of model to use
    class Meta:
        model = AgentTable
        fields = ["firstName", "lastName", "email","username","password","confirmPassword","dept","usertype"]

class ImageForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class DepartmentForm(forms.ModelForm):

    deptName= forms.CharField(widget=forms.TextInput(attrs={'class': 'deptName','id': 'deptName'}))
    class Meta:
        model=Department
        fields=["deptName"]


class RequestsForm(forms.ModelForm):
    requestedUserName = forms.CharField(widget=forms.TextInput(attrs={'class': 'requestedUserName', 'id': 'requestedUserName'}))
    description = forms.CharField(widget=forms.Textarea
        (attrs={'class': 'description','id': 'description'}))

    OPTIONS = [('IT','IT'),('Recruitment','Recruitment'),('Finance','Finance')]
    requestType  = forms.ChoiceField(required=True, choices=OPTIONS,widget=forms.Select
        (attrs={'class': 'requestType','id': 'requestType'}))
    class Meta:
        model = Requests
        fields = ["requestedUserName","description", "requestType"]
class AddressForm(forms.ModelForm):
    Dno = forms.CharField(widget=forms.TextInput(attrs={'class': 'dno', 'id':'dno'}))
    Street = forms.CharField(widget=forms.TextInput(attrs={'class': 'street', 'id': 'street'}))
    City = forms.CharField(widget=forms.TextInput(attrs={'class': 'city', 'id': ' city'}))
    State = forms.CharField(widget=forms.TextInput(attrs={'class': 'state', 'id': 'state'}))
    Pincode = forms.CharField(widget=forms.TextInput(attrs={'class': 'pincode', 'id': 'pincode'}))

    class Meta:
        model=MyAddressTable
        fields=["Dno","Street","City","State","Pincode","AddressType","agent_id","partner_id","branch_id"]

class PartnerForm(forms.ModelForm):
    class Meta:
        model=Partner
        fields = ["name", "code", "GSTCode"]

class BranchForm(forms.ModelForm):
    class Meta:
        model=Branch
        fields=["BranchName","BranchCode","GSTid","igst","cgst"]