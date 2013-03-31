"""
%% Views_ext.py %%
This file is used to create the views for the software. 
In order to avoid the confusion with generating the temperory jobs and then making them permanents, a different views file is created.
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
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#


@login_required
def perfselectfield(request):
	"""
	** perfselectfield **

	List the type of work to be done i.e Lab or Field work. Here, if the same client is making the slection 2 times then if condition is 		passed else the client is added in clientadd table.
	"""

	client =UserProfile.objects.get(id=request.GET['id'])
	add = editClientadd.objects.aggregate(Max('id'))    # this is in case one clicks on adding more material into a job
	addid =add['id__max']
	if addid == client:
		pass
	else:
		user = request.user
		m = editClientadd(client = client,user=user)
		m.save()
	report = Report.objects.all()
	mat = Material.objects.all()
	return render_to_response('tcc/performa/typeofworkperf.html',{'report':report,'mat':mat}, context_instance=RequestContext(request))

@login_required
def perfselect(request):
	"""
	** perfselect **

	List down the materials or the field work depending on the selection of the type of work.
	"""	

	report = Report.objects.all()
	mat = Material.objects.all()
	material = Report.objects.get(id=request.GET['id'])
	field_list = Material.objects.all().filter(report_id =material)
	return render_to_response('tcc/performa/tagsperf.html',{'field_list':field_list,'report':report,'mat':mat}, context_instance=RequestContext(request))

@login_required
def add_perf(request):
	"""
	** add_perf **

	This helps the user to add the job. Depending upon the material selected the tests are listed then. Two forms are defined in a single 		template file, so that there data get stored in different tables one after the other.
	"""

	report = Report.objects.all()
	query =request.GET.get('q', '')
	id = BillPerf.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	if maxid== None :
		maxid = 1
	else:
		maxid = maxid + 1
	work = Govt.objects.all()
	payment = Payment.objects.all()
	material =Material.objects.get(id=request.GET['q'])
	test = Test.objects.all().filter(material_id = query)
	if material.report_id == 1:
		field_list = Material.objects.all().filter(report_id = 1)
		if request.method=='POST':
			form1 = editJobForm(request.POST)
			form2 = editClientJobForm(request.POST)
			if form1.is_valid and form2.is_valid():
				def clean_name(self):
        				cleaned_data = self.cleaned_data
					pay = cleaned_data.get('pay', '')
					check_number = cleaned_data.get('check_number', '')
					check_dd_date = cleaned_data.get('check_dd_date', '')
					sample = cleaned_data.get('sample', '')
				profile = form1.save(commit=False)
				profile.job_no = maxid
				profile.ip = request.META.get('REMOTE_ADDR')
				cl = editClientadd.objects.aggregate(Max('id'))
				clientid =cl['id__max']
				clid = editClientadd.objects.get(id = clientid)
				profile.client = clid
				report = Report.objects.get(id=1)
				profile.report_type = report
				profile.save()
				form1.save_m2m()
				test = request.POST.getlist('test')
       				profile1 = form2.save(commit=False)		
				profile1.material = material
				jbmx = EditJob.objects.aggregate(Max('id'))
				jobmax =jbmx['id__max']
				client =EditJob.objects.get(id =jobmax)
				profile1.job = client
				profile1.save()
				form2.save_m2m()
				if profile.report_type == "1":
					return HttpResponseRedirect(reverse('Automation.tcc.views_ext.add_suspence_perf'))
				else :
					return HttpResponseRedirect(reverse('Automation.tcc.views_ext.gen_report_perf'))
		else:	
			form1 = editJobForm()
			form2 = editClientJobForm()
		return render_to_response('tcc/performa/add_perf.html', {"form1": form1,"test":test,'field_list':field_list,'payment':payment,'work':work,"report":report}, context_instance=RequestContext(request))
	else :
		field_list = Material.objects.all().filter(report_id = 2)
		if request.method=='POST':
			form1 = editJobForm(request.POST)
			form2 = editSuspenceJobForm(request.POST)
  			if form1.is_valid and form2.is_valid():
				def clean_name(self):
        				cleaned_data = self.cleaned_data
					pay = cleaned_data.get('pay', '')
					check_number = cleaned_data.get('check_number', '')
					check_dd_date = cleaned_data.get('check_dd_date', '')
					sample = cleaned_data.get('sample', '')
				profile = form1.save(commit=False)
				profile.job_no = maxid
				profile.ip = request.META.get('REMOTE_ADDR')
				cl = editClientadd.objects.aggregate(Max('id'))
				clientid =cl['id__max']
				clid = editClientadd.objects.get(id = clientid)
				profile.client = clid
				report = Report.objects.get(id=2)
				profile.report_type = report
				profile.save()
        			form1.save_m2m()
				profile1 = form2.save(commit=False)	
				profile1.job_no = maxid	
				profile1.field = material
				jbmx = editJob.objects.aggregate(Max('id'))
				jobmax =jbmx['id__max']
				client = editJob.objects.get(id =jobmax)
				profile1.job = client
				sel_test = get_object_or_404(Test, pk=request.POST.get('test'))
				profile1.test = sel_test
				profile1.save()
				form2.save_m2m()
				return HttpResponseRedirect(reverse('Automation.tcc.views_ext.add_suspence_perf'))
		else:	
			form1 = editJobForm()
			form2 = editSuspenceJobForm()
		return render_to_response('tcc/performa/add_suspence.html', {"form1": form1,"test":test,'field_list':field_list,'payment':payment,'work':work,"report":report}, context_instance=RequestContext(request))

def gen_report_perf(request):
	"""
	** gen_report_perf **

	The jobs which are non suspence comes here. Depending on the material type, it is given a type: Routine or Institutional.
	"""

	mee = EditJob.objects.aggregate(Max('id'))
	minid =mee['id__max']
	client = EditJob.objects.get(id=minid)
	gen = ClientEditJob.objects.aggregate(Max('id'))
	genid =gen['id__max']
	clients = ClientEditJob.objects.get(id =genid)
	value = ClientEditJob.objects.values_list('test').filter(id=genid)
	values = Test.objects.values_list('cost',flat=True).filter(id__in = value)
	price = sum(values)
	unit_price = price*int(client.sample)
	job_no = client.job_no
	job = client
	mat = clients.material_id
	test = Test.objects.all().filter(material_id = mat)
	if mat == 1 or mat == 2 or mat == 3 or mat == 4 or mat == 5 :
		type = "ROUTINE"
	else:
		type = "INSTITUTIONAL"
	p = TestTotalPerf(unit_price=unit_price, job_no=job_no,mat=mat,type=type,job=job)
	p.save()
	return HttpResponseRedirect(reverse('Automation.tcc.views_ext.job_submit_perf'))

def add_suspence_perf(request):
	"""
	** add_suspence_perf **

	The calculation for the price of the material to be tested is calculated here.
	"""

	mee = editSuspenceJob.objects.aggregate(Max('id'))
	minid =mee['id__max']
	client = editSuspenceJob.objects.get(id=minid)
	value = editSuspenceJob.objects.values_list('test').filter(id=minid)
	values = Test.objects.get(id = value)
	if client.field.name == "Soil for BC":
		a = int(client.other) - 10
		b = int(client.other) - 20
		c = int(client.other) - 30
		if a > 0:
			unit_price = a*int(values.cost)+int(values.quantity)
		elif b > 0: 
			unit_price = b*int(values.cost)+int(values.quantity)
		elif c > 0:
			unit_price = c*int(values.cost)+int(values.quantity)
		else :
			unit_price = int(client.other)*int(values.cost)+int(values.quantity)
	else:
		unit_price = values.cost
	mx = editJob.objects.aggregate(Max('id'))
	maxid =mx['id__max']
	clients = editJob.objects.get(id=maxid)
	price = unit_price*int(clients.sample)
	job_no = clients.job_no
	job = clients
	mat = client.field_id
	test = Test.objects.all().filter(material_id = mat)
	if mat == 7 or mat == 8 or mat == 9 or mat == 10 or mat == 11 :
		type = "INSITUTIONAL"
	else:
		type = "ROUTINE"
	p = TestTotalPerf(unit_price=price, job_no=job_no,mat=mat,type=type,job=job)
	p.save()
	return HttpResponseRedirect(reverse('Automation.tcc.views_ext.job_submit_perf'))

def job_submit_perf(request):
	"""
	** job_submit_perf **

	The view to ensure that job is successfully saved.
	"""

	mee = EditJob.objects.aggregate(Max('id'))
	minid =mee['id__max']
	client = EditJob.objects.get(id=minid)
	value = client.report_type_id
	add = editClientadd.objects.aggregate(Max('id'))    # this is in case one clicks on adding more material into a job
	addid =add['id__max']
	more = editClientadd.objects.get(id=addid)
	moremat = more.client_id
	return render_to_response('tcc/performa/job_submit.html',{'mee':mee,'value':value,'moremat':moremat}, context_instance=RequestContext(request))

@login_required
def job_ok_perf(request):
	"""
	** job_ok_perf **

	This is to do the calculation of taxes on the total amount of a job. 
	"""
	
	id = EditJob.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	job_no = maxid
	value = TestTotalPerf.objects.values_list('unit_price',flat=True).filter(job_no=maxid)
	price = sum(value)
	from Automation.tcc.variable import *
	service_tax= round(servicetax *  price)
	education_tax = round(educationtax *  price)
	higher_education_tax = round(highereducationtax *  price)
	net_total =  price + higher_education_tax + education_tax + service_tax
	m = BillPerf(job_no = job_no, price = price, service_tax=service_tax, higher_education_tax=higher_education_tax,education_tax=education_tax,net_total=net_total)
	m.save()
	return render_to_response('tcc/performa/job_ok.html', {"maxid":maxid,}, context_instance=RequestContext(request))

@login_required
def billperf(request):
	"""
	** billperf **

	This shows the bill in HTML format. All the taxes, amount, materials tested are defined.
	"""

	id = EditJob.objects.aggregate(Max('id'))
	maxid =id['id__max']
	job = EditJob.objects.get(id = maxid)
	job_no = job.job_no
	client = job.client.client.first_name
	getjob = EditJob.objects.all().filter(job_no=job_no).values('site','clienteditjob__test__name','suspenceeditjob__test__name','clienteditjob__material_id')
	mat = TestTotalPerf.objects.all().values_list('mat',flat=True).filter(job_no=job_no)
	mate = Material.objects.all().filter(id__in = mat)
	price = TestTotalPerf.objects.all().filter(job_no=job_no)
	from Automation.tcc.variable import *
	bill = BillPerf.objects.get(job_no=job_no)
	title = get_object_or_404(Department, pk='1')
	address = get_object_or_404(Organisation, pk='1')
	servicetaxprint = servicetaxprint
	educationtaxprint = educationtaxprint
	highereducationtaxprint = highereducationtaxprint
	net_total1 = bill.net_total
	net_total_eng = num2eng(net_total1)
	template = {'job_no': job_no ,'net_total_eng':net_total_eng,'servicetaxprint':servicetaxprint,
	'highereducationtaxprint':highereducationtaxprint,'educationtaxprint':educationtaxprint,'client': client,'bill':bill, 'title':title,
	'address':address,'mate':mate,'job':job,'price':price,'net_total1':net_total1,'getjob':getjob,}
	return render_to_response('tcc/performa/bill.html', template , context_instance=RequestContext(request))

def search_job(request):
	"""
	** search_job **

	Search Job function searches the performa job, for which one wants to get information about or want to confirm that job.
	"""
	query =request.GET.get('q', '')
	if query:
		job = EditJob.objects.filter(job_no = query).values('id','client__client__first_name','client__client__address_1','client__client__city','clienteditjob__material__name','suspenceeditjob__field__name','site','testtotalperf__unit_price')
	else:	
		job =[]	
	return render_to_response('tcc/performa/searchjob.html',{'job':job,'query':query},context_instance=RequestContext(request))



def edit_work(request):
	"""
	** edit_work **

	Edit Work function is used to edit or delete a particular performa job id and then confirm the job.
	"""

	query =request.GET.get('id', '')
	job = EditJob.objects.get(id = query)
	if job.report_type_id == 1:
		clientjob = ClientEditJob.objects.get(job =query)
    	if request.method == "POST":
			jform = JobForm(request.POST)
			sform = ClientjobForm(request.POST)
			if jform.is_valid() and sform.is_valid():
				profile = jform.save(commit=False)
				profile.client_id = job.client_id
				id = Job.objects.aggregate(Max('job_no'))
				maxid =id['job_no__max']
				if maxid== None :
					maxid = 1
				else:
					maxid = maxid + 1
				profile.job_no = maxid
				profile.report_type_id =1
				profile.save()
				test = request.POST.getlist('test')
       				prof = sform.save(commit=False)
				getmax = Job.objects.aggregate(Max('id'))
				getjob =getmax['id__max']
				getj=Job.objects.get(id=getjob)
				prof.job = getj
				prof.save()
				sform.save_m2m()
				if profile.report_type == "1":
					return HttpResponseRedirect(reverse('Automation.tcc.views.add_suspence'))
				else :
					return HttpResponseRedirect(reverse('Automation.tcc.views.gen_report'))
			else:	
				jform = JobForm(instance=job)
				sform = ClientjobForm(instance=clientjob)
			return render_to_response('tcc/performa/edit_job.html', {'jform': jform,'sform':sform}, context_instance=RequestContext(request))
	else :
		suspencejob = SuspenceEditJob.objects.get(job = query)
		if request.method == "POST":
			jform = JobForm(request.POST)
        	sform = SuspencejobForm(request.POST)
        	if jform.is_valid() and sform.is_valid():
				profile = jform.save(commit=False)
				profile.client_id = job.client_id
				id = Job.objects.aggregate(Max('job_no'))
				maxid =id['job_no__max']
				if maxid== None :
					maxid = 1
				else:
					maxid = maxid + 1
				profile.job_no = maxid
				profile.save()
				prof = sform.save(commit=False)
				sel_test = get_object_or_404(Test, pk=request.POST.get('test'))
				prof.test = sel_test
				prof.job = profile.id
				prof.save()
				sform.save_m2m()
				return HttpResponseRedirect(reverse('Automation.tcc.views.add_suspence'))
        	else:	
			jform = JobForm(instance=job)
			sform = SuspencejobForm(instance=suspencejob)
		return render_to_response('tcc/performa/edit_job.html', {'jform': jform,'sform':sform},context_instance=RequestContext(request))
