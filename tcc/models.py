"""
Automation Model Module
 
This contains all of the definitions for the model of the Testing & Consultancy Cell Automation,
including the tables, classes and mappers.
 
"""

from django.db import models
from django.forms import ModelForm, TextInput, ModelChoiceField
import datetime
from django import forms
from Automation.tcc.choices import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Max ,Q, Sum
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from tagging.fields import TagField
from tagging.models import Tag
from django.contrib.sessions.models import Session

class Report(models.Model):
	"""
	Define Client Report Form to reterive any Report Information,
	when we fill Job Number and type of Report Store in Database
	"""
	name = models.CharField(max_length=50)

	def __unicode__(self):
        	return self.name

class UserProfile(models.Model):
    # This field is required.
        user = models.ForeignKey(User)

    # Other fields here
        name = models.CharField(max_length=255)
	address_1 =models.CharField(max_length=255)
	address_2 =models.CharField(max_length=255)
	city =models.CharField(max_length=255)
	pin_code = models.IntegerField(null=False)
	state=models.CharField(max_length=30,choices=STATES_CHOICES,default='Punjab')
	website =models.URLField()
	contact_no =models.CharField(max_length=25)
	type_of_organisation = models.CharField(max_length=20,choices=ORGANISATION_CHOICES)

	def __unicode__(self):
        	return self.name


class UserProfileForm(ModelForm):
	class Meta :
		model = UserProfile
		exclude= ['user']
		widgets = {
             'name' : TextInput(attrs={'size':60}),
             'address_1' : TextInput(attrs={'size':60}),
             'address_2' : TextInput(attrs={'size':60}),
             'city' : TextInput(attrs={'size':60}),
             'pin_code' : TextInput(attrs={'size':60}),
             'website' : TextInput(attrs={'size':60}),
	     'contact_no' : TextInput(attrs={'size':60}),
                  }
	

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        created = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_user_profile, sender=User)
 

class Auto_number(models.Model):
	id = models.AutoField(primary_key=True)
	job_no = models.IntegerField(unique = True)

class Lab(models.Model):
	code = models.CharField(max_length=5)
	name = models.CharField(max_length=300)
	tags = TagField()

	def __unicode__(self):
        	return self.name

	def get_tags(self):
        	return Tag.objects.get_for_object(self) 


class DynamicChoiceField(forms.ChoiceField): 
    def clean(self, value): 
        return value


class Material(models.Model):
	lab = models.ForeignKey(Lab)
	code = models.CharField(max_length=5)
	name = models.CharField(max_length=300)
	tags = TagField()
	report = models.ForeignKey(Report)

	def __unicode__(self):
        	return self.name

	def get_tags(self):
        	return Tag.objects.get_for_object(self) 

class MyForm(forms.Form): 
    material = forms.ModelChoiceField(Material.objects, widget=forms.Select(attrs={'onchange':'FilterTests();'})) 
    test = DynamicChoiceField(widget=forms.Select(attrs={'disabled':'false'}), choices=(('-1','Select Tests'),))

class Test(models.Model):
	#lab = models.ForeignKey(Lab)
	material = models.ForeignKey(Material)
	code = models.CharField(max_length=5)
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
	user = models.ForeignKey(User)
	client = models.ForeignKey(UserProfile)
	
class Govt(models.Model):
	name =	models.CharField(max_length=600, blank=True )

	def __unicode__(self):
        	return self.name

class Payment(models.Model):
	name = models.CharField(max_length = 50,blank =True)

	def __unicode__(self):
        	return self.name

class Job(models.Model):
	"""
	**ClientJob**
	
	ClientJob Class is define all field required to submit detail about new Job.
	
	""" 
        client = models.ForeignKey(Clientadd)
	check_number = models.CharField(max_length=15,blank=True)
	check_dd_date = models.CharField(blank=True, max_length=15)
	job_no = models.IntegerField(editable =False)
	site = models.CharField(max_length=600, blank=True )
	type_of_work = models.ForeignKey(Govt)
	report_type = models.ForeignKey(Report)
	pay = models.CharField(max_length=600, blank=True )
	date = models.DateField(auto_now_add=True)

	def __unicode__(self):
          return self.id()


class JobForm(forms.ModelForm):
	class Meta :
		model = Job
		exclude= ['client','job_no','report_type','date','id']
        
class editJobForm(forms.ModelForm):
	class Meta :
		model = Job
		exclude= ['client','job_no','id'] 

	    
	
class ClientJob(models.Model):
	job = models.ForeignKey(Job)
	material = models.ForeignKey(Material)
	test = models.ManyToManyField(Test)
	
	def __unicode__(self):
          return self.id()
	
	
class ClientJobForm(forms.ModelForm):
	class Meta :
		model = ClientJob
		exclude= ['job','material']

