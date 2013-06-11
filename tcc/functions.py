"""
%% functions.py %%

This file is defines some important functions that are then called views.py file.  
"""

#:::::::::::::::::::::::CONSTANTS:::::::::::::::::::::::::::::::::::#
individual_ratio1 = 60
individual_ratio2 = 40
institutional_ratio1 = 40
institutional_ratio2 = 60
routine_ratio1 = 30
routine_ratio2 = 70
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE FUNCTIONS HERE:::::::::::::::::::::::::::#

def retrieve():
	"""
	** retrieve **

	Retrieve function is used to retrieve the data defined in variable.py file
	"""

	from Automation.tcc.variable import *
	collegeincome = collegeincome
	admincharge = admincharge
	servicetaxprint = servicetaxprint
	educationtaxprint =educationtaxprint
	highereducationtaxprint = highereducationtaxprint

def dates(start_date, end_date):
	import datetime
	from django import forms
	if start_date > datetime.date.today() or end_date > datetime.date.today():
		raise forms.ValidationError("The date cannot be in the future!")
	elif end_date < start_date :
		raise forms.ValidationError("The start_date is greater than end_date!")
	else:
		pass

def ratio1(con_type):
	"""
	** ratio1 **
	
	ratio1 function is creates the numerator of the ratio depanding upon the consultancy(Individual, Routine) type of the work.
	"""

	if con_type == 'ROUTINE':
		ratio1 = routine_ratio1
		ratio2 = routine_ratio2
	elif con_type == 'INDIVIDUAL':
		ratio1 = individual_ratio1
		ratio2 = individual_ratio2
	else :
		ratio1 = institutional_ratio1
		ratio2 = institutional_ratio2
	return ratio1

def ratio2(con_type):
	"""
	** ratio2 **
	
	ratio2 function is creates the denomenator of the ratio depending upon the consultancy type of the work.
	"""

	if con_type == 'ROUTINE':
		
		ratio2 = routine_ratio2
	elif con_type == 'INDIVIDUAL':
		
		ratio2 = individual_ratio2
	else :
		ratio2 = institutional_ratio2
	return ratio2

def months(month):
	"""
	** months **
	
	months Function converts the months name to there number.
	"""
	if month =='November':
		month =11
	elif month == 'December':
		month =12
	elif month == 'October':
		month =10
	elif month == 'September':
		month =9
	elif month == 'August':
		month =8
	elif month == 'July':
		month =7
	elif month == 'June':
		month = 6
	elif month == 'May':
		month =5
	elif month == 'April':
		month =4
	elif month == 'March':
		month =3
	elif month == 'February':
		month =2
	else :
		month =1
	return month
	

	
