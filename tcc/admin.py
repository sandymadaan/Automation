"""
%% admin.py %%

This file display usage information that admin requires to edit or add
in database tables, classes, forms and mappers in admin interface. This
make the data entry easy as one need to do it through MySQL server.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::::::::::::#
from django.contrib import admin
from Automation.tcc.models import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE ADMIN CLASSES HERE:::::::::::::::::::::::::::#

class JobAdmin(admin.ModelAdmin):
    	"""
	** JobAdmin **
	
	Job Admin is required to add, edit or delete the content into the Job model directly. The list to be displayed after adding and search 		and list filter	are also there.
	"""

	list_display = ('job_no', 'client','site' )
	search_fields = ('job_no',)
	list_filter = ['job_no']

class ClientAdmin(admin.ModelAdmin):
	"""
	** ClientAdmin **
	
	Client Admin is used to add, edit or delete the client and its inforamtion directly by the admin.
	"""

	list_display = ('id', 'name','address_1','address_2','state','city' )
	search_fields = ('name','city')
	list_filter = ['name']

class LabAdmin(admin.ModelAdmin):
	"""
	** LabAdmin **
	
	Lab Admin is used to add, edit or delete the Labs and there inforamtion directly by the admin.
	"""

	list_display = ( 'name', )
	search_fields = ('name',)
	list_filter = ['name']

class DistributionAdmin(admin.ModelAdmin):
	"""
	** DistributionAdmin **
	
	DistributionAdmin is used to add, edit or delete the various distributions and there inforamtion directly by the admin.
	"""

	list_display = ( 'name', )
	search_fields = ('name',)
	list_filter = ['name']

class GovtAdmin(admin.ModelAdmin):
	"""
	** GovtAdmin **
	
	Govt Admin is used to add, edit or delete the organisation or work type(like Government, Semi-Government or Private) directly by the admin.
	"""

	list_display = ('id', 'name' )
	search_fields = ('name',)
	list_filter = ['name']

class ReportAdmin(admin.ModelAdmin):
	"""
	** ReportAdmin **
	
	Report Admin is used to add, edit or delete the type of work(like Lab or Field work) directly by the admin.
	"""

	list_display = ('id', 'name' )
	search_fields = ('name',)
	list_filter = ['name']

class PaymentAdmin(admin.ModelAdmin):
	"""
	** PaymentAdmin **
	
	Payment Admin is used to add or edit or delete the different modes of payment like Cash, Cheque, Online or Demand Draft directly by 		the admin.
	"""

	list_display = ('id', 'name' )
	search_fields = ('name',)
	list_filter = ['name']


class MaterialAdmin(admin.ModelAdmin):
	"""
	** MaterialAdmin **
	
	Material Admin is used to add, edit or delete the different materials to be tested in differnt labs and there inforamtion directly by 		the admin.
	"""

	list_display = ('lab', 'name','report' )
	search_fields = ('name',)
	list_filter = ['name']

class TestAdmin(admin.ModelAdmin):
	"""
	** TestAdmin **
	
	Test Admin is used to add, edit or delete the tests performed on the material and there inforamtion directly by the admin.
	"""

	list_display = ('material', 'name','quantity','unit','cost' )
	search_fields = ('name',)
	list_filter = ['name']

class OrganisationAdmin(admin.ModelAdmin):
	"""
	** OrganisationAdmin **
	
	Organisation Admin is used to add, edit or delete the organisation and its information directly by the admin.
	"""
	list_display = ('name','address', 'phone','director')
	search_fields = ('name',)
	list_filter = ['name']

class DepartmentAdmin(admin.ModelAdmin):
	"""
	** DepartmentAdmin **
	
	Department Admin is used to add, edit or delete the different departments in the organisation and there inforamtion directly by the 		admin.
	"""
	list_display = ('organisation','name','address', 'phone','dean','faxno')
	search_fields = ('name',)
	list_filter = ['name']

class StaffAdmin(admin.ModelAdmin):
	"""
	** StaffAdmin **
	
	Staff Admin is used to add, edit or delete the staff members of particular lab and there inforamtion directly by the admin.
	"""

	list_display = ('department','code', 'name','daily_income','position','lab')
	search_fields = ('code',)
	list_filter = ['code']

class TransportationAdmin(admin.ModelAdmin):
	"""
	** TransportationAdmin **
	
	Transportation Admin is used to add, edit or delete the transportation inforamtion directly by the admin.
	"""

	list_display = ('vehicleno','rate')
	search_fields = ('vehicleno',)
	list_filter = ['vehicleno']

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Lab, LabAdmin)
admin.site.register(Govt, GovtAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Distribution, DistributionAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Transportation, TransportationAdmin)
