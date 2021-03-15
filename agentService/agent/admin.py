from django.contrib import admin

# Register your models here.

from .models import AgentTable,Requests,Department,LogTable,MyAddressTable,Partner,Branch,Invoice,InvoiceProduct

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
	list_display = ("Dno","Street","City","State","Pincode","AddressType","branch_id","partner_id")

admin.site.register(MyAddressTable, MyAddressadmin)

class MyPartnerAdmin(admin.ModelAdmin):
	list_display = ("id","name","code","GSTCode","IGST","CGST")
admin.site.register(Partner,MyPartnerAdmin)

class MyBranchAdmin(admin.ModelAdmin):
	list_display = ("id","BranchName","BranchCode","GSTid","igst","cgst")
admin.site.register(Branch,MyBranchAdmin)

class MyInvoiceAdmin(admin.ModelAdmin):
	list_display = ("id","invoiceSummary","invoiceNumber","status", "partner", "branch","created_date")
admin.site.register(Invoice,MyInvoiceAdmin)

class MyInvoiceProductAdmin(admin.ModelAdmin):
	list_display = ("Description", "HSNCode", "UOM", "QtyPerKg", "RatePerKg", "TotalQtyCost", "TransportCharges",
					 "TotalTax","TotalCost")
admin.site.register(InvoiceProduct,MyInvoiceProductAdmin)