class editClientJobForm(forms.ModelForm):
	test = forms.ModelMultipleChoiceField(queryset=Test.objects.all(), required=False,widget=forms.CheckboxSelectMultiple)

	class Meta :
		model = ClientJob
		exclude= ['job']
	
	def __init__(self,*args, **kwargs):
		super(editClientJobForm,self).__init__(*args,**kwargs)
		try:
            		material = kwargs['instance'].material
       		except KeyError:
           		 material = 1 	
		self.fields['test'].queryset=Test.objects.filter(material_id = material) 


class SuspenceJob(models.Model):
	"""
	**SuspenceJob**
	
	SuspenceJob Class is used to define all fields required to submit detail about new Suspence Job.
	
	""" 
	job = models.ForeignKey(Job)
	field = models.ForeignKey(Material)
	test = models.ForeignKey(Test)
	other = models.CharField(max_length=600, blank=True )
	

	def __unicode__(self):
          return self.id()

class SuspenceJobForm(forms.ModelForm):
	class Meta :
		model = SuspenceJob
		exclude= ['job','field','test']

class editSuspenceJobForm(forms.ModelForm):
	class Meta :
		model = SuspenceJob
		exclude= ['job']


class TestTotal(models.Model):
	job_no = models.IntegerField(editable =False)
	mat = models.IntegerField(editable =True,null=True)
	unit_price = models.IntegerField(blank=True,null=True)
	type = models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
        	return self.id

class TestTotalForm(forms.ModelForm):
	class Meta :
		model = TestTotal

	
	
class Sessiondata(models.Model):
	amt = models.IntegerField(blank=True,null=True)


class TestsForm(ModelForm):

    tests = forms.ModelMultipleChoiceField(queryset=Test.objects.all(), required=False,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ClientJob
	exclude = ('report_type','type_of_consultancy','field','client','date','site','type_of_work','letter_no','letter_date',)

    def __init__(self):
        super(TestsForm, self).__init__()
	id = ClientJob.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	field = Field.objects.all()
	client = ClientJob.objects.values_list('field_id',flat=True).filter(job_no = maxid)
        self.fields['tests'].queryset = Test.objects.filter(field_id = client)


class Bill(models.Model):
	job_no = models.IntegerField(primary_key=True, editable =False)
	education_tax = models.IntegerField(blank=True,null=True)
	higher_education_tax = models.IntegerField(blank=True,null=True)
	service_tax = models.IntegerField(blank=True,null=True)
	net_total = models.IntegerField(blank=True,null=True)
	price = models.IntegerField(blank=True,null=True)

class BillForm(ModelForm):
	class Meta :
		model = Bill

class Amount(models.Model):
	job_no = models.IntegerField(blank=True,null=True)
	college_income = models.IntegerField(blank=True, null=True)
	admin_charge = models.IntegerField(blank=True,null=True)
	consultancy_asst = models.IntegerField(blank=True,null=True)
	development_fund = models.IntegerField(blank=True,null=True)
	unit_price = models.IntegerField(blank=True,null=True)
	report_type = models.CharField(max_length=100,blank=True,null=True)
		
        def __unicode__(self):
          return self.id()



class AmountForm(ModelForm):
	class Meta :
		model = Amount

class CdfAmount(models.Model):
	job_no = models.IntegerField(primary_key=True, editable =False)
	date = models.DateField(default=datetime.date.today(), editable=False)
	lab = models.CharField(max_length=100)
	total = models.IntegerField()
	field = models.CharField(max_length=10)
	other_field = models.CharField(max_length=100,blank=True,null=True)
	report_type = models.CharField(max_length=20,editable=False)

class CdfAmountForm(ModelForm):
	class Meta :
		model = CdfAmount	
	
class Distance(models.Model):
    	job =models.IntegerField(editable =False)
    	sandy = models.DecimalField(max_digits=10, decimal_places=3)

class DistanceForm(ModelForm):
	class Meta :
		model = Distance
		exclude= ['job']
	
	def __unicode__(self):
        	return self.id



class Suspence(models.Model):
	job_no = models.IntegerField(blank=True, null=True)
	rate = models.IntegerField(null=True, blank=True)
	sus = models.ForeignKey(SuspenceJob)
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
	class Meta :
		model = Suspence


class Organisation(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=20)
	director = models.CharField(max_length=50) 
	logo_upload = models.ImageField(upload_to='logo')

	def __unicode__(self):
        	return self.name

class Department(models.Model):
	organisation = models.ForeignKey(Organisation)
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=20)
	dean = models.CharField(max_length=50)
	faxno = models.IntegerField( blank=True, null=True)

	def __unicode__(self):
        	return self.name

