#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ***Views.py***
# This file is used to create the views for the software. 
# It is the interface between the user interface, urls and database.
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
from django.db.models import F
from django import template
from tagging.models import Tag, TaggedItem
from Automation.tcc.choices import *
from Automation.tcc.models import *
from Automation.tcc.functions import *
from Automation.tcc.forms import *
from Automation.tcc.convert_function import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE FUNCTIONS HERE:::::::::::::::::::::#
@login_required
def index1(request):
	#'''
	#***This to have different views for different type of users
	#'''
	title = get_object_or_404(Department, pk='1')
	address = get_object_or_404(Organisation, pk='1')
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	if maxid== None :
		maxid = 1
	else:
		maxid = maxid + 1
	template = {'address':address,'title':title,'maxid':maxid,}
	if request.user.is_staff == 1 and request.user.is_active == 1 and request.user.is_superuser == 1:
		return render_to_response('index1.html',template,context_instance=RequestContext(request))
	elif request.user.is_staff == 0 and request.user.is_active == 1 and request.user.is_superuser == 0 :
		use = request.user
		client = UserProfile.objects.get(user_id = use)
		clients = client.id
		return render_to_response('index2.html',{'clients':clients}, context_instance=RequestContext(request))
	else:
		return render_to_response('index3.html', context_instance=RequestContext(request))


@login_required
def profile(request):
	#"""
	#***To fill personal details of user
	#"""
	if request.method == 'POST':
		form = UserProfileForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = request.user
			name = cd['name']
			address_1 = cd['address_1']
			address_2 = cd['address_2']
			city = cd['city']
			pin_code = cd['pin_code']
			state = cd['state']
			website = cd['website']
			contact_no = cd['contact_no']
			type_of_organisation = cd['type_of_organisation']
			'''pro = form.save(commit=False)
			pro.user = request.user
			pro.save()
			form.save()'''
			if request.user.is_staff == 1 and request.user.is_active == 1 and request.user.is_superuser == 0:
				UserProfile.objects.filter(user = user).update(name=name,address_1=address_1,address_2=address_2,city=city,pin_code=pin_code,state=state,website=website,contact_no=contact_no,type_of_organisation=type_of_organisation)
			else:
				form.save()
		id = UserProfile.objects.aggregate(Max('id'))
		maxid =id['id__max']		
		return render_to_response('tcc/new_client_ok.html', {'form': form,'maxid':maxid}, context_instance=RequestContext(request))
	else:
		form = UserProfileForm()
	return render_to_response('tcc/new_client.html', {'form': form}, context_instance=RequestContext(request))

@login_required
def performa(request):
	#"""
	#***Detail Veiw of data
	#"""
	user = User.objects.get(id=request.GET['id'])
	performa = UserProfile.objects.filter(user_id = user)
    	return render_to_response("tcc/detail.html", {'performa' : performa, 'user':user} )

@login_required
def previous(request):
	#"""
	#***Previous jobs entered by the user
	#"""
	title = get_object_or_404(Department, pk='1')
	client = request.user
	job = Job.objects.all().filter(client_id =client)
	return render_to_response('tcc/previous.html', {'job':job,'title':title}, context_instance=RequestContext(request))

@login_required
def material(request):
	#"""
	#***List the materials
	#"""
	material = Material.objects.all().order_by('name')
	return render_to_response('tcc/field.html', {'material':material,}, context_instance=RequestContext(request))

@login_required
def rate(request):
	#"""
	#***List the test to be performed on a material
	#"""
	lab = Lab.objects.all().order_by('code')
        field = Material.objects.all()
	material = Material.objects.get(id=request.GET['id'])
	test = Test.objects.filter(material_id = material)
	return render_to_response('tcc/test.html', {'lab':lab,'test':test,'material':material,'field':field}, context_instance=RequestContext(request))


@login_required
def selectfield(request):
	#"""
	#***List the type of work to be done i.e Lab or Field work
	#"""
	client =UserProfile.objects.get(id=request.GET['id'])
	add = Clientadd.objects.aggregate(Max('id'))    # this is in case one clicks on adding more material into a job
	addid =add['id__max']
	#devil = Clientadd.objects.get(id = addid)
	#dev = devil.id
	if addid == client:
		pass
	else:
		user = request.user
		m = Clientadd(client = client,user=user)
		m.save()
	report = Report.objects.all()
	mat = Material.objects.all()
	return render_to_response('tcc/typeofwork.html',{'report':report,'mat':mat}, context_instance=RequestContext(request))

