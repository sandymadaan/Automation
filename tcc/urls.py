"""
%% urls.py %%

This file define the urls used in the software for tcc application. In this regular expression are used, which are used to connect the url with the functions defined.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::::::::::::#
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from Automation.tcc.models import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE URLS HERE::::::::::::::::::::::::::::::::::::#

urlpatterns = patterns('Automation.tcc.views',
    (r'^index/$', 'index1'),
    (r'^catalog/$', 'material'),
    (r'^previous/$', 'previous'),
    (r'^addprofile/$', 'profile'),
    (r'^performa/$', 'performa'),
    (r'^rate/hello/$', 'rate'),
    (r'^performa/$', 'performa'),
    (r'^addjob/$', 'selectfield'),
    (r'^select/$', 'select'),
    (r'^save/$', 'add_job'),
    (r'^prev/$','previous'),
    (r'^transport/$', 'transport'),
    (r'^transportbill/$', 'transport_bill'),
    (r'^jobok/$', 'job_ok'),
    (r'^bill/$', 'bill'),
    (r'^receipt/$','receipt_report'),
    (r'^gen_report/$','gen_report'),
    (r'^report/$','rep'),
    (r'^map/$', 'distance'),
    (r'^g_report/$', 'g_report'),
    (r'^add_suspence/$', 'add_suspence'),
    (r'^job_submit/$', 'job_submit'),
    (r'^suspenceclearance/$', 'suspence_clearance'),
    (r'^search/$', 'search'),
    (r'^monthlyreport/$', 'monthly_report'),
    (r'^dailyreport/$', 'daily_report'),
    (r'^mainreg/$', 'main_register'),
    (r'^suspenceclearencereport/$', 'suspence_clearence_report'),
    (r'^suspenceclearreg/$', 'suspence_clearence_register'),
    (r'^tada/$', 'ta_da'),
    (r'^tadabill/$', 'ta_da_bill'),
    (r'^tada_view/$', 'tada_view'),
    (r'^prevwork/$', 'prevwork'), 
    (r'^clearjob/$', 'clearjob'),
    (r'^clientreport/$', 'clientreport'),
    (r'^cashbook/$', 'Cashbook'),
    (r'^labreport/$', 'lab_report'),
    (r'^contact/$', 'contact'),
    (r'^othertest/$', 'add_job_other_test'),
    (r'^gen_report_other/$', 'gen_report_other'),
    (r'^edit_profile/$', 'edit_profile'),
   
)

urlpatterns += patterns('Automation.tcc.views_ext',
    (r'^selectfield/$', 'perfselectfield'),
    (r'^perfselect/$', 'perfselect'),
    (r'^addperf/$', 'add_perf'),
    (r'^addsuspenceperf/$', 'add_suspence_perf'),
    (r'^genreportperf/$', 'gen_report_perf'),
    (r'^jobsubmitperf/$', 'job_submit_perf'),
    (r'^jobokperf/$', 'job_ok_perf'),
    (r'^billperf/$', 'billperf'),
    (r'^payjob/$', 'search_job'),
    (r'^editwork/$', 'edit_work'),
   )
