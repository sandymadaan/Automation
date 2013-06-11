"""
%% registers.py %%

This file is used to create the views for registers of the software. 
It is the interface between the user interface, urls and database.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::#
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.db.models import Max ,Q, Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.db.models import F
from django import template
from tagging.models import Tag, TaggedItem
from Automation.tcc.choices import *
from Automation.tcc.models import *
from Automation.tcc.functions import *
from Automation.tcc.forms import *
from Automation.tcc.convert_function import *
from django.core.mail import send_mail          
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE FUNCTIONS HERE:::::::::::::::::::::#
def material_site():
	"""
	This function is to be used through out the functions in the file. 
	The	objects defined ere like the college name and the software 
	name is to be used by nearly all the templates of the software.
	"""
	material = Material.objects.all().filter(report=1)
	field = Material.objects.all().filter(report=2)
	title = Department.objects.get(id=1)	
	address = get_object_or_404(Organisation, pk='1')
	report = Report.objects.all()
	work = Govt.objects.all()
	payment = Payment.objects.all()
	template = {'material':material, 'field':field, 'title':title, 
	'address':address, 'report':report, 'work':work, 'payment':payment}
	return template

tmp = material_site()

job = Job.objects.aggregate(Max('id'))
jobmaxid = job['id__max']




def  monthly_report(request):
	"""
	** monthly_report **

	Monthly report Function generates the register of work done within 
	a month. This also asks for the paid education tax, higher 
	education tax and service tax and then subtracts from the taxes 
	for the month.
	"""
	if request.method == 'POST':
		form = MonthlyReportadd(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			month = cd['month']
			year = cd['year']
			paid_education_tax= cd['paid_education_tax']
			paid_higher_education_tax= cd['paid_higher_education_tax']
			paid_service_tax= cd['paid_service_tax']
			month = months(month)
			client = Job.objects.filter(date__year=year).\
			filter(date__month=month).values('job_no','date',
			'client__client__first_name', 'client__client__middle_name',	
			'client__client__last_name', 'client__client__address', 
			'client__client__city').distinct().order_by('job_no')
			bill = Bill.objects.all()
			job = Job.objects.all().values_list('job_no',flat=True).\
			filter(date__year=year).filter(date__month=month)
			total_temp = Bill.objects.filter(job_no__in=job).\
			aggregate(Sum('price'))
			total= int(total_temp['price__sum'])
			service_tax_temp = Bill.objects.filter(job_no__in=job).\
			aggregate(Sum('service_tax'))
			service_tax= int(service_tax_temp['service_tax__sum'])
			education_tax_temp = Bill.objects.filter(job_no__in=job).\
			aggregate(Sum('education_tax'))
			education_tax= int(education_tax_temp['education_tax__sum'])
			higher_education_tax_temp = Bill.objects.filter(job_no__in
			=job).aggregate(Sum('higher_education_tax'))
			higher_education_tax= int(higher_education_tax_temp\
			['higher_education_tax__sum'])
			net_total_temp = Bill.objects.filter(job_no__in=job).\
			aggregate(Sum('net_total'))
			net_total= int(net_total_temp['net_total__sum'])
			tax = service_tax+education_tax+higher_education_tax
			ser_tax = service_tax-int(paid_service_tax)
			edu_tax = education_tax-paid_education_tax
			high_tax = higher_education_tax-paid_higher_education_tax
			final = ser_tax + edu_tax +high_tax
			paid_tax = paid_education_tax + paid_higher_education_tax+\
			paid_service_tax
			template = {'client':client, 'bill':bill, 'tax':tax, 'month'
			: month, 'service_tax':service_tax, 'education_tax'
			:education_tax, 'higher_education_tax':higher_education_tax, 
			'net_total':net_total, 'total':total, 'year':year, 
			'paid_higher_education_tax':paid_higher_education_tax, 
			'paid_tax':paid_tax, 'paid_education_tax':paid_education_tax, 
			'paid_service_tax':paid_service_tax, 'final':final, 
			'ser_tax':ser_tax,'edu_tax':edu_tax, 'high_tax':high_tax,}
			return render_to_response('tcc/monthlyreport.html',
			dict(template.items() + tmp.items()), context_instance=
			RequestContext(request))
	else:
		form = MonthlyReportadd()
	data = {'form': form}
	return render_to_response('tcc/client.html', dict(data.items() + 
	tmp.items()), context_instance=RequestContext(request))


def  Cashbook(request):    
	"""
	** Cashbook **

	This gives the debit and credit detail within a date range. The 
	amount deposited in some bank or credited to someone can also be 
	subtracted from the total.
	"""    
	if request.method == 'POST':
		form = CashBook(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date'] 
			dates(start_date, end_date)	
			name = cd['name']
			amount_given = cd['amount_given']
			temp = [0,0,0,0,0]
			i=0
			range = name.split(',')
			while i < len(range):
				temp[i] = range[i]
				i+=1
			name1 = temp[0]
			name2 = temp[1]
			name3 = temp[2]
			name4 = temp[3]
			name5 = temp[4]
			range = amount_given.split(',')
			tempamt = [0,0,0,0,0]
			j=0
			while j < len(range):
				tempamt[j] = range[j]
				j+=1
			amount1 = tempamt[0]
			amount2 = tempamt[1]
			amount3 = tempamt[2]
			amount4 = tempamt[3]
			amount5 = tempamt[4]
			sumamt = sum((int(amount1),int(amount2),int(amount3),
			int(amount4),int(amount5)))
			client = Job.objects.filter(date__range=(start_date,
			end_date)).values('job_no', 'date', 
			'client__client__first_name', 'pay', 'id').distinct().\
			order_by('job_no').filter(pay='CASH')
			job = Job.objects.all().filter(date__range=(start_date,
			end_date)).filter(pay='CASH')
			chequeclient = Job.objects.filter(date__range=(start_date,
			end_date)).filter(Q(pay='CHEQUE')|Q(pay='DD')|Q(pay=\
			'ONLINE')).values('job_no','date', 
			'client__client__first_name','pay').distinct().order_by(\
			'job_no')
			testtotal = TestTotal.objects.all()
			chequejob = Job.objects.all().filter(date__range=(start_date,
			end_date)).	filter(Q(pay='CHEQUE')|Q(pay='DD')|Q(pay=\
			'ONLINE'))
			total_temp = TestTotal.objects.filter(job_id__in=job).\
			aggregate(Sum('unit_price'))
			total= int(total_temp['unit_price__sum'])
			net_total_temp = TestTotal.objects.filter(job_id__in=
			chequejob).aggregate(Sum('unit_price'))
			net_total= int(net_total_temp['unit_price__sum'])
			balance = int(total)-int(sumamt)
			template ={'date': start_date, 'client':client, 'type':type, 
			'total':total, 'testtotal':testtotal, 'net_total':net_total, 
			'name1':name1, 'name2':name2, 'name3':name3, 'name4':name4, 
			'name5':name5, 'balance':balance, 'amount1':amount1, 
			'amount2':amount2, 'amount3':amount3, 'amount4':amount4, 
			'amount5':amount5, 'sumamt':sumamt, 'chequeclient':
			chequeclient }
			return render_to_response('tcc/cashbook.html',dict(\
			template.items() + tmp.items()), context_instance=
			RequestContext(request))
      	else:
		form = CashBook()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))


def  daily_report(request): 
	"""
	** daily_report **

	This lists the jobs with payment type as Cash, Cheque, DD or Online 
	depending on choice selected, within a date range.
	"""
	if request.method == 'POST':
		form = DailyReportadd(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date']
			type = cd['type']
			dates(start_date, end_date)	
			if type=="CASH":
				client = Job.objects.filter(date__range=(start_date,
				end_date)).filter(pay='CASH').values( 'date', 
				'client__client__first_name','client__client__middle_name',
				'client__client__last_name','client__client__address',
				'client__client__city','job_no','client__client__company'\
				).order_by('job_no').distinct()
				job = Job.objects.all().values_list('job_no',flat=True).\
				filter(date__range=(start_date,end_date)).filter(pay=
				'CASH')
				bill = Bill.objects.all()
				net_total_temp = Bill.objects.filter(job_no__in=job).\
				aggregate(Sum('net_total'))
				net_total= net_total_temp['net_total__sum']
				template ={'s_date': start_date,'e_date':end_date, 
				'client':client, 'type':type, 'bill':bill,'net_total':
				net_total,'job':job}
				return render_to_response('tcc/dailyreport.html', 
				dict(template.items() + tmp.items()), context_instance=
				RequestContext(request))
			else :
				client = Job.objects.filter(date__range=(start_date,
				end_date)).filter(Q(pay='CHEQUE')|Q(pay='DD')|\
				Q(pay='ONLINE')).values( 'date','client__client__first_name',
				'client__client__middle_name','client__client__last_name',
				'client__client__address','client__client__city','job_no').\
				order_by('job_no').distinct()
				job = Job.objects.all().values_list('job_no',flat=True).\
				filter(date__range=(start_date,end_date)).\
				filter(Q(pay='CHEQUE')|Q(pay='DD')|Q(pay='ONLINE'))
				bill = Bill.objects.all()
				net_total_temp = Bill.objects.filter(job_no__in=job).\
				aggregate(Sum('net_total'))
				net_total= net_total_temp['net_total__sum']
				template ={'date': start_date, 'client':client, 'type'
				:type, 'bill':bill,'net_total':net_total,'job':job}
				return render_to_response('tcc/dailyreport.html', 
				dict(template.items() + tmp.items()), context_instance=
				RequestContext(request))
	else:
		form = DailyReportadd()
	template = {'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))

def  main_register(request):
	"""
	** main_register **

	Main Register function lists all the jobs that are in general report i.e. 
	they are not suspence jobs.
	"""
	if request.method == 'POST':
		form = MonthlyReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			month = cd['month']
			year = cd['year']
			month_print = month
			month = months(month)
			job = Job.objects.filter(date__year=year).filter(date__month
			=month)
			client = Job.objects.filter(date__year=year).\
			filter(date__month= month).values(\
			'client__client__first_name')
			amount = Amount.objects.all().filter(job_id__in=job).\
			filter(report_type ='General_report').values('job__date', 
			'job__id', 'job__job_no', 'college_income', 'admin_charge', 
			'consultancy_asst', 'development_fund', 'unit_price', 
			'job__client__client__first_name', 
			'job__client__client__middle_name',
			'job__client__client__last_name', 
			'job__client__client__address', 'job__client__client__city',
			'job__clientjob__material__name',
			'job__client__client__company').order_by('job__id')
			admin_charge_temp = Amount.objects.filter(job_id__in=job).\
			filter(report_type ='General_report').aggregate(Sum(\
			'admin_charge'))
			admin_charge= admin_charge_temp['admin_charge__sum']
			college_income_temp =Amount.objects.filter(job_id__in=job).\
			filter(report_type ='General_report').aggregate(Sum(\
			'college_income'))
			college_income= college_income_temp['college_income__sum']
			consultancy_asst_temp =Amount.objects.filter(job_id__in=job).\
			filter(report_type = 'General_report').aggregate(Sum(\
			'consultancy_asst'))
			consultancy_asst= consultancy_asst_temp[\
			'consultancy_asst__sum']
			development_fund_temp = Amount.objects.filter(job_id__in=
			job).filter(report_type = 'General_report').aggregate(Sum(\
			'development_fund'))
			development_fund= development_fund_temp[\
			'development_fund__sum']
			price_temp = Amount.objects.filter(job_id__in=job).\
			filter(report_type = 'General_report').aggregate(Sum(\
			'unit_price'))
			total= price_temp['unit_price__sum']
			template ={'month': month_print, 'year':year, 'amount':
			amount, 'job':job, 'admin_charge':admin_charge, 
			'college_income':college_income, 'consultancy_asst':
			consultancy_asst,'development_fund':development_fund, 
			'total':total, 'client':client}
			return render_to_response('tcc/main_register.html', 
			dict(template.items() + tmp.items()), context_instance=
			RequestContext(request))
	else:
		form = MonthlyReport()
	template = {'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))

def suspence_clearence_register(request):
	"""
	** suspence_clearance_register **

	This function lists all the suspence jobs that are cleared.
	"""
	if request.method == 'POST':
		form = DateReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date']
			dates(start_date, end_date)	
			job = Job.objects.filter(date__range=(start_date,end_date))
			suspence =SuspenceJob.objects.all().filter(job_id__in=job).\
			values('field__name', 'job_id').distinct()
			suspencedetail = Suspence.objects.all().filter(job_id__in
			=job).values('work_charge', 'labour_charge', 
			'boring_charge_external', 'car_taxi_charge', 
			'boring_charge_internal', 'job_id')
			amount = Amount.objects.all().filter(job_id__in=job).\
			filter(report_type = 
			'Suspence').values('job__date', 'job__id', 'job__job_no', 
			'college_income', 'admin_charge', 'consultancy_asst', 
			'development_fund', 'unit_price',
			'job__client__client__first_name').order_by('job__id').\
			distinct().exclude(admin_charge = None)
			admin_charge_temp = Amount.objects.filter(id__in=job).\
			filter(report_type = 'Suspence').aggregate(Sum(\
			'admin_charge'))
			admin_charge= admin_charge_temp['admin_charge__sum']
			college_income_temp = Amount.objects.filter(id__in=job).\
			filter(report_type = 'Suspence').aggregate(Sum(\
			'college_income'))
			college_income= college_income_temp['college_income__sum']
			consultancy_asst_temp =Amount.objects.filter(id__in=job).\
			filter(report_type = 
			'Suspence').aggregate(Sum('consultancy_asst'))
			consultancy_asst= consultancy_asst_temp[\
			'consultancy_asst__sum']
			development_fund_temp = Amount.objects.filter(id__in=job).\
			filter(report_type = 'Suspence').aggregate(Sum(\
			'development_fund'))
			development_fund= development_fund_temp[\
			'development_fund__sum']
			price_temp = Amount.objects.filter(id__in=job).\
			filter(report_type = 'Suspence').exclude(admin_charge =
			None).aggregate(Sum('unit_price'))
			total= price_temp['unit_price__sum']
			template ={'form':form, 'job':job, 'suspence':suspence, 
			'suspencedetail':suspencedetail, 'amount': amount,'date': 
			start_date, 'admin_charge':admin_charge, 'college_income'
			:college_income, 'consultancy_asst':consultancy_asst, 
			'development_fund':development_fund, 'total':total,}
			return render_to_response('tcc/suspence_clearence_register.html', 
			dict(template.items() + tmp.items()), context_instance=
			RequestContext(request))
	else:
		form = DateReport()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))

def suspence_register(request):
	"""
	** suspence_register **

	This function lists all the suspence Jobs registered within a
	particular date range.
	"""
	if request.method == 'POST':
		form = DateReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date']
			dates(start_date, end_date)	
			job = Job.objects.filter(amount__report_type="Suspence").\
			filter(date__range=(start_date,end_date)).values( 'date', 
			'client__client__first_name','client__client__middle_name',
			'client__client__last_name','client__client__address', 
			'report_type','client__client__city','job_no', 'id', 
			'clientjob__material__name', 'suspencejob__field__name', 
			'pay', 'tds','check_number', 'check_dd_date','testtotal__unit_price').\
			order_by('id').distinct()
			client = Job.objects.all().values_list('job_no',flat=True).\
			filter(date__range=(start_date,end_date)).\
			filter(amount__report_type="Suspence")
			bill = Bill.objects.all()
			net_total_temp = Bill.objects.filter(job_no__in=client).\
			aggregate(Sum('net_total'))
			net_total= net_total_temp['net_total__sum']
			template ={'s_date': start_date, 'e_date':end_date, 
			'client':client, 'type':type, 'bill':bill,'net_total':
			net_total,'job':job}
			return render_to_response('tcc/suspence_register.html', 
			dict(template.items() + tmp.items()), context_instance=
			RequestContext(request))
	else:
		form = DateReport()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))

# Payment Register

def payment_register(request):
	"""
	** payment_register **

	This function lists all the payment Jobs. This include the general
	report wrk and suspence Jobs too. The register is made within a
	particular date range.
	"""
	if request.method == 'POST':
		form = DateReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date']
			dates(start_date, end_date)	
			job = Job.objects.filter(date__range=(start_date,end_date))\
			.values( 'date', 'client__client__first_name',
			'client__client__middle_name','client__client__last_name',
			'client__client__address', 'client__client__company',
			'client__client__city', 'client__client__email_address', 
			'client__client__contact_no', 'client__client__pin_code', 
			'clientjob__material__name', 'suspencejob__field__name',
			'report_type', 'job_no','id').order_by('job_no').distinct()
			client = Job.objects.all().values_list('job_no',flat=True).\
			filter(date__range=(start_date,end_date))
			bill = Bill.objects.all()
			net_total_temp = Bill.objects.filter(job_no__in=client).\
			aggregate(Sum('net_total'))
			net_total= net_total_temp['net_total__sum']
			template ={'form': form, 'job':job, 'bill':bill,
            'net_total':net_total}
			return render_to_response('tcc/payment_register.html', 
			dict(template.items() + tmp.items()), context_instance=
			RequestContext(request))
	else:
		form = DateReport()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))

# End Payment Register

# Performa Bill Register

def performa_register(request):
	"""
	** performa_register **

	This function lists all  the performa jobs within a particular
	date range.
	"""
	if request.method == 'POST':
		form = DateReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date']
			dates(start_date, end_date)	
			job = EditJob.objects.filter(date__range=(start_date,
			end_date)).values( 'date', 'client__client__first_name',
			'client__client__middle_name','client__client__last_name',
			'client__client__address', 'client__client__company',
			'client__client__city', 'client__client__email_address', 
			'client__client__contact_no','client__client__pin_code', 
			'clienteditjob__material__name', 'suspenceeditjob__field__name',
			'report_type', 'job_no','id').order_by('job_no').distinct()
			client = EditJob.objects.all().values_list('job_no',flat=True).\
			filter(date__range=(start_date,end_date))
			bill = BillPerf.objects.all()
			net_total_temp = BillPerf.objects.filter(job_no__in = 
			client).aggregate(Sum('net_total'))
			net_total= net_total_temp['net_total__sum']
			template ={'form': form, 'job':job, 'bill':bill,
			'net_total':net_total}
			return render_to_response('tcc/performa_register.html', 
			dict(template.items() + tmp.items()), context_instance =
			RequestContext(request))
	else:
		form = DateReport()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))

# End Performa Bill Register

def tds_register(request):
	"""
	** tds_register **

	This function lists all the jobs with TDS amount within a
	particular date range.
	"""
	if request.method == 'POST':
		form = DateReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date']
			dates(start_date, end_date)
			job = Job.objects.exclude(tds=0).filter(date__range=
			(start_date, end_date)).values('job_no', 'date', 
			'client__client__first_name','client__client__middle_name', 
			'client__client__last_name', 'client__client__address', 
			'client__client__city', 'date', 'tds')
			bill = Bill.objects.all()
			client = Job.objects.values_list('job_no',flat=True).\
			exclude(tds=0).\
			filter(date__range=(start_date, end_date))
			tds_temp = Job.objects.filter(job_no__in=client).\
			aggregate(Sum('tds'))
			tds= tds_temp['tds__sum']			
			total_temp = Bill.objects.filter(job_no__in=client).\
			aggregate(Sum('price'))
			total= total_temp['price__sum']
			service_tax_temp = Bill.objects.filter(job_no__in=client).\
			aggregate(Sum('service_tax'))
			service_tax= service_tax_temp['service_tax__sum']
			education_tax_temp = Bill.objects.filter(job_no__in=client).\
			aggregate(Sum('education_tax'))
			education_tax= education_tax_temp['education_tax__sum']
			higher_education_tax_temp = Bill.objects.filter(job_no__in
			=client).aggregate(Sum('higher_education_tax'))
			higher_education_tax= higher_education_tax_temp\
			['higher_education_tax__sum']
			net_total_temp = Bill.objects.filter(job_no__in=client).\
			aggregate(Sum('net_total'))
			net_total= net_total_temp['net_total__sum']
			balance_temp = Bill.objects.filter(job_no__in=client).\
			aggregate(Sum('balance'))
			balance= balance_temp['balance__sum']
			template = {'job':job, 'bill':bill, 'total':total, 
			'service_tax':service_tax, 'education_tax':education_tax, 
			'higher_education_tax':higher_education_tax, 'tds':tds,
			'net_total':net_total, 'balance':balance, 's_date':start_date, 
			'e_date':end_date}
			return render_to_response('tcc/tds_register.html', 
			dict(template.items() + tmp.items()), context_instance=
			RequestContext(request))
	else:
		form = DateReport()
	template = {'form':form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))
			
def non_payment_register(request):
	"""
	** non_payment_register **

	This function lists all the information of non payment jobs within
	the specified date range.
	"""
	if request.method == 'POST':
		form = DateReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date']
			dates(start_date, end_date)
			npr_obj = NonPaymentJob.objects.all().filter(date__range=
			(start_date, end_date)).values('id','date', 'dated','ref_no',
			'site','client__first_name','client__middle_name',
			'client__last_name','client__address','material_type')
			template = {'npr_obj':npr_obj}
			return render_to_response('tcc/non_payment_register.html', 
			dict(template.items() + tmp.items()), context_instance=
			RequestContext(request))
	else:
		form = DateReport()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))	

# Client Register

def client_register(request):
	"""
	** client_register **

	This function is used to list all the information about the
	clients registered within the date range specified.
	"""
	if request.method == 'POST':
		form = DateReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start_date = cd['start_date']
			end_date = cd['end_date']
			dates(start_date, end_date)
			cr_obj = UserProfile.objects.all().filter(date__range=
			(start_date,end_date)).values('first_name','middle_name', 
			'last_name', 'address', 'company', 'city', 'pin_code', 
			'state', 'website', 'email_address', 'contact_no', 
			'type_of_organisation', 'date')
			template={'cr_obj':cr_obj}
			return render_to_response('tcc/client_register.html', 
			dict(template.items()
			+ tmp.items()), context_instance=RequestContext(request))
	else:
		form = DateReport()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() 
	+ tmp.items()), context_instance=RequestContext(request))	

# end cliemt_register function

def  gov_pri_report(request):
	"""
	** gov_pri_report **

	This function lists the jobs that are Goverment, Semi-Government 
	or Private depending upon the choice made within a particular date range.
	
	"""
	if request.method == 'POST':
		form = GovPriReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			type_of_organisation =cd['type_of_organisation']
			month = cd['month']
			year = cd['year']
			month = months(month)
			client = Job.objects.filter(date__year=year).filter(date__month
			=month).filter(type_of_work = type_of_organisation)
			amount = Amount.objects.all().filter(job_id__in=job).\
			filter(report_type = 'Suspence').values('job__date', 
			'job__id', 'job__job_no', 'college_income', 'admin_charge', 
			'consultancy_asst', 'development_fund', 'unit_price', 
			'job__client__client__name').order_by('job__id').\
			distinct().exclude(admin_charge = None)
			admin_charge_temp = Amount.objects.filter(date__year=year)\
			.filter(date__month=month).filter(report_type = 
			'GENERAL REPORT').aggregate(Sum('admin_charge'))
			admin_charge = admin_charge_temp['admin_charge__sum']
			college_income_temp = Amount.objects.filter(date__year=
			year).filter(date__month=month).filter(report_type = 
			'GENERAL REPORT').aggregate(Sum('college_income'))
			college_income = college_income_temp['college_income__sum']
			consultancy_asst_temp = Amount.objects.filter(date__year=
			year).filter(date__month=month).filter(report_type=
			'GENERAL REPORT').aggregate(Sum('consultancy_asst'))
			consultancy_asst = consultancy_asst_temp['consultancy_asst__sum']
			development_fund_temp = Amount.objects.filter(date__year=
			year).filter(date__month=month).filter(report_type=
			'GENERAL REPORT').aggregate(Sum('development_fund'))
			development_fund= development_fund_temp['development_fund__sum']
			service_tax_temp = Amount.objects.filter(date__year=year).\
			filter(date__month=month).filter(report_type = 
			'GENERAL REPORT').aggregate(Sum('service_tax'))
			service_tax= service_tax_temp['service_tax__sum']
			education_tax_temp = Amount.objects.filter(date__year=
			year).filter(date__month=month).filter(report_type = 
			'GENERAL REPORT').aggregate(Sum('education_tax'))
			education_tax= education_tax_temp['education_tax__sum']
			higher_education_tax_temp = Amount.objects.filter(date__year
			=year).filter(date__month=month).filter(report_type=
			'GENERAL REPORT').aggregate(Sum('higher_education_tax'))
			higher_education_tax= higher_education_tax_temp\
			['higher_education_tax__sum']
			balance_temp = Amount.objects.filter(date__year=year).\
			filter(date__month=month).filter(report_type=
			'GENERAL REPORT').aggregate(Sum('balance'))
			balance= balance_temp['balance__sum']
			tds_temp = Amount.objects.filter(date__year=year).\
			filter(date__month=month).filter(report_type =
			'GENERAL REPORT').aggregate(Sum('tds'))
			tds= tds_temp['tds__sum']
			return render_to_response('Automation/gov_pri_report.html', 
			dict(template.items() + tmp.items()), context_instance=
			RequestContext(request))
	else:
		form = MonthlyReport()
	template =  {'form': form}
	return render_to_response('Automation/client.html',
	dict(template.items() + tmp.items()), context_instance=
	RequestContext(request))

def lab_report(request):       
	"""
	** lab_report **

	This function lists all the jobs for a particular material in a 
	date range.
	"""   
	form = LabReport(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		start_date = cd['start_date']
		end_date = cd['end_date'] 
		dates(start_date, end_date)	 
		material = cd['material']
		mat = Material.objects.get(name=material)
		if mat.report_id==1:
			job = Job.objects.filter(clientjob__material__name=material).\
			filter(date__range=(start_date,end_date))
		else:
			job = Job.objects.filter(suspencejob__field__name=material).\
			filter(date__range=(start_date,end_date))
		client = Job.objects.filter(id__in=job).values('job_no', 'date', 
		'client__client__first_name', 'client__client__address', 'amount__unit_price')
		total_temp = Amount.objects.all().filter(job__in=job).\
		aggregate(Sum('unit_price'))
		total= total_temp['unit_price__sum']
		template ={'form':form, 'total':total, 'date':start_date, 
		'client':client, 'job':job, 'material':material}
		return render_to_response('tcc/labreport.html', 
		dict(template.items() + tmp.items()) , context_instance =
		RequestContext(request))
	else:
		form = LabReport()         
	template ={'form': form}  
	return render_to_response('tcc/client.html', dict(template.items() + 
	tmp.items()), context_instance=RequestContext(request))
