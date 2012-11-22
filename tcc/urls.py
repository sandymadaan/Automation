from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from Automation.tcc.models import *


urlpatterns = patterns('Automation.tcc.views',
    (r'^index/$', 'index1'),
    (r'^catalog/$', 'material'),
    (r'^previous/$', 'previous'),
    (r'^addprofile/$', 'profile'),
    (r'^performa/$', 'performa'),
    (r'^rate/$', 'rate'),
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
    (r'^save_susp/$', 'suspence'),
    (r'^g_report/$', 'g_report'),
    (r'^add_suspence/$', 'add_suspence'),
    (r'^job_submit/$', 'job_submit'),
    (r'^suspenceclearance/$', 'suspence_clearance'),
    (r'^search/$', 'search'),
    (r'^payjob/$', 'search_jobid'),
    (r'^edit_job/$', 'edit_job'),
    (r'^bank/$', 'fillbank'),
   
)

