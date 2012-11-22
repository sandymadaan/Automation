from django import forms
from Automation.tcc.models import *

class SuspenceClearence(forms.Form):
	"""
	Suspence Clearence Form for adding extra Charges. 
	"""
	job_no = forms.IntegerField()
	labour_charge = forms.IntegerField(initial= '0')
	car_taxi_charge = forms.IntegerField(initial= '0')
	boring_charge_external = forms.IntegerField(initial= '0')
	boring_charge_internal = forms.IntegerField(initial= 0)
	lab_testing_staff = forms.CharField(max_length = 20)
	field_testing_staff = forms.CharField(max_length = 20,required=False)
