"""
All the forms of report are described here.
"""
from Automation.report.models import * # Change as necessary
from django.forms import ModelForm

#################################
# From the module "Report" only #
#################################

"""Main form for Reports"""
class ReportForm(ModelForm):
  	class Meta:
    		model = Report
    		exclude = ('job_id')

"""Form for Cube"""
class CubeForm(ModelForm):
	class Meta:
		model = Cube
    		exclude = ('Report_id','ip_address')

"""Form for Chemical Analysis"""
class Chem_analysisForm(ModelForm):
	class Meta :
		model = Chem_analysis
		exclude = ('Report_id','ip_address')

"""Form for Steel"""  
class SteelForm(ModelForm):
	class Meta :
		model = Steel
		exclude = ('Report_id','ip_address')

"""Form for Ground_Water"""
class Ground_WaterForm(ModelForm):
	class Meta :
		model = Ground_Water
		exclude = ('Report_id','ip_address')

"""Form for Concrete_Paver"""
class Concrete_PaverForm(ModelForm):
	class Meta :
		model = Concrete_Paver
		exclude = ('Report_id','ip_address')

"""Form for PC"""  
class PCForm(ModelForm):
	class Meta :
		model = PC
		exclude = ('Report_id','ip_address')

"""Form for Rebound_Hammer_Testing""" 
class Rebound_Hammer_TestingForm(ModelForm):
	class Meta :
		model = Rebound_Hammer_Testing
		exclude = ('Report_id','ip_address')

"""Form for Brick""" 
class BrickForm(ModelForm):
	class Meta :
		model = Brick
		exclude = ('Report_id','ip_address')

"""Form for Water"""
class WaterForm(ModelForm):
	class Meta :
		model = Water
		exclude = ('Report_id','ip_address')

"""Form for Soil_Ohsr""" 
class Soil_OhsrForm(ModelForm):
	class Meta :
		model = Soil_Ohsr
		exclude = ('Report_id','ip_address')		

"""Form for Soil_Building""" 
class Soil_BuildingForm(ModelForm):
	class Meta :
		model = Soil_Building
		exclude = ('Report_id','ip_address')		

"""Form for Admixture"""
class AdmixtureForm(ModelForm):
	class Meta :
		model = Admixture
		exclude = ('Report_id','ip_address')		

"""Form for Cement_PPC"""
class Cement_PPCForm(ModelForm):
	class Meta :
		model = Cement_PPC
		exclude = ('Report_id','ip_address')		

"""Form for Cement_OPC_33"""
class Cement_OPC_33Form(ModelForm):
	class Meta :
		model = Cement_OPC_33
		exclude = ('Report_id','ip_address')		

"""Form for Cement_OPC_43"""
class Cement_OPC_43Form(ModelForm):
	class Meta :
		model = Cement_OPC_43
		exclude = ('Report_id','ip_address')		

"""Form for Cement_OPC_53"""
class Cement_OPC_53Form(ModelForm):
	class Meta :
		model = Cement_OPC_53
		exclude = ('Report_id','ip_address')		



