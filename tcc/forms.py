"""
%% forms.py %%

This file contain the defination of the forms of Automation Software 
"""

from django import forms
from Automation.tcc.models import *

class SuspenceClearence(forms.Form):
	"""
	**SuspenceClearance**

	Suspence Clearence Form for adding extra Charges like labour, car taxi, boring charge, etc.
	"""
	
	labour_charge = forms.IntegerField(initial= '0')
	car_taxi_charge = forms.IntegerField(initial= '0')
	boring_charge_external = forms.IntegerField(initial= '0')
	boring_charge_internal = forms.IntegerField(initial= 0)
	lab_testing_staff = forms.CharField(max_length = 20)
	field_testing_staff = forms.CharField(max_length = 20,required=False)

class ContactForm(forms.Form):
   	subject = forms.CharField(max_length=100)
    	email = forms.EmailField( label='Your e-mail address')
    	message = forms.CharField(widget=forms.Textarea)

class MonthlyReportadd(forms.Form):
	"""
	**MonthlyReportadd**

	Monthly Reportadd Form is for getting the monthly income and taxes of the company and then subtrating the paid taxes from it.
	"""
 
	month = forms.ChoiceField(choices=MONTH_CHOICES)
	year = forms.ChoiceField(choices=YEAR_CHOICES)
	paid_service_tax =forms.IntegerField(initial= '0')
	paid_education_tax =forms.IntegerField(initial= '0')
	paid_higher_education_tax =forms.IntegerField(initial= '0')
	
class DailyReportadd(forms.Form):
	"""
	**DailyReportadd**

	Daily Report Form to retrieve Daily income Information for a specified payment type like cash, cheque, online and Demand Draft.
	"""

        start_date= forms.DateField()
        end_date= forms.DateField()
        type = forms.ChoiceField( choices=DAILY_CHOICES)

class MonthlyReport(forms.Form):
	"""
	**MonthlyReport**

	Montly Report Form to retrieve Montly Tax Information.
	"""

	month = forms.ChoiceField(choices=MONTH_CHOICES)
	year = forms.ChoiceField(choices=YEAR_CHOICES)

class DateReport(forms.Form):
	"""
	**DateReport**

	Date Report Form that displays start and end date and thus helps in retrieving data between this date range.
	"""

	start_date= forms.DateField()
        end_date= forms.DateField()

	def clean_date(self):
        	start_date = self.cleaned_data['start_date']
		end_date = self.cleaned_data['end_date']
        	if start_date > datetime.date.today():
        	    raise forms.ValidationError("The date cannot be in the future!")
        	return date

class GovPriReport(forms.Form):
	"""
	**GovPriReport**

	Governament Private Report is for different Jobs like: Government/Semi_government/Private. 
	"""

	month = forms.ChoiceField(choices=MONTH_CHOICES)
	year = forms.ChoiceField(choices=YEAR_CHOICES)
	type_of_work = models.ForeignKey(Govt)

class CashBook(forms.Form):
	"""
	**CashBook**

	Cash book to manage the money transactions within a specified date range.
	"""

        start_date= forms.DateField()
        end_date= forms.DateField()
	name = forms.CharField(max_length = 100)
	amount_given = forms.CharField(max_length = 100)


	
