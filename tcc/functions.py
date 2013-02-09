def retrieve():
	from Automation.tcc.variable import *
	#amount = get_object_or_404(Amount, pk=job_no_id)
	collegeincome = collegeincome
	admincharge = admincharge
	servicetaxprint = servicetaxprint
	educationtaxprint =educationtaxprint
	highereducationtaxprint = highereducationtaxprint


individual_ratio1 = 60
individual_ratio2 = 40
institutional_ratio1 = 40
institutional_ratio2 = 60
routine_ratio1 = 30
routine_ratio2 = 70

def ratio1(con_type):
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
	if con_type == 'ROUTINE':
		
		ratio2 = routine_ratio2
	elif con_type == 'INDIVIDUAL':
		
		ratio2 = individual_ratio2
	else :
		ratio2 = institutional_ratio2
	return ratio2

def months(month):
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
	

	