@login_required
def select(request):
	#"""
	#***List down the materials or the field work depending on the selection of the type of work
	#"""	
	report = Report.objects.all()
	mat = Material.objects.all()
	material = Report.objects.get(id=request.GET['id'])
	field_list = Material.objects.all().filter(report_id =material)
	return render_to_response('tcc/tags.html',{'field_list':field_list,'report':report,'mat':mat}, context_instance=RequestContext(request))

@login_required
def add_job(request):
	#"""
	#***This helps the user to add the job
	#"""
	report = Report.objects.all()
	field_list = Material.objects.all().filter(report_id = 2)
	query =request.GET.get('q', '')
	id = Bill.objects.aggregate(Max('job_no'))
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
		if request.method=='POST':
			form1 = JobForm(request.POST)
			form2 = ClientJobForm(request.POST)
			if form1.is_valid and form2.is_valid():
				def clean_name(self):
        				cleaned_data = self.cleaned_data
					pay = cleaned_data.get('pay', '')
					check_number = cleaned_data.get('check_number', '')
					check_dd_date = cleaned_data.get('check_dd_date', '')
				profile = form1.save(commit=False)
				profile.job_no = maxid
				cl = Clientadd.objects.aggregate(Max('id'))
				clientid =cl['id__max']
				clid = Clientadd.objects.get(id = clientid)
				profile.client = clid
				report = Report.objects.get(id=1)
				profile.report_type = report
				profile.save()
				form1.save_m2m()
				test = request.POST.getlist('test')
       				profile1 = form2.save(commit=False)		
				profile1.material = material
				jbmx = Job.objects.aggregate(Max('id'))
				jobmax =jbmx['id__max']
				client = Job.objects.get(id =jobmax)
				profile1.job = client
				profile1.save()
				form2.save_m2m()
				if profile.report_type == "1":
					return HttpResponseRedirect(reverse('Automation.tcc.views.add_suspence'))
				else :
					return HttpResponseRedirect(reverse('Automation.tcc.views.gen_report'))
		else:	
			form1 = JobForm()
			form2 = ClientJobForm()
		return render_to_response('tcc/add_job.html', {"form1": form1,"test":test,'field_list':field_list,'payment':payment,'work':work,"report":report}, context_instance=RequestContext(request))
	else :
		if request.method=='POST':
			form1 = JobForm(request.POST)
			form2 = SuspenceJobForm(request.POST)
  			if form1.is_valid and form2.is_valid():
				def clean_name(self):
        				cleaned_data = self.cleaned_data
					pay = cleaned_data.get('pay', '')
					check_number = cleaned_data.get('check_number', '')
					check_dd_date = cleaned_data.get('check_dd_date', '')
				profile = form1.save(commit=False)
				profile.job_no = maxid
				cl = Clientadd.objects.aggregate(Max('id'))
				clientid =cl['id__max']
				clid = Clientadd.objects.get(id = clientid)
				profile.client = clid
				report = Report.objects.get(id=2)
				profile.report_type = report
				profile.save()
        			form1.save_m2m()
				profile1 = form2.save(commit=False)	
				profile1.job_no = maxid	
				profile1.field = material
				jbmx = Job.objects.aggregate(Max('id'))
				jobmax =jbmx['id__max']
				client = Job.objects.get(id =jobmax)
				profile1.job = client
				sel_test = get_object_or_404(Test, pk=request.POST.get('test'))
				profile1.test = sel_test
				profile1.save()
				form2.save_m2m()
				return HttpResponseRedirect(reverse('Automation.tcc.views.add_suspence'))
		else:	
			form1 = JobForm()
			form2 = SuspenceJobForm()
		return render_to_response('tcc/add_suspence.html', {"form1": form1,"test":test,'field_list':field_list,'payment':payment,'work':work,"report":report}, context_instance=RequestContext(request))
	
