"""
%% views.py %%

This file is used to create the views for the software. 
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
from Auto.tcc.choices import *
from Auto.tcc.models import *
from Auto.tcc.functions import *
from Auto.tcc.forms import *
from Auto.tcc.convert_function import *
from django.core.mail import send_mail
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE FUNCTIONS HERE:::::::::::::::::::::#

def material_site():
	material = Material.objects.all().filter(report=1)
	field = Material.objects.all().filter(report=2)
	title = Department.objects.get(id=1)	
	address = get_object_or_404(Organisation, pk='1')
	template={'material':material,'field':field,'title':title,'address':address}
	return template

tmp =material_site()

def index1(request):
	'''
	** index1 **

	This is to have different views for different type of users. Like here we have 2 types of users :one which is active,staff and is 		superuser is the superuser of the software. The one who is just active is the normal user. Depending upon there status different
	views are created in index1.html and index2.html respectively. 
	'''

	
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	if maxid== None :
		maxid = 1
	else:
		maxid = maxid + 1
	template = {'maxid':maxid,}
	if request.user.is_staff == 1 and request.user.is_active == 1 and request.user.is_superuser == 1:
		return render_to_response('index1.html',dict(template.items() + tmp.items()),context_instance=RequestContext(request))
	elif request.user.is_staff == 0 and request.user.is_active == 1 and request.user.is_superuser == 0 :
		try:
   			use = request.user
			client = UserProfile.objects.get(user_id = use)
			clients = client.id
			template ={'clients':clients,'maxid':maxid,}
			return render_to_response('index2.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))
		except UserProfile.DoesNotExist:
   			return render_to_response('index2.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))
	else:
		return render_to_response('index.html', tmp ,context_instance=RequestContext(request))


@login_required
def profile(request):
	"""
	** profile **

	This function is used to make the user fill the personal detail. If a normal user fills the detail, then his userprofile           	 	get updated, but if a superuser creates a profile that means he/she is registering the client (and registration of client 		can be done as many times as possible.
	"""
	tmp = material_site()
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
			if request.user.is_staff == 0 and request.user.is_active == 1 and request.user.is_superuser == 0:
				UserProfile.objects.filter(user = user).update(name=name,address_1=address_1,address_2=address_2,city=city,pin_code=pin_code,state=state,website=website,contact_no=contact_no,type_of_organisation=type_of_organisation)
			else:
				pro = UserProfile(name=name,address_1=address_1,address_2=address_2,city=city,pin_code=pin_code,state=state,website=website,contact_no=contact_no,type_of_organisation=type_of_organisation,user=user)
				pro.save()
			id = UserProfile.objects.aggregate(Max('id'))
			maxid =id['id__max']	
			x = {'form': form,'maxid':maxid,}	
			return render_to_response('tcc/client/profileadded.html',dict(x.items() + tmp.items()) , context_instance=RequestContext(request))
	else:
		form = UserProfileForm()
	form = {'form':form}
	if request.user.is_staff == 1 and request.user.is_active == 1 and request.user.is_superuser == 1:
		return render_to_response('tcc/new_client.html',dict(form.items() + tmp.items()),context_instance=RequestContext(request))
	else :
		return render_to_response('tcc/client/addprofile.html', dict(form.items() + tmp.items()), context_instance=RequestContext(request))

@login_required
def performa(request):
	"""
	** performa **

	Gives the detailed view of profile filled by client. Just the data is extracted from UserProfile table.
	"""

	user = User.objects.get(id=request.GET['id'])
	performa = UserProfile.objects.filter(user_id = user)
	temp = {'performa' : performa, 'user':user}
	return render_to_response("tcc/client/detail.html", dict(temp.items() + tmp.items()), context_instance=RequestContext(request) )

@login_required
def previous(request):
	"""
	** previous **

	This function lists the previous jobs of the user who have logged in the software. Just filters the jobs done by user from the 		Job table.
	"""

	title = get_object_or_404(Department, pk='1')
	client = request.user
	job = Job.objects.all().filter(client_id =client)
	return render_to_response('tcc/previous.html', {'job':job,'title':title}, context_instance=RequestContext(request))

@login_required
def material(request):
	"""
	** material **

	Material Function lists all the materials or field works. These are the links, depending on the selection of material selected, there 		tests are filtered.
	"""
	material = Material.objects.all().order_by('name')
	return render_to_response('tcc/field.html', tmp, context_instance=RequestContext(request))


def rate(request):
	"""
	** rate **

	Rate Function gets the value of material(that was selected previously) from the url and based on that material, the tests are listed.
	"""
	
	lab = Lab.objects.all().order_by('code')
	mat = Material.objects.get(id=request.GET['id'])
	test = Test.objects.filter(material_id = mat)
	temp = {'lab':lab,'test':test,'mat':mat,}
	if request.user.is_staff == 1 and request.user.is_active == 1 and request.user.is_superuser == 1:
		return render_to_response('tcc/test.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))
	else :
		return render_to_response('tcc/test_nonclient.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))

@login_required
def selectfield(request):
	"""
	** selectfield **

	List the type of work to be done i.e Lab or Field work.
	"""
	
	tmp = material_site()
	client =UserProfile.objects.get(id=request.GET['id'])
	add = Clientadd.objects.aggregate(Max('id'))    # this is in case one clicks on adding more material into a job
	addid =add['id__max']
	if addid == client:
		pass
	else:
		user = request.user
		m = Clientadd(client = client,user=user)
		m.save()
	report = Report.objects.all()
	mat = Material.objects.all()
	temp = {'report':report,'mat':mat}
	return render_to_response('tcc/typeofwork.html',dict(temp.items() + tmp.items()), context_instance=RequestContext(request))

@login_required
def select(request):
	"""
	** select **

	List down the materials or the field work depending on the selection of the type of work i.e lab or Field work.
	"""	
	tmp = material_site()
	report = Report.objects.all()
	mat = Material.objects.all()
	material = Report.objects.get(id=request.GET['id'])
	field_list = Material.objects.all().filter(report_id =material)
	temp = {'field_list':field_list,'report':report,'mat':mat}
	return render_to_response('tcc/tags.html',dict(temp.items() + tmp.items()), context_instance=RequestContext(request))

@login_required
def add_job(request):
	"""
	** add_job **

	This helps the user to add the job. Depending upon the material selected the tests are listed then. Two forms are defined in a single 		template file, so that there data get stored in different tables one after the other.
	"""
	
	
	report = Report.objects.all()
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
		field_list = Material.objects.all().filter(report_id = 1)
		if request.method=='POST':
			form1 = JobForm(request.POST)
			form2 = ClientJobForm(request.POST)
			if form1.is_valid and form2.is_valid():
				def clean_name(self):
        				cleaned_data = self.cleaned_data
					pay = cleaned_data.get('pay', '')
					check_number = cleaned_data.get('check_number', '')
					check_dd_date = cleaned_data.get('check_dd_date', '')
					sample = cleaned_data.get('sample', '')
					letter_no = cleaned_data.get('letter_no','')
				profile = form1.save(commit=False)
				profile.job_no = maxid
				profile.ip = request.META.get('REMOTE_ADDR')
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
					return HttpResponseRedirect(reverse('Auto.tcc.views.add_suspence'))
				else :
					return HttpResponseRedirect(reverse('Auto.tcc.views.gen_report'))
		else:	
			form1 = JobForm()
			form2 = ClientJobForm()
		temp = {"form1": form1,"test":test,'field_list':field_list,'payment':payment,'work':work,"report":report}
		return render_to_response('tcc/add_job.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))
	else :
		field_list = Material.objects.all().filter(report_id = 2)
		if request.method=='POST':
			form1 = JobForm(request.POST)
			form2 = SuspenceJobForm(request.POST)
  			if form1.is_valid and form2.is_valid():
				def clean_name(self):
        				cleaned_data = self.cleaned_data
					pay = cleaned_data.get('pay', '')
					check_number = cleaned_data.get('check_number', '')
					check_dd_date = cleaned_data.get('check_dd_date', '')
					sample = cleaned_data.get('sample', '')
					letter_no = cleaned_data.get('letter_no','')
				profile = form1.save(commit=False)
				profile.job_no = maxid
				profile.ip = request.META.get('REMOTE_ADDR')
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
				return HttpResponseRedirect(reverse('Auto.tcc.views.add_suspence'))
		else:	
			form1 = JobForm()
			form2 = SuspenceJobForm()
		temp ={"form1": form1,"test":test,'field_list':field_list,'payment':payment,'work':work,"report":report}
		return render_to_response('tcc/add_suspence.html',dict(temp.items() + tmp.items()) , context_instance=RequestContext(request))
	
def add_suspence(request):
	"""
	** add_suspence **

	The calculation for the price of the material to be tested is calculated here.
	"""

	mee = SuspenceJob.objects.aggregate(Max('id'))
	minid =mee['id__max']
	client = SuspenceJob.objects.get(id=minid)
	value = SuspenceJob.objects.values_list('test').filter(id=minid)
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
	mx = Job.objects.aggregate(Max('id'))
	maxid =mx['id__max']
	clients = Job.objects.get(id=maxid)
	price = unit_price*int(clients.sample)
	balance = price - int(clients.tds)
	job_no = clients.job_no
	job = clients
	mat = client.field_id
	test = Test.objects.all().filter(material_id = mat)
	if mat == 7 or mat == 8 or mat == 9 or mat == 10 or mat == 11 :
		type = "INSITUTIONAL"
	else:
		type = "ROUTINE"
	p = TestTotal(unit_price=price, job_no=job_no,mat=mat,type=type,job=job,balance=balance)
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
	m = Suspence(rate=rate, sus=sus,job=job)
	m.save()
	amt = Amount(job = job ,unit_price=price,report_type = report_type,)
	amt.save()
	return HttpResponseRedirect(reverse('Auto.tcc.views.job_submit'))

def gen_report(request):
	"""
	** gen_report **

	The jobs which are non suspence comes here. Depending on the material type, it is given a type: Routine or Institutional.
	"""

	mee = Job.objects.aggregate(Max('id'))
	minid =mee['id__max']
	client = Job.objects.get(id=minid)
	gen = ClientJob.objects.aggregate(Max('id'))
	genid =gen['id__max']
	clients = ClientJob.objects.get(id =genid)
	value = ClientJob.objects.values_list('test').filter(id=genid)
	values = Test.objects.values_list('cost',flat=True).filter(id__in = value)
	price = sum(values)
	unit_price = price*int(client.sample)
	balance = unit_price-int(client.tds)
	job_no = client.job_no
	job = client
	mat = clients.material_id
	test = Test.objects.all().filter(material_id = mat)
	if mat == 1 or mat == 2 or mat == 3 or mat == 4 or mat == 5 :
		type = "ROUTINE"
	else:
		type = "INSTITUTIONAL"
	p = TestTotal(unit_price=unit_price, job_no=job_no,mat=mat,type=type,job=job,balance=balance)
	p.save()
	if client.pay == "CASH":
		report_type = "General_report"
	else:
		report_type = "Suspence"
	from Auto.tcc.variable import *
	college_income = round(collegeincome * unit_price / 100.00)
	admin_charge = round(admincharge * unit_price / 100.00)
	temp =  unit_price - college_income - admin_charge
	ratio1 = ratio1(type)
	ratio2 = ratio2(type)
	consultancy_asst = round(ratio1 * temp / 100)
	development_fund = round(ratio2 * temp / 100)
	m = Amount(job = job ,unit_price=unit_price,development_fund=development_fund, college_income =college_income, admin_charge=admin_charge, consultancy_asst=consultancy_asst,report_type = report_type)
	m.save()
	return HttpResponseRedirect(reverse('Auto.tcc.views.job_submit'))

def job_submit(request):
	"""
	** job_submit **

	The view to ensure that job is successfully saved.
	"""
	
	tmp = material_site()
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
	temp = {'mee':mee,'clients':clients,'value':value,'moremat':moremat}
	return render_to_response('tcc/job_submit.html',dict(temp.items() + tmp.items()), context_instance=RequestContext(request))
	
@login_required
def job_ok(request):
	"""
	** job_ok **

	This is to do the calculation of taxes on the total amount of a job. 
	"""

	tmp = material_site()
	material =request.GET.get('id', '')
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	job_no = maxid
	value = TestTotal.objects.values_list('unit_price',flat=True).filter(job_no=maxid)
	price = sum(value)
	from Auto.tcc.variable import *
	service_tax= round(servicetax *  price)
	education_tax = round(educationtax *  price)
	higher_education_tax = round(highereducationtax *  price)
	net_total =  price + higher_education_tax + education_tax + service_tax
	m = Bill(job_no = job_no, price = price, service_tax=service_tax, higher_education_tax=higher_education_tax,education_tax=education_tax,net_total=net_total)
	m.save()
	temp = {"maxid":maxid,'material':material,'maxid':maxid}
	return render_to_response('tcc/job_ok.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))

@login_required
def bill(request):
	"""
	** bill **

	This shows the bill in HTML format. All the taxes, amount, materials tested are defined.
	"""

	try :
		job =Job.objects.get(id=request.GET['id'])
		job_no=job.job_no
	except Exception:
		id = Job.objects.aggregate(Max('id'))
		maxid =id['id__max']
		job = Job.objects.get(id = maxid)
		job_no = job.job_no
	client = job.client.client.first_name
	getjob = Job.objects.all().filter(job_no=job_no).values('clientjob__test__name','suspencejob__test__name','clientjob__material_id',).distinct()
	getadd = Job.objects.all().filter(job_no=job_no).values('client__client__first_name','client__client__middle_name','client__client__last_name','client__client__address_1','client__client__city','client__client__state').distinct()
	getsite =Job.objects.all().filter(job_no=job_no).values('site')
	mat = TestTotal.objects.all().values_list('mat',flat=True).filter(job_no=job_no)
	mate = Material.objects.all().filter(id__in = mat)
	price = TestTotal.objects.all().filter(job_no=job_no)
	from Auto.tcc.variable import *
	bill = Bill.objects.get(job_no=job_no)
	title = get_object_or_404(Department, pk='1')
	address = get_object_or_404(Organisation, pk='1')
	servicetaxprint = servicetaxprint
	educationtaxprint = educationtaxprint
	highereducationtaxprint = highereducationtaxprint
	net_total1 = bill.net_total
	net_total_eng = num2eng(net_total1)
	template = {'job_no': job_no ,'net_total_eng':net_total_eng,'servicetaxprint':servicetaxprint,
	'highereducationtaxprint':highereducationtaxprint,'educationtaxprint':educationtaxprint,'client': client,'bill':bill, 'title':title,
	'address':address,'mate':mate,'job':job,'price':price,'net_total1':net_total1,'getjob':getjob,'getadd':getadd,'getsite':getsite}
	return render_to_response('tcc/bill.html', template , context_instance=RequestContext(request))

@login_required
def receipt_report(request):
	"""
	** receipt_report **

	View the Receipt In Html format. This shows the material tested for the client and total amount for it.
	"""

	try :
		job =Job.objects.get(id=request.GET['id'])
		job_no=job.job_no
	except Exception:
		id = Job.objects.aggregate(Max('id'))
		maxid =id['id__max']
		job = Job.objects.get(id = maxid)
		job_no = job.job_no
	client = job.client.client.first_name
	mat = TestTotal.objects.all().values_list('mat',flat=True).filter(job_no=job_no)
	mate = Material.objects.all().filter(id__in = mat)
	bill = Bill.objects.get(job_no=job_no)
	net_total1 = bill.net_total
	net_total_eng = num2eng(net_total1)
	template = {'mate':mate, 'net_total_eng':net_total_eng,'client':client,'bill':bill,'job':job}
	return render_to_response('tcc/receipt.html', template , context_instance=RequestContext(request))

def g_report(request):
	"""
	** g_report **

	g_report Function shows the total vouchers generated in a job.
	"""

	tmp = material_site()
	id = Job.objects.aggregate(Max('job_no'))
	maxid =id['job_no__max']
	amt = Job.objects.filter(job_no = maxid)
	temp =  {'amt':amt}
	return render_to_response('tcc/get_report.html',dict(temp.items() + tmp.items()) , context_instance=RequestContext(request))	
	
@login_required	
def rep(request):
	"""
	** rep **

	Rep Function Displays the voucher in html format. This dispays the all the distributions with there amount like college incomee, 		admincharge, etc.
	"""

	from Auto.tcc.variable import *
	query =request.GET.get('id')
	client = TestTotal.objects.all().get(job_id =query)
	amount = Amount.objects.all().get(job_id =query)
	user = Job.objects.all().get(id=query)
	name = user.client.client.first_name
	try:
    		use = ClientJob.objects.all().get(job_id=query)
		mat = use.material.name
		lab = use.material.lab_id
	except Exception:
    		use = SuspenceJob.objects.all().get(job_id=query)
		mat = use.field.name
		lab = use.field.lab_id
	staff = Staff.objects.all().filter(lab_id = lab)
	con_type = client.type
	ratio1 = ratio1(con_type)
	ratio2 = ratio2(con_type)
	net_total1 = amount.unit_price
	net_total_eng = num2eng(net_total1)
	template = {'net_total_eng':net_total_eng,'servicetaxprint':servicetaxprint,
	'highereducationtaxprint':highereducationtaxprint,'educationtaxprint':educationtaxprint,'client': client,'amount':amount,'con_type':con_type, 'ratio1':ratio1 ,'ratio2':ratio2,'collegeincome':collegeincome,'admincharge' : admincharge,'user':user,'name':name,'mat':mat,'staff':staff}
	return render_to_response('tcc/report.html', template , context_instance=RequestContext(request))


def transport(request):
	"""
	** transport **

	Transport Function displays the form that get the information like kilometeres travelled etc from the user to get the transportation 		charges.
	"""

	tmp = material_site()
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
			return render_to_response('tcc/trans.html', dict(data.items() + tmp.items()),  context_instance=RequestContext(request))
	else:
		form = TransportForm()
	temp = {'form': form}
	return render_to_response('tcc/client.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))

def transport_bill(request):
	"""
	** transport_bill **

	Transport Bill Function generates transport Bill
	"""

	tmp =material_site()
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
	return render_to_response('tcc/transportbill.html', dict(template.items() + tmp.items()) , context_instance=RequestContext(request))

@login_required
def ta_da(request):
	"""
	** ta_da **

	Ta_Da Function displays the form for filling the Transport and Daily Allowance charges for a Job.
	"""

	query = request.GET.get('q', '')
	try :
		sus = Suspence.objects.get(job=query)
	except Exception:	
		sus =[]
	if request.method == 'POST':
		form = TadaForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			job =cd['job']
			test_date =cd['test_date']
                        end_date =cd['end_date']
			reach_site =cd['reach_site']
			profile = form.save(commit=False)
			profile.job = job
			profile.save()
			return HttpResponseRedirect(reverse('Auto.tcc.views.tada_view'))
	else:
		form = TadaForm()
	temp = {'form': form,'query':query,'sus':sus}
	return render_to_response('tcc/suspenceclear.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))


def tada_view(request):
	"""
	** tada_view **
	Tada_view function confirms that tada is saved.
	"""

	tmp = material_site()
	id = TaDa.objects.aggregate(Max('id'))
	maxid =id['id__max']
	tada = TaDa.objects.all().get(id=maxid)
	data = {'tada':tada }			
	return render_to_response('tcc/tada_ok.html', dict(data.items() + tmp.items()), context_instance=RequestContext(request))


def ta_da_bill(request):
	"""
	** ta_da_bill **

	Report of TA/DA Bill For Particular Date.
	"""

	tada = TaDa.objects.get(job=request.GET['job'],test_date=request.GET['test_date'])
	job = Job.objects.get(id=request.GET['job'])
	c = job.id
	client = Job.objects.filter(id=c).values('client__client__name')
	lab_staff = tada.testing_staff_code
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
	
	staff =Staff.objects.all().filter(Q(code=amount1)| Q(code=amount2) | Q(code=amount3) 
	| Q(code=amount4) | Q(code=amount5) | Q(code=amount6) | Q(code=amount7)| Q(code=amount8)
	| Q(code=amount9) | Q(code=amount10)).order_by('id') 
	daily_income = Staff.objects.filter(Q(code=amount1)| Q(code=amount2) | Q(code=amount3) 
	| Q(code=amount4) | Q(code=amount5) | Q(code=amount6) | Q(code=amount7)| Q(code=amount8)
	| Q(code=amount9) | Q(code=amount10)).aggregate(Sum('daily_income'))
	daily = int(daily_income['daily_income__sum']) 
	TaDa.objects.filter(job = tada.job).update( tada_amount = daily )
	
	data = {'tada':tada,'job':job,'staff':staff,  'daily':daily,'client':client}
	return render_to_response('tcc/ta_da_bill.html', data , context_instance=RequestContext(request))

def distance(request):
	"""
	** distance **

	Distance Function is for calculation of distance of the site on the map. This displays a form fo filling the site.
	"""

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
			sandy = cd['sandy']
			profile = form.save(commit=False)
			profile.job = jobid
			profile.save()
			return render_to_response('tcc/map_ok.html',tmp, context_instance=RequestContext(request))
		
	else:
  		form = DistanceForm()
	return render_to_response('tcc/siteinmap.html', {"form": form,}, context_instance=RequestContext(request))

def clientreport(request):
	"""
	** clientreport **

	Retrieves out the bill or receipt on demand for a particular job.
	"""

	query =request.GET.get('q', '')
	if query:
		job = Job.objects.filter(job_no = query).values('id','client__client__first_name','client__client__address_1','client__client__city','clientjob__material__name','suspencejob__field__name','site','testtotal__unit_price').order_by('id').distinct()
	else:	
		job =[]
	temp = {'job':job,'query':query}
	return render_to_response('tcc/clientreport.html',dict(temp.items() + tmp.items()),context_instance=RequestContext(request))
	

def suspence_clearance(request):
	"""
	** suspence_clearance **

	Suspence Clearance Function clears the suspence work. It has the form for filling the extra charges. 
	"""
	
	query = request.GET.get('q', '')
	try :
		sus = Suspence.objects.get(job=query)
	except Exception:	
		sus =[]
	if request.method == 'POST':
		form = SuspenceClearence(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			labour_charge =cd['labour_charge']
			car_taxi_charge =cd['car_taxi_charge']
			boring_charge_external=cd['boring_charge_external']
			boring_charge_internal=cd['boring_charge_internal']
			lab_testing_staff=cd['lab_testing_staff']
			field_testing_staff =cd['field_testing_staff']
			job =query
			Suspence.objects.filter(job = job).update(labour_charge=labour_charge,boring_charge_external=boring_charge_external, 
			boring_charge_internal= boring_charge_internal,field_testing_staff=field_testing_staff,car_taxi_charge=car_taxi_charge,lab_testing_staff=lab_testing_staff)
			data = {'job_no' :job, 'labour_charge':labour_charge,'boring_charge_external':boring_charge_external,
			'boring_charge_internal': boring_charge_internal,'car_taxi_charge':car_taxi_charge,'lab_testing_staff':lab_testing_staff,'sus':sus,}
			return render_to_response('tcc/suspence_clearence_ok.html', dict(data.items() + tmp.items()), context_instance=RequestContext(request))
	else:
		form = SuspenceClearence()
	temp ={'form': form,'query':query,'sus':sus}
	return render_to_response('tcc/suspenceclear.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))

def search(request):
	"""
	** search **

	Search Function is used to search a client using his/her name, type of work and address. The 'icontain' keyword is used which fetches 		all the rows that contain the query. THen the data related to that client that is required is also enlisted.
	"""

	query = request.GET.get('q', '')
	addquery=request.GET.get('add', '')
	if query:
		qset = (
			Q(first_name__icontains=query) |
			Q(type_of_organisation__icontains=query) 
	   	)
		aset = (
	     		Q(address_1__icontains=addquery)
		)
        	results = UserProfile.objects.filter(qset).filter(aset).distinct()
    	else:
        	results = []
	temp = {'results': results,'query': query,}
    	return render_to_response("tcc/search.html", dict(temp.items() + tmp.items()),context_instance=RequestContext(request))

def prevwork(request):
	"""
	** prevwork **

	Prevwork function is used to list down all the previous jobs for the client that was searched using search function. It also states 		which suspence job is cleared and which is still to be cleared, thus requiring the link to clear that job. The values with double 		underscore indicates that foreign key values are fetched.		
	"""

	user = UserProfile.objects.get(id=request.GET['id'])
	client = user.id
	job = Job.objects.filter(client__client__id = client).values('clientjob__material__name','suspencejob__field__name','id','job_no','date','site','amount__report_type','report_type','amount__college_income')
	data = {'user':user, 'job':job,}
	return render_to_response('tcc/prevwork.html',dict(data.items() + tmp.items()), context_instance=RequestContext(request))
	
def clearjob(request):
	"""
	** clearjob **

	Clearjob Function points to the job that is to be cleared listing all the necessary data that is required to be filled. 
	"""

	user = Job.objects.get(id=request.GET['job_id'])
	job = user.id
	temp = {'job':job}
	return render_to_response('tcc/compwork.html',dict(temp.items() + tmp.items()), context_instance=RequestContext(request))

def suspence_clearence_report(request):
	"""
	** suspence_clearance_report **

	This function generates the report for the suspence job after clearing it. Here the split function splits out the staff code entry 		to fetch its name from the tables.
	"""

	suspence = Suspence.objects.get(job=request.GET['job_no'])
	amount = Amount.objects.get(job=request.GET['job_no'])
	consultancy = TestTotal.objects.get(job=request.GET['job_no'])
	client =Job.objects.get(id=request.GET['job_no'])
	clientname = Job.objects.filter(id=client.id).values('client__client__first_name','suspencejob__field__name')
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
	staff =Staff.objects.all().filter(Q(code=amount1)| Q(code=amount2) | Q(code=amount3) 
	| Q(code=amount4) | Q(code=amount5) | Q(code=amount6) | Q(code=amount7)| Q(code=amount8)
	| Q(code=amount9) | Q(code=amount10)| Q(code=amounts1)| Q(code=amounts2) | Q(code=amounts3) 
	| Q(code=amounts4) | Q(code=amounts5) | Q(code=amounts6) | Q(code=amounts7)| Q(code=amounts8)
	| Q(code=amounts9) | Q(code=amounts10)).order_by('id')
	
	temp = suspence.labour_charge+suspence.rate+suspence.boring_charge_external+suspence.car_taxi_charge
	balance= amount.unit_price - (temp + suspence.boring_charge_internal)
	from Auto.tcc.variable import *
	college_income = round(collegeincome * balance / 100.00)
	admin_charge = round(admincharge * balance / 100.00)
	work_charge = round(workcharge * balance / 100.00)
	balance_temp = balance - college_income - admin_charge -work_charge
	con_type = consultancy.type
	ratio1 = ratio1(con_type)
	ratio2 = ratio2(con_type)
	consultancy_asst = round(ratio1 * balance_temp / 100)
	development_fund = round(ratio2 * balance_temp / 100)
	net_total1 = amount.unit_price
	net_balance_eng = num2eng(net_total1)
	retrieve()
	Suspence.objects.filter(job = client).update( work_charge = work_charge)
	Amount.objects.filter(job = client).update( college_income = college_income, admin_charge=admin_charge,
	consultancy_asst=consultancy_asst, development_fund=development_fund )
	sus = Suspence.objects.get(job=request.GET['job_no'])
	data = {'transport' : transport, 'net_balance_eng':net_balance_eng,'teachers':staff,'servicetaxprint':servicetaxprint,
	'highereducationtaxprint':highereducationtaxprint,'educationtaxprint':educationtaxprint,'ratio1':ratio1 ,
	'job_no':consultancy.id,'ratio2':ratio2,'other':temp,'collegeincome':collegeincome,'admincharge' : admincharge ,'client' :client, 'amount': amount,'suspence': sus,'client':client,'consultancy':consultancy,'clientname':clientname}
	return render_to_response('tcc/suspence_clearence_report.html', dict(data.items() + tmp.items()) , context_instance=RequestContext(request))

def  monthly_report(request):
	"""
	** monthly_report **

	Monthly report Function generates the register of work done within a month. This also asks for the paid education tax, higher 		education tax and service tax and then subtracts from the taxes for the month.
	"""

	if request.method == 'POST':
		form = MonthlyReportadd(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			month = cd['month']
			year = cd['year']
			month_print = month
			paid_education_tax= cd['paid_education_tax']
			paid_higher_education_tax= cd['paid_higher_education_tax']
			paid_service_tax= cd['paid_service_tax']
			month = months(month)
			client = Job.objects.filter(date__year=year).filter(date__month=month).values('job_no','date','client__client__first_name').distinct().order_by('job_no')
			bill = Bill.objects.all()
			job = Job.objects.all().values_list('job_no',flat=True).filter(date__year=year).filter(date__month=month)
			total_temp = Bill.objects.filter(job_no__in=job).aggregate(Sum('price'))
                        total= int(total_temp['price__sum'])
			service_tax_temp = Bill.objects.filter(job_no__in=job).aggregate(Sum('service_tax'))
			service_tax= int(service_tax_temp['service_tax__sum'])
			education_tax_temp = Bill.objects.filter(job_no__in=job).aggregate(Sum('education_tax'))
			education_tax= int(education_tax_temp['education_tax__sum'])
			higher_education_tax_temp = Bill.objects.filter(job_no__in=job).aggregate(Sum('higher_education_tax'))
			higher_education_tax= int(higher_education_tax_temp['higher_education_tax__sum'])
			net_total_temp = Bill.objects.filter(job_no__in=job).aggregate(Sum('net_total'))
			net_total= int(net_total_temp['net_total__sum'])
			tax = service_tax+education_tax+higher_education_tax
			ser_tax = service_tax-int(paid_service_tax)
			edu_tax = education_tax-paid_education_tax
			high_tax = higher_education_tax-paid_higher_education_tax
			final = ser_tax + edu_tax +high_tax
			paid_tax = paid_education_tax+paid_higher_education_tax+ paid_service_tax
			template = {'client':client,'bill':bill,'tax':tax,'month': month_print,'service_tax':service_tax,
			'education_tax':education_tax,'higher_education_tax':higher_education_tax, 'net_total':net_total,'total':total,
			'year':year,'paid_higher_education_tax':paid_higher_education_tax,'paid_tax':paid_tax,
			'paid_education_tax': paid_education_tax, 'paid_service_tax':paid_service_tax, 'final':final, 'ser_tax':ser_tax,
			'edu_tax':edu_tax, 'high_tax':high_tax,}
			return render_to_response('tcc/monthlyreport.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))
	else:
		form = MonthlyReportadd()
	data = {'form': form}
	return render_to_response('tcc/client.html', dict(data.items() + tmp.items()), context_instance=RequestContext(request))


def  Cashbook(request):    
	"""
	** Cashbook **

	This gives the debit and credit detail within a date range. The amount deposited in some bank or credited to someone can also be 		subtracted from the total.
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
			sumamt = sum((int(amount1),int(amount2),int(amount3),int(amount4),int(amount5)))
                        client = Job.objects.filter(date__range=(start_date,end_date)).values('job_no','date','client__client__first_name','pay','id').distinct().order_by('job_no').filter(pay='CASH')
			job = Job.objects.all().filter(date__range=(start_date,end_date)).filter(pay='CASH')
			chequeclient = Job.objects.filter(date__range=(start_date,end_date)).filter(Q(pay='CHEQUE')|Q(pay='DD')|Q(pay='ONLINE')).values('job_no','date','client__client__first_name','pay').distinct().order_by('job_no')
			testtotal = TestTotal.objects.all()
			chequejob = Job.objects.all().filter(date__range=(start_date,end_date)).filter(Q(pay='CHEQUE')|Q(pay='DD')|Q(pay='ONLINE'))
                        total_temp = TestTotal.objects.filter(job_id__in=job).aggregate(Sum('unit_price'))
                        total= int(total_temp['unit_price__sum'])
			net_total_temp = TestTotal.objects.filter(job_id__in=chequejob).aggregate(Sum('unit_price'))
                        net_total= int(net_total_temp['unit_price__sum'])
			balance = int(total)-int(sumamt)
			template ={'date': start_date, 'client':client,'type':type,'total':total,'testtotal':testtotal,'net_total':net_total,'name1':name1,'name2':name2,'name3':name3,'name4':name4,'name5':name5,'balance':balance,'amount1':amount1,'amount2':amount2,'amount3':amount3,'amount4':amount4,'amount5':amount5,'sumamt':sumamt,'chequeclient':chequeclient}
			return render_to_response('tcc/cashbook.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))
      	else:
		form = CashBook()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() + tmp.items()), context_instance=RequestContext(request))


