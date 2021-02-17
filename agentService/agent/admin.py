from django.contrib import admin

# Register your models here.
from .models import AgentTable,Requests,Department,LogTable,AddressTable

class MyAgentadmin(admin.ModelAdmin):
   	list_display = ('id','firstName', 'lastName', 'username','password', 'dept','created_date','usertype')
admin.site.register(AgentTable, MyAgentadmin)

class MyDepartmentadmin(admin.ModelAdmin):
   	list_display = ('deptName', 'createdBy', 'created_date')
admin.site.register(Department, MyDepartmentadmin)

"""""class MyRequestadmin(admin.ModelAdmin):
   	list_display = ('requestedBy', 'requestedDate', 'approvedBy','approvedDate','status','description','requestType')
admin.site.register(Request, MyRequestadmin)
"""""
class MyRequestsadmin(admin.ModelAdmin):
   	list_display = ('requestedUserName','requestedBy', 'requestedDate', 'approvedBy','approvedDate','status','description','requestType')
admin.site.register(Requests, MyRequestsadmin)

class MylogTableadmin(admin.ModelAdmin):
   	list_display = ('id','loginTime', 'logoutTime', 'sessionId')
admin.site.register(LogTable, MylogTableadmin)

'''class MyAddressadmin(admin.ModelAdmin):
	list_display = ("dno","street","city","state","pincode","address_type")
admin.site.register(PermanentAddress,MyAddressadmin)'''

class MyAddressadmin(admin.ModelAdmin):
	list_display = ("Dno","Street","City","State","Pincode","AddressType")
admin.site.register(AddressTable,MyAddressadmin)