def add_suspence(request):
	#"""
	#***The jobs which are to be kept under suspence comes here 
	#"""
	mee = SuspenceJob.objects.aggregate(Max('id'))
	minid =mee['id__max']
	client = SuspenceJob.objects.get(id=minid)
	value = SuspenceJob.objects.values_list('test').filter(id=minid)
	values = Test.objects.get(id = value)
	if client.field_id == 5:
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
	elif client.field_id == 6:
		unit_price = values.cost
	mx = Job.objects.aggregate(Max('id'))
	maxid =mx['id__max']
	clients = Job.objects.get(id=maxid)
	job_no = clients.job_no
	mat = client.field_id
	test = Test.objects.all().filter(material_id = mat)
	if mat == 7 or mat == 8 or mat == 9 or mat == 10 or mat == 11 :
		type = "INSITUTIONAL"
	else:
		type = "ROUTINE"
	p = TestTotal(unit_price=unit_price, job_no=job_no,mat=mat,type=type)
	p.save()
	dist =  Distance.objects.aggregate(Max('id'))
	distid =dist['id__max']
	site = Distance.objects.get(id=distid)
	distance = 2*site.sandy
	report_type = "Suspence" 
	if distance < 100:
		rate = 1000
	else :
		rate = 10*distance
	sus = client
	m = Suspence(rate=rate, sus=sus,job_no=job_no)
	m.save()
	amt = Amount(job_no = job_no ,unit_price=unit_price,report_type = report_type)
	amt.save()
	return HttpResponseRedirect(reverse('Automation.tcc.views.job_submit'))

def gen_report(request):
	#"""
	#***The jobs which are non suspence comes here
	#"""
	mee = Job.objects.aggregate(Max('id'))
	minid =mee['id__max']
	client = Job.objects.get(id=minid)
	gen = ClientJob.objects.aggregate(Max('id'))
	genid =gen['id__max']
	clients = ClientJob.objects.get(id =genid)
	value = ClientJob.objects.values_list('test').filter(id=genid)
	values = Test.objects.values_list('cost',flat=True).filter(id__in = value)
	unit_price = sum(values)
	job_no = client.job_no
	mat = clients.material_id
	test = Test.objects.all().filter(material_id = mat)
	if mat == 1 or mat == 2 or mat == 3 or mat == 4 or mat == 5 :
		type = "ROUTINE"
	else:
		type = "INSTITUTIONAL"
	p = TestTotal(unit_price=unit_price, job_no=job_no,mat=mat,type=type)
	p.save()
	if client.pay == "CASH":
		report_type = "General_report"
	else:
		report_type = "Suspence"
	from Automation.tcc.variable import *
	college_income = round(collegeincome * unit_price / 100.00)
	admin_charge = round(admincharge * unit_price / 100.00)
	temp =  unit_price - college_income - admin_charge
	ratio1 = ratio1(type)
	ratio2 = ratio2(type)
	consultancy_asst = round(ratio1 * temp / 100)
	development_fund = round(ratio2 * temp / 100)
	m = Amount(job_no = job_no ,unit_price=unit_price,development_fund=development_fund, college_income = 	college_income, admin_charge=admin_charge, consultancy_asst=consultancy_asst,report_type = report_type)
	m.save()
	return HttpResponseRedirect(reverse('Automation.tcc.views.job_submit'))

def job_submit(request):
	#"""
	#***The view to ensure that job is successfully saved
	#"""
	if request.user.is_staff == 0 and request.user.is_active == 1 and request.user.is_superuser == 0 :
		use = request.user
		client = UserProfile.objects.get(user_id = use)
		clients = client.id
	if request.user.is_staff == 1 and request.user.is_active == 1 and request.user.is_superuser == 1:
		id = UserProfile.objects.aggregate(Max('id'))
		clients =id['id__max']
	mee = Job.objects.aggregate(Max('id'))
	minid =mee['id__max']
	client = Job.objects.get(id=minid)
	value = client.report_type_id
	add = Clientadd.objects.aggregate(Max('id'))    # this is in case one clicks on adding more material into a job
	addid =add['id__max']
	more = Clientadd.objects.get(id=addid)
	moremat = more.client_id
	return render_to_response('tcc/job_submit.html',{'mee':mee,'clients':clients,'value':value,'moremat':moremat}, context_instance=RequestContext(request))
	