class Staff(models.Model):
	department = models.ForeignKey(Department)
	code = models.CharField(max_length=5)
	name = models.CharField(max_length=50)
	daily_income = models.IntegerField(blank=True)
	position = models.CharField(max_length=15)
	lab = models.ForeignKey(Lab)
	email =models.EmailField(blank=True)

	def __unicode__(self):
        	return self.name
	

class Proformabill(models.Model):
	pro_no = models.AutoField(primary_key=True)
	name = models.CharField(max_length=210)
	address = models.CharField(max_length=750)
	charges_for = models.CharField(max_length=450)
	site = models.CharField(max_length=750)
	sample = models.CharField(max_length=270)
	ref_no = models.CharField(max_length=300)
	rate = models.IntegerField()
	amount = models.IntegerField()
	date = models.DateField(default=datetime.date.today())
	transpotation = models.IntegerField()
	labour = models.CharField(max_length=300)


class ProformabillForm(ModelForm):
	class Meta :
		model = Proformabill
                widgets = {
             'name' : TextInput(attrs={'size':60}),
             'address' : TextInput(attrs={'size':60}),
             'charges_for' : TextInput(attrs={'size':60}),
             'site' : TextInput(attrs={'size':60}),
             'sample' : TextInput(attrs={'size':60}),
             'ref_no' : TextInput(attrs={'size':60}),
             'rate' : TextInput(attrs={'size':60}),
             'amount' : TextInput(attrs={'size':60}),
             'date' : TextInput(attrs={'size':60}),
             'transpotation' : TextInput(attrs={'size':60}),
             'labour' : TextInput(attrs={'size':60}),
         }

class ProfromaTax(models.Model):
    pro_no = models.IntegerField(primary_key=True)
    service_tax = models.IntegerField()
    higher_education_tax = models.IntegerField()
    education_tax = models.IntegerField()
    total = models.IntegerField()

class Ta_Da(models.Model):
	"""
	Model of TA/DA Report
	"""
	id = models.AutoField(primary_key=True)
	job_no = models.IntegerField()
	departure_time_up = models.TimeField(default = "00:00:00") 
	arrival_time_up = models.TimeField(default = "00:00:00") 
	departure_time_down = models.TimeField(default = "00:00:00")
	arrival_time_down = models.TimeField(default = "00:00:00") 
	tada_amount = models.IntegerField(blank=True, null=True, editable=False)
	reach_site = models.CharField(max_length=60, blank=True)
	test_date = models.CharField(default='0000-00-00', max_length=15)
	end_date = models.CharField(max_length=15)
	testing_staff_code_1 = models.CharField(max_length=4)
	testing_staff_code_2 = models.CharField(max_length=4, blank=True)
	testing_staff_code_3 = models.CharField(max_length=4, blank=True)
	testing_staff_code_4 = models.CharField(max_length=4, blank=True)
	testing_staff_code_5 = models.CharField(max_length=4, blank=True)
	testing_staff_code_6 = models.CharField(max_length=4, blank=True)
	testing_staff_code_7 = models.CharField(max_length=4, blank=True)
	testing_staff_code_8 = models.CharField(max_length=4, blank=True)
	testing_staff_code_9 = models.CharField(max_length=4, blank=True)
	testing_staff_code_10 = models.CharField(max_length=4, blank=True)

class Ta_DaForm(ModelForm):
	class Meta :
		model = Ta_Da
		widgets = {
            'testing_staff_code_1': TextInput(attrs={'size': 1}),
            'testing_staff_code_2': TextInput(attrs={'size': 1}),
            'testing_staff_code_3': TextInput(attrs={'size': 1}),
            'testing_staff_code_4': TextInput(attrs={'size': 1}),
            'testing_staff_code_5': TextInput(attrs={'size': 1}),
            'testing_staff_code_6': TextInput(attrs={'size': 1}),
            'testing_staff_code_7': TextInput(attrs={'size': 1}),
            'testing_staff_code_8': TextInput(attrs={'size': 1}),
            'testing_staff_code_9': TextInput(attrs={'size': 1}),
            'testing_staff_code_10': TextInput(attrs={'size': 1}),
        }

class Transportation(models.Model):
	vehicleno = models.CharField(max_length=150)
	rate = models.IntegerField(default='7')

       	def __str__(self):
          return '%s %s' % (self.vehicleno, self.rate)

class Transport(models.Model):
	"""
	Model of Transport  Bill record
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
	class Meta :
		model = Transport

class Bankdetails(models.Model):
	accname = models.CharField(max_length=50)
	accountno = models.IntegerField(null=False)
	accountcode = models.CharField(max_length=50)
	address = models.CharField(max_length=150)

class BankdetailsForm(ModelForm):
	class Meta :
		model = Bankdetails

