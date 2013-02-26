"""
Views for different search functions
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from Automation.report.models import *
from Automation.report.forms import *
from Automation.report.views import *
from django.core.context_processors import csrf

"""
For search by report_id
"""
'''
def search_report(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():	
			cd = form.cleaned_data
			Report_id = cd['Report_id']
			Test_Report = cd['Test_Report']

			if Test_Report == "SOIL OHSR":
				Report_id = Soil_Ohsr.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_Soil_ohsr'))

			if Test_Report == "SOIL BUILDING":
				Report_id = Soil_Building.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_soil_building'))

			if Test_Report == "ADMIXTURE":
				Report_id = Admixture.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_Admixture'))

			if Test_Report == "CUBE":
				Report_id = Cube.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_cube'))

			if Test_Report == "WATER":
				Report_id = Water.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_water'))

			if Test_Report == "BRICK":
				Report_id = Brick.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_brick'))

			if Test_Report == "CHEMICAL ANALYSIS":
				Report_id = Chem_analysis.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_chem'))

			if Test_Report == "CEMENT PPC":
				Report_id = Cement_PPC.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_Cement_PPC'))

			if Test_Report == "OPC 33 GRADE":
				Report_id = Cement_OPC_33.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_Cement_OPC_33'))

			if Test_Report == "OPC 43 GRADE":
				Report_id = Cement_OPC_43.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_Cement_OPC_43'))

			if Test_Report == "OPC 53 GRADE":
				Report_id = Cement_OPC_53.objects.get(Report_id = Report_id)
				return HttpResponseRedirect(reverse('Automation.report.views.result_Cement_OPC_53'))

			else:
		        	return HttpResponse("The Report no. or Test Report did not match, Please enter the correct Report no.")
	else:
		form = SearchForm()
	return render_to_response('report/report.html', {'form': form}, context_instance=RequestContext(request))
'''

"""
Search Box of searching Job_id to generate report
"""
def search(request):
	query = request.GET.get('q', '')
    	if query:
        	results = Job.objects.filter(id = query).values('client__client__name','client__client__address_1','clientjob__material__name','suspencejob__field__name','id','job_no','date','site','report_type',)
	else:
        	results = []
    	return render_to_response("report/search.html", {"results": results,"query": query})

"""
For searching the report by Job_id
"""
def search_report(request):
	query = request.GET.get('q', '')
    	if query:
        	results = Job.objects.filter(id = query).values('report__Sample_no','report__id','client__client__name','client__client__address_1','clientjob__material__name','suspencejob__field__name','id','job_no','date','site','report_type',)
	else:
        	results = []
    	return render_to_response("report/search_report.html", {"results": results,"query": query})

"""
For re-generating the report
"""
def report_gen(request):
	job = request.GET.get('id', '')
	p = Search(job = job)
	p.save()	
	material = Job.objects.filter(id = job).values('clientjob__material__name',)
	report = Report.objects.filter(id = job).values('id')
	
	if material == "Cube":
		Report_id = Cube.objects.get(report = Report_id)
		return HttpResponseRedirect(reverse('Automation.report.views.result_cube'))
	else:
			
		return HttpResponse("gal halle bani ni")