@login_required
def job_ok(request):
	#"""
	#***This is to do the calculation of taxes 
	#"""
	material =request.GET.get('id', '')
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	job_no = maxid
	value = TestTotal.objects.values_list('unit_price',flat=True).filter(job_no=maxid)
	price = sum(value)
	from Automation.tcc.variable import *
	service_tax= round(servicetax *  price)
	education_tax = round(educationtax *  price)
	higher_education_tax = round(highereducationtax *  price)
	net_total =  price + higher_education_tax + education_tax + service_tax
	m = Bill(job_no = job_no, price = price, service_tax=service_tax, higher_education_tax=higher_education_tax,education_tax=education_tax,net_total=net_total)
	m.save()
	return render_to_response('tcc/job_ok.html', {"maxid":maxid,'material':material,'maxid':maxid}, context_instance=RequestContext(request))

@login_required
def bill(request):
	#"""
	#***This shows the bill in HTML format
	#"""
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	job_no = maxid
	client = Job.objects.all().values_list('client_id',flat=True).filter(job_no=job_no)
	cli = Clientadd.objects.all().values_list('client_id',flat=True).filter(id__in = client)
	clients = UserProfile.objects.all().get(id__in = cli)
	job = Job.objects.all().filter(job_no=maxid)
	mat = TestTotal.objects.all().values_list('mat',flat=True).filter(job_no=maxid)
	mate = Material.objects.all().filter(id__in = mat)
	price = TestTotal.objects.all().filter(job_no=maxid)
	from Automation.tcc.variable import *
	bill = Bill.objects.get(job_no=maxid)
	title = get_object_or_404(Department, pk='1')
	address = get_object_or_404(Organisation, pk='1')
	servicetaxprint = servicetaxprint
	educationtaxprint = educationtaxprint
	highereducationtaxprint = highereducationtaxprint
	net_total1 = bill.net_total
	net_total_eng = num2eng(net_total1)
	template = {'job_no': job_no ,'bill_no':bill.job_no,'net_total_eng':net_total_eng,'servicetaxprint':servicetaxprint,
	'highereducationtaxprint':highereducationtaxprint,'educationtaxprint':educationtaxprint,'clients': clients,'bill':bill, 'title':title,
	'address':address,'mate':mate,'job':job,'price':price,'net_total1':net_total1}
	return render_to_response('tcc/bill.html', template , context_instance=RequestContext(request))

@login_required
def receipt_report(request):
	#"""
	#***View the Receipt In Html format
	#"""
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	job_no = maxid
	price = TestTotal.objects.all().filter(job_no=maxid)
	client = Job.objects.all().values_list('client_id',flat=True).filter(job_no=job_no)
	cli = Clientadd.objects.all().values_list('client_id',flat=True).filter(id__in = client)
	clients = UserProfile.objects.all().get(id__in = cli)
	job = Job.objects.all().filter(job_no=maxid)
	mat = TestTotal.objects.all().values_list('mat',flat=True).filter(job_no=maxid)
	mate = Material.objects.all().filter(id__in = mat)
	total = Bill.objects.all().filter(job_no=maxid)
	bill = Bill.objects.get(job_no=job_no)
	title = get_object_or_404(Department, pk='1')
	address = get_object_or_404(Organisation, pk='1')
	net_total1 = bill.net_total
	net_total_eng = num2eng(net_total1)
	template = {'job_no': job_no ,'mate':mate, 'net_total_eng':net_total_eng,'type':type,'price': price,'title':title, 'address':address,'clients':clients,'total':total,'job':job}
	return render_to_response('tcc/receipt.html', template , context_instance=RequestContext(request))

def g_report(request):
	#"""
	#***Shows the total reports generated
	#"""
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	job_no = maxid
	amt = Amount.objects.all().filter(job_no=maxid)
	return render_to_response('tcc/get_report.html', {'job_no':job_no,'amt':amt} , context_instance=RequestContext(request))	
	
