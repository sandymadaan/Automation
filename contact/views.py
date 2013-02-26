from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from Auto.contact.forms import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from Auto.tcc.models import *

def material_site():
	material = Material.objects.all().filter(report=1)
	field = Material.objects.all().filter(report=2)
	title = get_object_or_404(Department, pk='1')	
	address = get_object_or_404(Organisation, pk='1')
	template={'material':material,'field':field,'title':title,'address':address}
	return template

tmp =material_site()

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
            return render_to_response('contact/thanks.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = ContactForm()
		temp ={'form': form}
		if request.user.is_staff == 1 and request.user.is_active == 1 and request.user.is_superuser == 1:
    		return render_to_response('contact/contact.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))
		elif request.user.is_staff == 0 and request.user.is_active == 1 and request.user.is_superuser == 0 :
			return render_to_response('contact/contact1.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))
		else:
			return render_to_response('contact/contact2.html', dict(temp.items() + tmp.items()), context_instance=RequestContext(request))