def  daily_report(request): 
	"""
	** daily_report **

	This lists the jobs with payment type as Cash, Cheque, DD or Online depending on choice selected, within a date range.
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
				client = Job.objects.filter(date__range=(start_date,end_date)).filter(pay='CASH').values('id','job_no','date','client__client__first_name','tds').distinct().order_by('job_no')
				job = Job.objects.all().filter(date__range=(start_date,end_date)).filter(pay='CASH')
				testtotal = TestTotal.objects.all()
				tds_temp = Job.objects.all().filter(date__range=(start_date,end_date)).aggregate(Sum('tds'))
				tds= tds_temp['tds__sum']
				total_temp = TestTotal.objects.filter(job_id__in=job).aggregate(Sum('unit_price'))
				total= total_temp['unit_price__sum']
				template ={'date': start_date, 'client':client,'type':type,'total':total,'testtotal':testtotal,'tds':tds}
				return render_to_response('tcc/dailyreport.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))
			else :
				client = Job.objects.filter(date__range=(start_date,end_date)).filter(pay='ONLINE').values('id','job_no','date','client__client__first_name','tds').distinct().order_by('job_no')
				job = Job.objects.all().filter(date__range=(start_date,end_date)).filter(pay='ONLINE')
				testtotal = TestTotal.objects.all()
				tds_temp = Job.objects.all().filter(date__range=(start_date,end_date)).aggregate(Sum('tds'))
				tds= tds_temp['tds__sum']
				total_temp = TestTotal.objects.filter(job_id__in=job).aggregate(Sum('unit_price'))
				total= total_temp['unit_price__sum']
				template ={'date': start_date, 'client':client,'type':type,'total':total,'testtotal':testtotal,'tds':tds}
				return render_to_response('tcc/dailyreport.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))
	else:
		form = DailyReportadd()
	template = {'form': form}
	return render_to_response('tcc/client.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))


def  main_register(request):
	"""
	** main_register **

	Main Register function lists all the jobs that are in general report i.e. they are not suspence jobs.
	"""

	if request.method == 'POST':
		form = MonthlyReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			month = cd['month']
			year = cd['year']
			month_print = month
			month = months(month)
			job = Job.objects.filter(date__year=year).filter(date__month=month)
			client = Job.objects.filter(date__year=year).filter(date__month=month).values('client__client__first_name')
			amount = Amount.objects.all().filter(id__in=job).filter(report_type='General_report').values('job__date','job__id','job__job_no','college_income','admin_charge','consultancy_asst','development_fund','unit_price','job__client__client__first_name','job__clientjob__material__name')
			admin_charge_temp = Amount.objects.filter(id__in=job).filter(report_type='General_report').aggregate(Sum('admin_charge'))
			admin_charge= admin_charge_temp['admin_charge__sum']
			college_income_temp = Amount.objects.filter(id__in=job).filter(report_type='General_report').aggregate(Sum('college_income'))
			college_income= college_income_temp['college_income__sum']
			consultancy_asst_temp = Amount.objects.filter(id__in=job).filter(report_type='General_report').aggregate(Sum('consultancy_asst'))
			consultancy_asst= consultancy_asst_temp['consultancy_asst__sum']
			development_fund_temp = Amount.objects.filter(id__in=job).filter(report_type='General_report').aggregate(Sum('development_fund'))
			development_fund= development_fund_temp['development_fund__sum']
			price_temp = Amount.objects.filter(id__in=job).filter(report_type='General_report').aggregate(Sum('unit_price'))
			total= price_temp['unit_price__sum']
			template ={'month': month_print, 'year':year,'amount':amount,'job':job,'admin_charge':admin_charge,'college_income':college_income,'consultancy_asst':consultancy_asst,'development_fund':development_fund,
'total':total,'client':client}
			return render_to_response('tcc/main_register.html', dict(template.items() + tmp.items()), context_instance=RequestContext(request))
	else:
		form = MonthlyReport()
	template = {'form': form}
	return render_to_response('tcc/client.html', dict(template.items() + tmp.items()), context_instance=RequestContext(request))

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
			suspence = SuspenceJob.objects.all().filter(job_id__in=job).values('field__name','job_id').distinct()
			suspencedetail = Suspence.objects.all().filter(job_id__in=job).values('work_charge','labour_charge','boring_charge_external','car_taxi_charge','boring_charge_internal','job_id')
			amount = Amount.objects.all().filter(job_id__in=job).filter(report_type='Suspence').values('job__date','job__id','job__job_no','college_income','admin_charge','consultancy_asst','development_fund','unit_price','job__client__client__first_name').order_by('job__id').distinct().exclude(admin_charge = None)
			admin_charge_temp = Amount.objects.filter(id__in=job).filter(report_type='Suspence').aggregate(Sum('admin_charge'))
			admin_charge= admin_charge_temp['admin_charge__sum']
			college_income_temp = Amount.objects.filter(id__in=job).filter(report_type='Suspence').aggregate(Sum('college_income'))
			college_income= college_income_temp['college_income__sum']
			consultancy_asst_temp = Amount.objects.filter(id__in=job).filter(report_type='Suspence').aggregate(Sum('consultancy_asst'))
			consultancy_asst= consultancy_asst_temp['consultancy_asst__sum']
			development_fund_temp = Amount.objects.filter(id__in=job).filter(report_type='Suspence').aggregate(Sum('development_fund'))
			development_fund= development_fund_temp['development_fund__sum']
			price_temp = Amount.objects.filter(id__in=job).filter(report_type='Suspence').exclude(admin_charge = None).aggregate(Sum('unit_price'))
			total= price_temp['unit_price__sum']
			template ={'form':form, 'job':job,'suspence':suspence,'suspencedetail': suspencedetail, 'amount': amount,'date': start_date,'admin_charge':admin_charge,'college_income':college_income,'consultancy_asst':consultancy_asst,'development_fund':development_fund,
'total':total,}
			return render_to_response('tcc/suspence_clearence_register.html', dict(template.items() + tmp.items()), context_instance=RequestContext(request))
	else:
		form = DateReport()
	template ={'form': form}
	return render_to_response('tcc/client.html', dict(template.items() + tmp.items()), context_instance=RequestContext(request))


def  gov_pri_report(request):
	"""
	** gov_pri_report **

	This function lists the jobs that are Goverment, Semi-Government or Private depending upon the choice made within a particular date 		range.
	
	"""
	if request.method == 'POST':
		form = GovPriReport(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			type_of_organisation =cd['type_of_organisation']
			month = cd['month']
			year = cd['year']
			month = months(month)
			client = Job.objects.filter(date__year=year).filter(date__month=month).filter(type_of_work=type_of_organisation)
			amount = Amount.objects.all().filter(job_id__in=job).filter(report_type='Suspence').values('job__date','job__id','job__job_no','college_income','admin_charge','consultancy_asst','development_fund','unit_price','job__client__client__name').order_by('job__id').distinct().exclude(admin_charge = None)
			admin_charge_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('admin_charge'))
			admin_charge= admin_charge_temp['admin_charge__sum']
			college_income_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('college_income'))
			college_income= college_income_temp['college_income__sum']
			consultancy_asst_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('consultancy_asst'))
			consultancy_asst= consultancy_asst_temp['consultancy_asst__sum']
			development_fund_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('development_fund'))
			development_fund= development_fund_temp['development_fund__sum']
			service_tax_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('service_tax'))
			service_tax= service_tax_temp['service_tax__sum']
			education_tax_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('education_tax'))
			education_tax= education_tax_temp['education_tax__sum']
			higher_education_tax_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('higher_education_tax'))
			higher_education_tax= higher_education_tax_temp['higher_education_tax__sum']
			balance_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('balance'))
			balance= balance_temp['balance__sum']
			tds_temp = Amount.objects.filter(date__year=year).filter(date__month=month).filter(report_type='GENERAL REPORT').aggregate(Sum('tds'))
			tds= tds_temp['tds__sum']
			return render_to_response('Auto/gov_pri_report.html', dict(template.items() + tmp.items()), context_instance=RequestContext(request))
	else:
		form = MonthlyReport()
	template =  {'form': form}
	return render_to_response('Auto/client.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))

def lab_report(request):       
	"""
	** lab_report **

	This function lists all the jobs for a particular material in a date range.
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
			job=Job.objects.filter(clientjob__material__name=material).filter(date__range=(start_date,end_date))
		else:
			job=Job.objects.filter(suspencejob__field__name=material).filter(date__range=(start_date,end_date))
		client=Job.objects.filter(id__in=job).values('job_no','date','client__client__first_name','amount__unit_price')
		total_temp = Amount.objects.all().filter(job__in=job).aggregate(Sum('unit_price'))
		total= total_temp['unit_price__sum']
		template ={'form':form, 'total':total,'date':start_date, 'client':client,'job':job,'material':material}
		return render_to_response('tcc/labreport.html', dict(template.items() + tmp.items()) , context_instance=RequestContext(request))
       	else:
	        form = LabReport()         
		template ={'form': form}  
        return render_to_response('tcc/client.html', dict(template.items() + tmp.items()), context_instance=RequestContext(request))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['mkaurkhalsa@gmail.com'],
			)
			template = {'form': form}
			return render_to_response('contact/thanks.html',dict(template.items() + tmp.items()), context_instance=RequestContext(request))
    else:
        form = ContactForm()
	temp ={'form': form}
	if request.user.is_staff == 1 and request.user.is_active == 1 and request.user.is_superuser == 1:
		return render_to_response('contact/contact.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))
	elif request.user.is_staff == 0 and request.user.is_active == 1 and request.user.is_superuser == 0 :
		return render_to_response('contact/contact1.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))
	else:
		return render_to_response('contact/contact2.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))