@login_required	
def rep(request):
	#"""
	#***Displays the voucher in html format
	#"""
	from Automation.tcc.variable import *
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	job_no = maxid
	query =request.GET.get('id')
	client = TestTotal.objects.all().get(id =query)
	amount = Amount.objects.all().get(id =query)
	user = Job.objects.all().get(id=query)
	users = user.client_id
	clients = Clientadd.objects.all().get(id = users)
	cli = clients.client_id
	pro = UserProfile.objects.all().get(id=cli )
	use = ClientJob.objects.all().get(job_id=query)
	mat = use.material_id
	mate = Material.objects.all().get(id = mat)
	lab = mate.lab_id
	staff = Staff.objects.all().filter(lab_id = lab)
	title = get_object_or_404(Department, pk='1')
	address = get_object_or_404(Organisation, pk='1')
	con_type = client.type
	ratio1 = ratio1(con_type)
	ratio2 = ratio2(con_type)
	job_no = amount.job_no
	net_total1 = amount.unit_price
	net_total_eng = num2eng(net_total1)
	#teachers = Teachers.objects.all().filter(lab=lab).order_by('id')
	retrieve()
	template = {'job_no': job_no,'net_total_eng':net_total_eng,'title':title,'address':address, 'servicetaxprint':servicetaxprint,
	'highereducationtaxprint':highereducationtaxprint,'educationtaxprint':educationtaxprint,'client': client,'amount':amount,'con_type':con_type, 'ratio1':ratio1 ,'ratio2':ratio2,'collegeincome':collegeincome,'admincharge' : admincharge,'pro':pro,'mate':mate,'staff':staff, }
	return render_to_response('tcc/report.html', template , context_instance=RequestContext(request))


def transport(request):
	#"""
	#***View of Transport Bill
	#"""
	if request.method == 'POST':
		form = TransportForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			job_no =cd['job_no']
			test_date =cd['test_date']
			kilometer =cd['kilometer']
			date =cd ['date']
			id = Transport.objects.aggregate(Max('id'))
			maxid =id['id__max']
			if maxid== None :
				maxid = 1
			else:
				maxid = maxid + 1
			bill_no = maxid
			#rate = cd ['rate']
			form.save()
			Transport.objects.filter(job_no = job_no).update( bill_no = maxid )
			data = {'job_no':job_no,'rate':rate, 'kilometer': kilometer,'bill_no':bill_no,'test_date':test_date}
			return render_to_response('tcc/trans.html', data,  context_instance=RequestContext(request))
	else:
		form = TransportForm()
	return render_to_response('tcc/client.html', {'form': form}, context_instance=RequestContext(request))

def transport_bill(request):
	#"""
	#***Final Report of Transport Bill
	#"""
	transport_old = Transport.objects.get(job_no=request.GET['job_no'])
	client = ClientJob.objects.get(job_no=request.GET['job_no'])
	kilometer = transport_old.kilometer
	temp = [0,0,0,0,0,0,0,0,0,0]
	range = kilometer.split(',')
	i=0
	while i < len(range):
		temp[i] = range[i]
		i+=1
	rate = transport_old.rate
	amount1 = int(temp[0])*rate
	amount2 = int(temp[1])*rate
	amount3 = int(temp[2])*rate
	amount4 = int(temp[3])*rate
	amount5 = int(temp[4])*rate
	amount6 = int(temp[5])*rate
	amount7 = int(temp[6])*rate
	amount8 = int(temp[7])*rate
	amount9 = int(temp[8])*rate
	amount10 = int(temp[9])*rate
	total = amount1 + amount2 + amount3 + amount4 + amount5 + amount6 + amount7 + amount8 + amount9 + amount10
	all_amounts = amount1,amount2,amount3,amount4,amount5,amount6,amount7,amount8,amount9,amount10
	Transport.objects.filter(job_no = transport_old.job_no).update( total = total, amounts = all_amounts )
	transport = Transport.objects.get(job_no=transport_old.job_no)
	title = get_object_or_404(Variable, pk='1')
	sub_title = get_object_or_404(Variable, pk='2')
	sign = get_object_or_404(Variable, pk='3')
	vehical_no = get_object_or_404(Variable, pk='4')
	template ={'transport':transport,'title':title,'sub_title':sub_title, 'vehical_no':vehical_no ,'client':client,'sign':sign}
	return render_to_response('tcc/transportbill.html', template , context_instance=RequestContext(request))

