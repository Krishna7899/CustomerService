from django.forms import ModelForm
from .models import AgentTable, Requests, Department,PermanentAddress,TemporaryAddress
from django import forms


from django.core.exceptions import NON_FIELD_ERRORS


# ModelForm class
OPTIONS = (("agent", "agent"), ("supervisor", "supervisor"))
class AgentForm(forms.ModelForm):

    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'firstName','id': 'firstName'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'lastName','id': 'lastName'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'email', 'id': 'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username','id': 'username' ,'placeholder': ''}))
    password = forms.CharField(widget=forms.PasswordInput (attrs={'class': 'password', 'id': 'password'}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'confirmPassword', 'id': 'confirmPassword'}))
    dept=forms.ModelChoiceField(queryset=Department.objects.all(), initial=0,widget=forms.Select(attrs={'class':'dept-select'}))
    usertype=forms.ChoiceField(choices=OPTIONS,widget=forms.Select(attrs={'class':'usertype-select'}))
    # specify the name of model to use
    class Meta:
        model = AgentTable
        fields = ["firstName", "lastName", "email","username","password","confirmPassword","dept","usertype"]

class ImageForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class DepartmentForm(forms.ModelForm):

    deptName= forms.CharField(widget=forms.TextInput
    (attrs={'class': 'deptName','id': 'deptName'}))
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
class PaddressForm(forms.ModelForm):
    pDno = forms.CharField(widget=forms.TextInput(attrs={'class': 'dno', 'id':'dno'}))
    pStreet = forms.CharField(widget=forms.TextInput(attrs={'class': 'street', 'id': 'street'}))
    pCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'city', 'id': ' city'}))
    pState = forms.CharField(widget=forms.TextInput(attrs={'class': 'state', 'id': 'state'}))
    pPincode = forms.CharField(widget=forms.TextInput(attrs={'class': 'pincode', 'id': 'pincode'}))

    class Meta:
        model=PermanentAddress
        fields=["pDno","pStreet","pCity","pState","pPincode","pAddressType"]


class TaddressForm(forms.ModelForm):
    tDno = forms.CharField(widget=forms.TextInput(attrs={'class': 'dno', 'id': 'dno'}))
    tStreet = forms.CharField(widget=forms.TextInput(attrs={'class': 'street', 'id': 'street'}))
    tCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'city', 'id': ' city'}))
    tState = forms.CharField(widget=forms.TextInput(attrs={'class': 'state', 'id': 'state'}))
    tPincode = forms.CharField(widget=forms.TextInput(attrs={'class': 'pincode', 'id': 'pincode'}))

    class Meta:
        model =TemporaryAddress
        fields = ["tDno", "tStreet", "tCity", "tState", "tPincode", "tAddressType"]