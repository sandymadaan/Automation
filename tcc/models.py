"""
%% models.py %%
This file contains all the defination for models of Automation software. 
including tables, classes, forms and mappers.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE:::::::::::::::::::::::::::::#
from django.db import models
from django.forms import ModelForm, TextInput, ModelChoiceField
from django import forms
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Max ,Q, Sum
import datetime
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from tagging.fields import TagField
from tagging.models import Tag
from Automation.tcc.choices import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#::::::::::::::::::::::DEFINE THE MODELS HERE:::::::::::::::::::::::::::#
class Report(models.Model):
	"""
	** Report **

	Report Class to reterive any Report Information,
	when we fill Job Number and type of Report Store in Database

	"""

	name = models.CharField(max_length=50)

	def __unicode__(self):
        	return self.name

class UserProfile(models.Model):
	"""
	** UserProfile **
	
	UserProfile Class define all field required to submit detail about new Client.

	""" 
    # This field is required.
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100,blank=True, null=True)
	last_name = models.CharField(max_length=100,blank=True, null=True)
	address = models.CharField(max_length=255)
	company = models.CharField(max_length=255,blank=True, null=True)
	city = models.CharField(max_length=255)
	pin_code = models.IntegerField(null=True)
	state = models.CharField(max_length=30,choices=STATES_CHOICES,default='Punjab')
	website = models.URLField(blank=True, null=True)
	email_address = models.EmailField(blank=True, null=True)
	contact_no = models.CharField(max_length=25)
	type_of_organisation = models.CharField(max_length=20, choices = 
	ORGANISATION_CHOICES)

	def __unicode__(self):
        	return self.first_name


class UserProfileForm(ModelForm):
	"""
	** UserProfileForm **
	
	UserProfileForm Class define the form for UserProfile model.
	
	""" 
	class Meta :
		model = UserProfile
		exclude= ['user']
		widgets = {
		'first_name' : TextInput(attrs={'size':60}),
		'middle_name' : TextInput(attrs={'size':60}),
		'last_name' : TextInput(attrs={'size':60}),
		'address' : TextInput(attrs={'size':60}),
		'company' : TextInput(attrs={'size':60}),
		'city' : TextInput(attrs={'size':60}),
		'pin_code' : TextInput(attrs={'size':60}),
		'website' : TextInput(attrs={'size':60}),
		'email_address' : TextInput(attrs={'size':60}),
		'contact_no' : TextInput(attrs={'size':60}),
                  }
	
class Organisation(models.Model):
	"""
	** Organisation **
	
	Organisation Class define all fields required to submit detail about 
	Organisation.
	
	""" 
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=20)
	director = models.CharField(max_length=50) 
	status = models.CharField(max_length=5000)
	logo_upload = models.ImageField(upload_to='logo')

	def __unicode__(self):
        	return self.name

class Department(models.Model):
	"""
	** Department **
	
	Department Class define all fields required to submit detail about a 
	department for a particular Organisation.
	
	""" 
	organisation = models.ForeignKey(Organisation)
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=20, blank=True)
	dean = models.CharField(max_length=50, blank=True)
	faxno = models.CharField(max_length=100, blank=True)
	email_1 = models.CharField(max_length=75,blank=True)
	email_2 = models.CharField(max_length=75,blank=True)
	url = models.CharField(max_length=50,blank=True)
	about = models.CharField(max_length=150,blank=True)

	def __unicode__(self):
        	return self.name


class Distribution(models.Model):
	"""
	** Distribution **
	
	Distribution Class define all didtribution of income that is to be done.
	
	"""
	name = models.CharField(max_length=100)

	def __unicode__(self):
        	return self.name

 
class Lab(models.Model):
	"""
	** Lab **
	
	Lab Class define all fields required to submit detail about a LAB of a 
	Department.
	
	""" 
	name = models.CharField(max_length=300)
	department = models.ForeignKey(Department)
	tags = TagField()

	def __unicode__(self):
        	return self.name

	def get_tags(self):
        	return Tag.objects.get_for_object(self) 


class Material(models.Model):
	"""
	** Material **
	
	Material Class define all fields required to submit detail about a Material un
	der a Lab.
	
	""" 
	lab = models.ForeignKey(Lab)
	distribution = models.ForeignKey(Distribution)
	name = models.CharField(max_length=300)
	tags = TagField()
	report = models.ForeignKey(Report)
	image = models.ImageField(upload_to='logo')

	def __unicode__(self):
        	return self.name

	def get_tags(self):
        	return Tag.objects.get_for_object(self) 


class Test(models.Model):
	"""
	** Test **
	
	Test Class define all fields required to submit detail about a test under a 
	Material.
	
	""" 
	material = models.ForeignKey(Material)
	name = models.CharField(max_length=300)
	quantity = models.IntegerField(blank=True, null=True)
	unit = models.CharField(max_length=15)
	cost = models.IntegerField(blank=True, null=True)
	tags = TagField()

	def __unicode__(self):
        	return self.name
	
	def get_tags(self):
        	return Tag.objects.get_for_object(self) 

class Clientadd(models.Model):
	"""
	** Clientadd **
	
	Clientadd Class define that which user for which client is adding the jobid.
	
	""" 
	user = models.ForeignKey(User)
	client = models.ForeignKey(UserProfile)
	
	
class editClientadd(models.Model):
	"""
	** editClientadd **
	
	editClientadd Class define that which user for which client is adding the 
	performa jobid.
	
	""" 
	user = models.ForeignKey(User)
	client = models.ForeignKey(UserProfile)


class Govt(models.Model):
	"""
	** Govt **
	
	Govt Class define all fields required to submit detail about a organisation 
	Type (Government, Semi-Government or Private).
	
	""" 
	name =	models.CharField(max_length=600, blank=True )

	def __unicode__(self):
        	return self.name


class Payment(models.Model):
	"""
	** Payment **
	
	Payment Class define all fields required to submit detail about Payment 
	type (Cash, Cheque, Online or DD).
	
	""" 
	name = models.CharField(max_length = 50,blank =True)

	def __unicode__(self):
        	return self.name


class Job(models.Model):
	"""
	**Job**
	
	Job Class is define all field required to submit detail about new Job.
	
	""" 
	client = models.ForeignKey(Clientadd)
	job_no = models.IntegerField(editable =False)
	sample = models.IntegerField()
	ip = models.CharField(max_length=50)
	site = models.CharField(max_length=50)
	type_of_work = models.ForeignKey(Govt)
	report_type = models.ForeignKey(Report)
	pay = models.CharField(max_length=600)
	check_number = models.CharField(max_length=15,blank=True)
	check_dd_date = models.CharField(blank=True, max_length=15)
	date = models.DateField(auto_now_add=True)
	letter_no = models.CharField(max_length=15,blank=True)
	letter_date = models.DateField( blank=True, null=True)
	tds = models.IntegerField(default="0")

	def __unicode__(self):
          return self.id()


class EditJob(models.Model):
	"""
	**EditJob**
	
	EditJob Class is define all field required to submit detail about new 
	performa Job.
	
	""" 
	client = models.ForeignKey(editClientadd)
	job_no = models.IntegerField(editable =False)
	sample = models.CharField(max_length=11)
	ip = models.CharField(max_length=50)
	site = models.CharField(max_length=600)
	type_of_work = models.ForeignKey(Govt)
	report_type = models.ForeignKey(Report)
	pay = models.CharField(max_length=600, blank=True )
	date = models.DateField(auto_now_add=True)
	check_number = models.CharField(max_length=15,blank=True)
	check_dd_date = models.CharField(blank=True, max_length=15)
	letter_no = models.IntegerField(blank=True,null=True)
	letter_date = models.DateField( blank=True, null=True)
	tds = models.IntegerField(default="0")

	def __unicode__(self):
          return self.id()


class JobForm(forms.ModelForm):
	"""
	** JobForm **
	
	JobForm Class define form for Job model.
	
	""" 
	class Meta :
		model = Job
		exclude= ['client','job_no','report_type','date','ip']
        
        
class editJobForm(forms.ModelForm):
	"""
	** editJobForm **
	
	editJobForm Class define form for editJob model.
	
	""" 
	class Meta :
		model = EditJob
		exclude= ['client','job_no','report_type','date','ip'] 
	
	
class ClientJob(models.Model):
	"""
	** ClientJob **
	
	ClientJob Class define the materials and tests performed on a clientjob.
	
	""" 
	job = models.ForeignKey(Job)
	material = models.ForeignKey(Material)
	other_test = models.CharField(max_length=400, blank=True )
	test = models.ManyToManyField(Test, blank=True)
	
	def __unicode__(self):
          return self.id()


class ClientJobForm(forms.ModelForm):
	"""
	** ClientJobForm **
	
	ClientJobForm Class define the form for ClientJob model.
	
	""" 
	class Meta :
		model = ClientJob
		exclude= ['job','material']


class ClientEditJob(models.Model):
	"""
	** ClientEditJob **
	
	ClientEditJob Class define the materials and tests performed on a performa 
	clientjob.
	
	""" 
	job = models.ForeignKey(EditJob)
	material = models.ForeignKey(Material)
	test = models.ManyToManyField(Test)
	
	def __unicode__(self):
          return self.id()
	

class ClientjobForm(forms.ModelForm):
	"""
	** Test **
	
	Test Class define all fields required to submit detail about a test under a 
	Material.
	
	""" 
	test = forms.ModelMultipleChoiceField(queryset=Test.objects.all(), required=False, 
	widget=forms.CheckboxSelectMultiple)

	class Meta :
		model = ClientJob
		exclude= ['job']

	def __init__(self,*args, **kwargs):
		super(ClientjobForm,self).__init__(*args,**kwargs)
		try:
			material = kwargs['instance'].material
		except KeyError:
			material = 1 	
		self.fields['test'].queryset=Test.objects.filter(material_id = material)


class editClientJobForm(forms.ModelForm):
	"""
	** editClientJobForm **
	
	editClientJobForm Class define form for editClientJob model.
	
	""" 
	class Meta :
		model = ClientEditJob
		exclude= ['job','material']
	

class SuspenceJob(models.Model):
	"""
	**SuspenceJob**
	
	SuspenceJob Class is used to define all fields required to submit detail about 
	new Suspence Job.
	
	""" 
	job = models.ForeignKey(Job)
	field = models.ForeignKey(Material)
	test = models.ForeignKey(Test)
	other = models.CharField(max_length=600, blank=True )
	
	def __unicode__(self):
          return self.id()


class SuspenceEditJob(models.Model):
	"""
	**SuspenceEditJob**
	
	SuspenceJob Class is used to define all fields required to submit detail 
	about new performa Suspence Job.
	
	""" 
	job = models.ForeignKey(EditJob)
	field = models.ForeignKey(Material)
	test = models.ForeignKey(Test)
	other = models.CharField(max_length=600, blank=True )
	
	def __unicode__(self):
          return self.id()


class SuspenceJobForm(forms.ModelForm):
	"""
	** SuspenceJobForm **
	
	SuspenceJobForm Class define the form for SuspenceJob model.
	
	""" 
	class Meta :
		model = SuspenceJob
		exclude= ['job','field','test']


class editSuspenceJobForm(forms.ModelForm):
	"""
	** editSuspenceJobForm **
	
	editSuspenceJobForm Class define the form for editSuspenceJob model.
	
	""" 
	class Meta :
		model = SuspenceEditJob
		exclude= ['job','field','test']


class TestTotal(models.Model):
	"""
	** TestTotal **
	
	TestTotal Class define all fields required to submit amount detail about a 
	job_id.
	
	""" 
	job = models.ForeignKey(Job)
	unit_price = models.IntegerField(blank=True,null=True)
		
	def __unicode__(self):
        	return self.id
        	
        	        	
class TestTotalForm(forms.ModelForm):
	"""
	** TestTotalForm **
	
	TestTotalForm Class define the form for TestTotal model.
	
	""" 
	class Meta :
		model = TestTotal
		exclude= ['job','balance']


class TestTotalPerf(models.Model):
	"""
	** TestTotalPerf **
	
	TestTotalPerf Class define all fields required to submit amount detail about 
	a performa job_id.
	
	""" 
	job_no = models.IntegerField(editable =False)
	job = models.ForeignKey(EditJob)
	mat = models.IntegerField(editable =True,null=True)
	unit_price = models.IntegerField(blank=True,null=True)
	balance = models.IntegerField(blank=True,null=True)
	type = models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
        	return self.id


class Bill(models.Model):
	"""
	** Bill **
	
	Bill Class define all fields required to submit detail about a taxes on an 
	amount for a particular job.
	
	""" 
	job_no = models.IntegerField(primary_key=True, editable =False)
	education_tax = models.IntegerField(blank=True,null=True)
	higher_education_tax = models.IntegerField(blank=True,null=True)
	service_tax = models.IntegerField(blank=True,null=True)
	net_total = models.IntegerField(blank=True,null=True)
	price = models.IntegerField(blank=True,null=True)
	trans_total = models.IntegerField(blank=True,null=True)
	trans_net_total = models.IntegerField(blank=True,null=True)
	balance = models.IntegerField(blank=True,null=True)


class BillPerf(models.Model):
	"""
	** BillPerf **
	
	BillPerf Class define all fields required to submit detail about a taxes on 
	an amount for a particular performa job.
	
	""" 
	job_no = models.IntegerField(primary_key=True, editable =False)
	education_tax = models.IntegerField(blank=True,null=True)
	higher_education_tax = models.IntegerField(blank=True,null=True)
	service_tax = models.IntegerField(blank=True,null=True)
	net_total = models.IntegerField(blank=True,null=True)
	price = models.IntegerField(blank=True,null=True)


class Amount(models.Model):
	"""
	** Amount **
	
	Amount Class define all fields required to submit detail about amount and 
	there distribution for a particular Job id.
	
	""" 
	job = models.ForeignKey(Job)
	college_income = models.IntegerField(blank=True, null=True)
	admin_charge = models.IntegerField(blank=True,null=True)
	consultancy_asst = models.IntegerField(blank=True,null=True)
	development_fund = models.IntegerField(blank=True,null=True)
	unit_price = models.IntegerField(blank=True,null=True)
	report_type = models.CharField(max_length=100,blank=True,null=True)
		
        def __unicode__(self):
          return self.id()


class CdfAmount(models.Model):
	"""
	** CdfAmount **
	
	CdfAmount Class define all fields required to submit detail about cdf Amount.
	
	""" 
	job_no = models.IntegerField(primary_key=True, editable =False)
	date = models.DateField(default=datetime.date.today(), editable=False)
	lab = models.CharField(max_length=100)
	total = models.IntegerField()
	field = models.CharField(max_length=10)
	other_field = models.CharField(max_length=100,blank=True,null=True)
	report_type = models.CharField(max_length=20,editable=False)


class Distance(models.Model):
	"""
	** Distance **
	
	Distance Class define all fields required to submit detail about a site and 
	its distance for a prticular Job_id.
	
	""" 
    	job =models.IntegerField(editable =False)
    	sandy = models.DecimalField(max_digits=10, decimal_places=3)


class DistanceForm(ModelForm):
	"""
	** DistanceForm **
	
	DistanceForm Class define form for distance model.
	
	""" 
	class Meta :
		model = Distance
		exclude= ['job']
	
	def __unicode__(self):
        	return self.id



class Suspence(models.Model):
	"""
	** Suspence **
	
	Suspence Class define all fields required to submit detail about a Suspence 
	Job.
	
	""" 
	job = models.ForeignKey(Job)
	rate = models.IntegerField(null=True, blank=True)
	sus = models.ForeignKey(SuspenceJob, blank=True)
	work_charge = models.IntegerField(null=True, blank=True)
	labour_charge = models.IntegerField( blank=True, null=True)
	boring_charge_external = models.IntegerField( blank=True, null=True)
	boring_charge_internal = models.IntegerField( blank=True, null=True)
	car_taxi_charge = models.IntegerField( blank=True, null=True)
	lab_testing_staff = models.CharField( max_length=90,blank=True)
	field_testing_staff =models.CharField( max_length=90,blank=True)
	test_date = models.DateField( blank=True, null=True)
	suspence_bill_no = models.IntegerField( blank=True, null=True)


class SuspenceForm(ModelForm):
	"""
	** SuspenceForm **
	
	SuspenceForm Class define form for Suspence model.
	
	""" 
	class Meta :
		model = Suspence


class Staff(models.Model):
	"""
	** Staff **
	
	Staff Class define all fields required to submit detail about a particular 
	Staff member.
	
	""" 
	department = models.ForeignKey(Department)
	code = models.CharField(max_length=5)
	name = models.CharField(max_length=50)
	daily_income = models.IntegerField(blank=True)
	position = models.CharField(max_length=15)
	lab = models.ForeignKey(Lab)
	email =models.EmailField(blank=True)

	def __unicode__(self):
        	return self.name
	
class ProfromaTax(models.Model):
    pro_no = models.IntegerField(primary_key=True)
    service_tax = models.IntegerField()
    higher_education_tax = models.IntegerField()
    education_tax = models.IntegerField()
    total = models.IntegerField()


class TaDa(models.Model):
	"""
	** TaDa **
	
	TaDa Class define all fields required to submit detail about transport and 
	Daily Allowance for a particular Job id.
	
	""" 
	job = models.ForeignKey(Job)
	departure_time_up = models.TimeField(default = "00:00:00") 
	arrival_time_up = models.TimeField(default = "00:00:00") 
	departure_time_down = models.TimeField(default = "00:00:00")
	arrival_time_down = models.TimeField(default = "00:00:00") 
	tada_amount = models.IntegerField(blank=True, null=True, editable=False)
	reach_site = models.CharField(max_length=60, blank=True)
	test_date = models.CharField(max_length=15)
	end_date = models.CharField(max_length=15)
	testing_staff_code = models.CharField(max_length=50)
	

class TadaForm(ModelForm):
	"""
	** TadaForm **
	
	TadaForm Class define form for Tada model.
	
	""" 
	class Meta :
		model = TaDa
		exclude= ['job']
		widgets = {
             'job' : TextInput(attrs={'size':20}),
             'departure_time_up' : TextInput(attrs={'size':20}),
             'arrival_time_up' : TextInput(attrs={'size':20}),
             'departure_time_down' : TextInput(attrs={'size':20}),
             'arrival_time_down' : TextInput(attrs={'size':20}),
             'tada_amount' : TextInput(attrs={'size':20}),
	     'reach_site' : TextInput(attrs={'size':20}),
	     'test_date' : TextInput(attrs={'size':20}),
	     'end_date' : TextInput(attrs={'size':20}),
	     'testing_staff_code' : TextInput(attrs={'size':20}),
                  }

		
class Transportation(models.Model):
	"""
	** Transportation **
	
	Transportation Class define all fields required to submit detail about 
	transportation.
	
	""" 
	vehicleno = models.CharField(max_length=150)
	rate = models.IntegerField(default='7')

       	def __str__(self):
          return '%s %s' % (self.vehicleno, self.rate)


class Transport(models.Model):
	"""
	** Transport **
	
	Transport Class define all fields required for transportation for a particular 
	job id.
	
	""" 
	vehicle = models.ForeignKey(Transportation)
	id = models.AutoField(primary_key=True)
	job_no = models.IntegerField()
	bill_no = models.IntegerField(null=True, editable=False)
	kilometer = models.CharField(max_length=150, default="00, 00, 00")
	#rate = models.IntegerField(default='4')
	amounts = models.CharField(max_length=180, blank=True,editable=False)
	total = models.IntegerField(blank=True, null=True , editable=False)
	date = models.DateField(default=datetime.date.today())
	test_date = models.CharField(max_length=300, default="0000-00-00, 0000-00-00")


class TransportForm(ModelForm):
	"""
	** TransportForm **
	
	TransportForm Class define form for Transport model.
	
	""" 
	class Meta :
		model = Transport


class Bankdetails(models.Model):
	"""
	** Bankdetails **
	
	Bankdetails Class define all fields required to submit detail about a bank.
	
	""" 
	accname = models.CharField(max_length=50)
	accountno = models.IntegerField(null=False)
	accountcode = models.CharField(max_length=50)
	address = models.CharField(max_length=150)


class BankdetailsForm(ModelForm):
	"""
	** BankdetailsForm **
	
	BankdetailsForm Class define form for Bankdetails model.
	
	""" 
	class Meta :
		model = Bankdetails


class LabReport(forms.Form):
	"""
	** LabReport **

	LabReport Form that displays start and end date and thus helps in retrieving 
	data between this date range for a particular material.

	"""
	start_date= forms.DateField()
	end_date= forms.DateField()
	material = forms.ModelChoiceField(queryset=Material.objects.all())