def distance(request):
	#"""
	#***This is for calculation of distance of the site on the map
	#"""
	mee = Job.objects.aggregate(Max('id'))
	jobid =mee['id__max']
	if jobid== None :
		jobid = 1
	else:
		jobid = jobid +1
	if request.method =='POST':
		form = DistanceForm(request.POST)
  		if form.is_valid():
			cd = form.cleaned_data
			#end = cd['end']
			sandy = cd['sandy']
			profile = form.save(commit=False)
			profile.job = jobid
			profile.save()
			return render_to_response('tcc/map_ok.html', context_instance=RequestContext(request))
		
	else:
  		form = DistanceForm()
	return render_to_response('tcc/siteinmap.html', {"form": form,}, context_instance=RequestContext(request))

def suspence_clearance(request):
	#"""
	#***Suspence Clearance is done here 
	#"""
	if request.method == 'POST':
		form = SuspenceClearence(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			job_no =cd['job_no']
			labour_charge =cd['labour_charge']
			car_taxi_charge =cd['car_taxi_charge']
			boring_charge_external=cd['boring_charge_external']
			boring_charge_internal=cd['boring_charge_internal']
			lab_testing_staff=cd['lab_testing_staff']
			field_testing_staff =cd ['field_testing_staff']
			#suspence_bill_no =cd['suspence_bill_no']
			Suspence.objects.filter(job_no = job_no).update(labour_charge=labour_charge,boring_charge_external=boring_charge_external, 
			boring_charge_internal= boring_charge_internal,field_testing_staff=field_testing_staff,car_taxi_charge=car_taxi_charge,lab_testing_staff=lab_testing_staff)
			data = {'job_no' :job_no, 'labour_charge':labour_charge,'boring_charge_external':boring_charge_external,
			'boring_charge_internal': boring_charge_internal,'car_taxi_charge':car_taxi_charge,'lab_testing_staff':lab_testing_staff}
			return render_to_response('tcc/suspence_clearence_ok.html', data, context_instance=RequestContext(request))
	else:
		form = SuspenceClearence()
		return render_to_response('tcc/new_client.html', {'form': form}, context_instance=RequestContext(request))

def suspence(request):
	return render_to_response('tcc/add_job2.html', context_instance=RequestContext(request))

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query) |
            Q(type_of_organisation__icontains=query)
        )
        results = UserProfile.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("tcc/search.html", {
        "results": results,
        "query": query
    })


