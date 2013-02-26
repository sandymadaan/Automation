"""
This view is defined to produce pdf output 
"""

"""
For Pisa library
"""
import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.http import HttpResponseRedirect
from cgi import escape
from Auto.report.views import *
"""
For Reportlab
"""
from reportlab.graphics.shapes import Drawing,colors
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.lineplots import LinePlot

"""
Reportlab view
"""
def report_pdf(request):
	#Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=report.pdf'

	#Create a PDF object, using the response object as its "file."
	p = canvas.Canvas(response)

	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(100, 100, "Guru Nanak Dev Engg College, Ludhiana")

	# Close the PDF object cleanly, and we're done.
	p.showPage()
    	p.save()
  	return response


"""
Pisa view
"""
'''
def render_to_pdf(template_src, context_dict):
	template = get_template(template_src)
	context = Context(context_dict)
	html  = template.render(context)
	result = StringIO.StringIO()
	
	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), mimetype='application/pdf')
	return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def myview(request):
    #Retrieve data or whatever you need
    results = "hello"
    return render_to_pdf(
            'report/pdf.html',
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )'''

			
