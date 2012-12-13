from django import forms
from Automation.tcc.models import *

class SuspenceClearence(forms.Form):
	"""
	Suspence Clearence Form for adding extra Charges. 
	"""
	
	labour_charge = forms.IntegerField(initial= '0')
	car_taxi_charge = forms.IntegerField(initial= '0')
	boring_charge_external = forms.IntegerField(initial= '0')
	boring_charge_internal = forms.IntegerField(initial= 0)
	lab_testing_staff = forms.CharField(max_length = 20)
	field_testing_staff = forms.CharField(max_length = 20,required=False)

class MonthlyReportadd(forms.Form):
	month = forms.ChoiceField(choices=MONTH_CHOICES)
	year = forms.ChoiceField(choices=YEAR_CHOICES)
	paid_service_tax =forms.IntegerField(initial= '0')
	paid_education_tax =forms.IntegerField(initial= '0')
	paid_higher_education_tax =forms.IntegerField(initial= '0')
	
class DailyReportadd(forms.Form):
	"""
	Daily Report Form to reterive Daily income Information.
	"""
        start_date= forms.DateField()
        end_date= forms.DateField()
        type = forms.ChoiceField( choices=DAILY_CHOICES)

class MonthlyReport(forms.Form):
	"""
	Montly Report Form to reterive Montly Tax Information.
	"""
	month = forms.ChoiceField(choices=MONTH_CHOICES)
	year = forms.ChoiceField(choices=YEAR_CHOICES)

class DateReport(forms.Form):
	"""
	Form that displays start and end date and thus helps in retrieving data between this date range.
	"""
	start_date= forms.DateField()
        end_date= forms.DateField()

class GovPriReport(forms.Form):
	"""
	Montly Report for different Jobs like: Government/Semi_government/Private. 
	"""
	month = forms.ChoiceField(choices=MONTH_CHOICES)
	year = forms.ChoiceField(choices=YEAR_CHOICES)
	type_of_work = models.ForeignKey(Govt)

class CashBook(forms.Form):
	"""
	Cash book to manage the money transactions
	"""
        start_date= forms.DateField()
        end_date= forms.DateField()
	name = forms.CharField(max_length = 100)
	amount_given = forms.CharField(max_length = 100)


	