def suspence_clearence_report(request):
	transport = Transport.objects.get(job_no=request.GET['job_no'])
	client = ClientJob.objects.get(job_no=request.GET['job_no'])
	amount = Amount.objects.get(job_no=request.GET['job_no'])
	suspence = Suspence.objects.get(job_no=request.GET['job_no'])
	lab_staff = suspence.lab_testing_staff
        t1=0
        temp = [0,0,0,0,0,0,0,0,0,0]
	range = lab_staff.split(',')
	i=0
	while i < len(range):
		temp[i] = range[i]
		i+=1
	amount1 = temp[0]
	amount2 = temp[1]
	amount3 = temp[2]
	amount4 = temp[3]
	amount5 = temp[4]
	amount6 = temp[5]
	amount7 = temp[6]
	amount8 = temp[7]
	amount9 = temp[8]
	amount10 = temp[9]
	
	field_staff = suspence.field_testing_staff
	temp = [0,0,0,0,0,0,0,0,0,0]
	range = field_staff.split(',')
	i=0
	while i < len(range):
		temp[i] = range[i]
		i+=1
	amounts1 = temp[0]
	amounts2 = temp[1]
	amounts3 = temp[2]
	amounts4 = temp[3]
	amounts5 = temp[4]
	amounts6 = temp[5]
	amounts7 = temp[6]
	amounts8 = temp[7]
	amounts9 = temp[8]
	amounts10 = temp[9]
	teachers =Teachers.objects.all().filter(Q(code=amount1)| Q(code=amount2) | Q(code=amount3) 
	| Q(code=amount4) | Q(code=amount5) | Q(code=amount6) | Q(code=amount7)| Q(code=amount8)
	| Q(code=amount9) | Q(code=amount10)| Q(code=amounts1)| Q(code=amounts2) | Q(code=amounts3) 
	| Q(code=amounts4) | Q(code=amounts5) | Q(code=amounts6) | Q(code=amounts7)| Q(code=amounts8)
	| Q(code=amounts9) | Q(code=amounts10)).order_by('id')
	title = get_object_or_404(Variable, pk='1')
	sub_title = get_object_or_404(Variable, pk='2')
	sign = get_object_or_404(Variable, pk='3')
        tada_temp = Ta_Da.objects.filter(job_no=client.job_no).aggregate(Sum('tada_amount'))
	tada_sum= int(tada_temp['tada_amount__sum']) 
	field_testing_staff = Ta_Da.objects.filter(job_no=client.job_no)
	temp = suspence.labour_charge+transport.total+suspence.boring_charge_external+suspence.car_taxi_charge
	balance= amount.total - (tada_sum + temp + suspence.boring_charge_internal)
	college_income = round(collegeincome * balance / 100.00)
	admin_charge = round(admincharge * balance / 100.00)
	work_charge = round(workcharge * balance / 100.00)
	balance_temp = balance - college_income - admin_charge -work_charge
	from TCC11_12.automation.functions import *
	con_type = client.type_of_consultancy
	ratio1 = ratio1(con_type)
	ratio2 = ratio2(con_type)
	consultancy_asst = round(ratio1 * balance_temp / 100)
	development_fund = round(ratio2 * balance_temp / 100)
	net_total1 = amount.balance
	net_balance_eng = num2eng(net_total1)
	retrieve()
	Suspence.objects.filter(job_no = client.job_no).update( work_charge = work_charge)
	Amount.objects.filter(job_no = client.job_no).update( college_income = college_income, admin_charge=admin_charge,
	consultancy_asst=consultancy_asst, development_fund=development_fund )
	data = {'transport' : transport, 'net_balance_eng':net_balance_eng,'teachers':teachers,'servicetaxprint':servicetaxprint,
	'highereducationtaxprint':highereducationtaxprint,'educationtaxprint':educationtaxprint,'ratio1':ratio1 ,'field_testing_staff':field_testing_staff,
	'job_no':client.job_no,'ratio2':ratio2,'other':temp,'collegeincome':collegeincome,'admincharge' : admincharge ,'client' :client, 'amount': amount,
	'suspence':suspence,'tada_sum':tada_sum,'sign':sign,'title':title,'sub_title':sub_title,}
	return render_to_response('automation/suspence_clearence_report.html', data , context_instance=RequestContext(request))

def search_jobid(request):
	return render_to_response('tcc/searchjob.html',context_instance=RequestContext(request))
	
def edit_job(request):
	query =request.GET.get('q', '')
	job = Job.objects.get(id = query)
	amt = Amount.objects.get(id = query)
	if amt.report_type == "Suspence":
		suspencejob = SuspenceJob.objects.get(job_id = query)
    		if request.method == "POST":
			jform = editJobForm(request.POST, instance=job)
        		sform = editSuspenceJobForm(request.POST, instance=suspencejob)
        		if jform.is_valid() and sform.is_valid():
				jform.save()
            			sform.save()
            			return render_to_response('tcc/succes.html',context_instance=RequestContext(request))
        	else:	
			jform = editJobForm(instance=job)
			sform = editSuspenceJobForm(instance=suspencejob)
		return render_to_response('tcc/edit_job.html', {'jform': jform,'sform':sform},context_instance=RequestContext(request))
	else:
		clientjob = ClientJob.objects.get(job_id = query)
    		if request.method == "POST":
			jform = editJobForm(request.POST, instance=job)
        		sform = editClientJobForm(request.POST, instance=clientjob)
        		if jform.is_valid() and sform.is_valid():
				jform.save()
            			sform.save()
            			return render_to_response('tcc/succes.html',context_instance=RequestContext(request))
        	else:	
			jform = editJobForm(instance=job)
			sform = editClientJobForm(instance=clientjob)
		return render_to_response('tcc/edit_job.html', {'jform': jform,'sform':sform},context_instance=RequestContext(request))

def fillbank(request):
	if request.method == "POST":
		form = BankdetailsForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('tcc/succes.html',context_instance=RequestContext(request))
	else:
		form = BankdetailsForm()
	return render_to_response('tcc/bank.html', {'form': form},context_instance=RequestContext(request))

