"""
Models for the TCC-Automation is described in this file
"""
from django.db import models
from django.forms import ModelForm, TextInput, ModelChoiceField
import datetime
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Max ,Q, Sum
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from Automation.tcc.models import *
from django.forms.models import BaseModelFormSet  #for defining formset in models
#from report.tests import SeparatedValuesField 	  #for storing array in the models
from Automation.report.choices import *
import ast

"""
Search Report 
"""
class Search(models.Model):
	job = models.CharField(max_length=10)
	report = models.CharField(max_length=10)
	material = models.CharField(max_length=50)

	def __str__(self):
		return self.report
"""
Main reort table
"""
class Report(models.Model):
    #Head_id = models.ForeignKey(head)
	job = models.ForeignKey(Job, null=True)
	Sample_no = models.CharField(max_length=100, default=1)
	Header_column_1 = models.CharField(max_length=255,blank=True)
	Header_column_2 = models.CharField(max_length=255,blank=True)
	Footer_column_3 = models.CharField(max_length=255,blank=True)
    
	def __unicode__(self):
		return self.Sample_no #+ "(" + str(self.Head_id) + ")"

"""
Report Type Cube_Test
"""
class Cube(models.Model):
	ip_address = models.IPAddressField() 
	Report_id = models.ForeignKey(Report)
    	S_No = models.CharField(max_length=255,blank=True, default=1) 
    	Description = models.CharField(max_length=150, help_text="")
    	Breaking_load = models.CharField(max_length=150)
    	Mix = models.CharField(max_length=255,blank=True) 
    	Comp_strength = models.CharField(max_length=150, blank=True)
    
    	def __unicode__(self):
        	return self.S_No + " (" + str(self.Report_id) + ")"

"""
Report Type Cheical_Analysis
"""       
class Chem_analysis(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
    	s_no = models.CharField(max_length=255,blank=True, default=1)
    	description = models.CharField(max_length=255,blank=True)
    	result = models.CharField(max_length=255,blank=True)
    
    	def __unicode__(self):
        	return self.s_no + "(" + str(self.Report_id) + ")"

"""
Report Of Steel Samples
"""
class Steel(models.Model):
	ip_address = models.IPAddressField()		
	Report_id = models.ForeignKey(Report)
	S_No = models.CharField(max_length=255,blank=True, default=1)  
	Description_of_Test = models.CharField(max_length=255,blank=True)
	Acceptable_limit_as_per = models.CharField(max_length=255,blank=True)
	Result_1 = models.CharField(max_length=255,blank=True)
	Result_2 = models.CharField(max_length=255,blank=True)
	Result_3 = models.CharField(max_length=255,blank=True)
	
	def __unicode__(self):
		return self.S_No + "(" + str(self.Report_id) + ")"

"""
Report of Ground Water
"""
class Ground_Water(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	S_No = models.CharField(max_length=255,blank=True, default=1)		
	Result_1 = models.CharField(max_length=255,blank=True)
	Result_2 = models.CharField(max_length=255,blank=True)
	Result_3 = models.CharField(max_length=255,blank=True)

	def __unicode__(self):
		return self.S_No + "(" + str(self.Report_id) + ")"

"""
Report of Concrete Paver
"""
class Concrete_Paver(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	S_No = models.CharField(max_length=255,blank=True, default=1)		
	Description = models.CharField(max_length=255,blank=True)
	Thickness = models.CharField(max_length=255,blank=True)
	Comp_Strength_MPa = models.CharField(max_length=255,blank=True)
	 
	def __unicode__(self):
		return self.S_No + "(" + str(self.Report_id) + ")"

"""
Report of Interlock_Tiles
"""
class Interlock_Tiles(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	S_No = models.CharField(max_length=255,blank=True, default=1)		
	Description = models.CharField(max_length=255,blank=True)
	Thickness = models.CharField(max_length=255,blank=True)
	Comp_Strength_MPa = models.CharField(max_length=255,blank=True)
	 
	def __unicode__(self):
		return self.S_No + "(" + str(self.Report_id) + ")"

"""
Report of PC Samples
"""
class PC(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	S_No = models.CharField(max_length=255,blank=True, default=1)		
	Description = models.CharField(max_length=255,blank=True)
	Bitumen_Content = models.CharField(max_length=255,blank=True)
	 
	def __unicode__(self):
		return self.S_No + "(" + str(self.Report_id) + ")"
  
"""
Report of Rebound Hammer Testing
"""
class Rebound_Hammer_Testing(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	S_No = models.CharField(max_length=255,blank=True)		
	Location = models.CharField(max_length=255,blank=True)
	Striking_Angle = models.CharField(max_length=255,blank=True)
	Average_Rebound_No = models.CharField(max_length=255,blank=True)
	Comp_Strength_MPa = models.CharField(max_length=255,blank=True)
 	 
	def __unicode__(self):
		return self.S_No + "(" + str(self.Report_id) + ")"

"""
Report of Brick Sample
"""
class Brick(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	S_No = models.CharField(max_length=255,blank=True)		
	Comp_Strength = models.CharField(max_length=255,blank=True)
	Water_Absorption = models.CharField(max_length=255,blank=True)
	Efflorescence = models.CharField(max_length=255,blank=True)
	Dimension_Test = models.CharField(max_length=255,blank=True)
 	 
	def __unicode__(self):
		return self.S_No + "(" + str(self.Report_id) + ")"

"""
Report of WATER/WASTE WATER
"""
class Water(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	PH_Value = models.CharField(max_length=255,blank=True, default=1)
	Color = models.CharField(max_length=255,blank=True, default=1)
	COD_Total = models.CharField(max_length=255,blank=True, default=1)
	COD_Filtered = models.CharField(max_length=255,blank=True, default=1)
	BOD5_Total = models.CharField(max_length=255,blank=True, default=1)
	BOD5_Filtered = models.CharField(max_length=255,blank=True, default=1)
	Sulphide = models.CharField(max_length=255,blank=True, default=1)
	Sulphate = models.CharField(max_length=255,blank=True, default=1)
	Alkalinity = models.CharField(max_length=255,blank=True, default=1)
	Total_Suspended_Solids = models.CharField(max_length=255,blank=True, default=1)
	Volatile_Suspended_Solids = models.CharField(max_length=255,blank=True, default=1)
	Chloride_as_Cl = models.CharField(max_length=255,blank=True, default=1)
	Nickel = models.CharField(max_length=255,blank=True, default=1)
	Iron = models.CharField(max_length=255,blank=True, default=1)
	Maganese = models.CharField(max_length=255,blank=True, default=1)
	Copper = models.CharField(max_length=255,blank=True, default=1)
	Hardness = models.CharField(max_length=255,blank=True, default=1)
	Nitrates = models.CharField(max_length=255,blank=True, default=1)
	Nitrites = models.CharField(max_length=255,blank=True, default=1)
	Turbidity = models.CharField(max_length=255,blank=True, default=1)
	Faecal_coliform = models.CharField(max_length=255,blank=True, default=1)
	TDS = models.CharField(max_length=255,blank=True, default=1)
	Taste_and_Odour = models.CharField(max_length=255,blank=True, default=1)
	Calcium_and_Ca_Mg_per_l = models.CharField(max_length=255,blank=True, default=1)
	Residual_Free_Chloride = models.CharField(max_length=255,blank=True, default=1)
	Florides = models.CharField(max_length=255,blank=True, default=1)
	Ammonia_Nitrogen = models.CharField(max_length=255,blank=True, default=1)
	Total_Phosphorus = models.CharField(max_length=255,blank=True, default=1)
	TKN = models.CharField(max_length=255,blank=True, default=1)	

	def __unicode__(self):
		return self.PH_Value + "(" + str(self.Report_id) + ")"

"""
 Model for SOIL OSHR
"""
class Soil_Ohsr(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	Date_of_testing = models.DateField()
	Type_of_str = models.CharField(max_length=255)
	Latitude_N = models.CharField(max_length=255,blank=True)
	Longitude_E = models.CharField(max_length=255,blank=True)
	Presence_1 = models.CharField(max_length=255)
	Presence_2 = models.CharField(max_length=255,blank=True)
	Submitted_1 = models.CharField(max_length=255)
	Submitted_2 = models.CharField(max_length=255,blank=True)
	Submitted_3 = models.CharField(max_length=255,blank=True)
	Site_name = models.CharField(max_length=255)
	Water_table = models.CharField(max_length=255)
	Depth_D = models.CharField(max_length=255,blank=True,default=3.0)
	Diameter_B = models.CharField(max_length=255,default=11.0)
	Gama_G = models.CharField(max_length=255, default=16.8)
	C = models.CharField(max_length=255, default=5.0)
	Phay = models.CharField(max_length=255, default=24)	
	Phay_fe = models.CharField(max_length=255, default=16.60)
	Nc = models.CharField(max_length=255)
	Nq = models.CharField(max_length=255)
	Ny = models.CharField(max_length=255)
	dc = models.CharField(max_length=255)
	dqdy = models.CharField(max_length=255)
	Water = models.CharField(max_length=255)
	Pulse_Pulse = models.CharField(max_length=255)
	Eq_Total = models.CharField(max_length=255)
	Total_Dby_2 = models.CharField(max_length=255)
	Dt_1 = models.CharField(max_length=255)
	Dt_2 = models.CharField(max_length=255)
	Dt_3 = models.CharField(max_length=255)
	Dt_4 = models.CharField(max_length=255)
	Dt_5 = models.CharField(max_length=255)
	Dt_6 = models.CharField(max_length=255)
	Dt_7 = models.CharField(max_length=255)
	Dt_8 = models.CharField(max_length=255)
	Ob_Pr_1 = models.CharField(max_length=255)
	Ob_Pr_2 = models.CharField(max_length=255)
	Ob_Pr_3 = models.CharField(max_length=255)
	Ob_Pr_4 = models.CharField(max_length=255)
	Ob_Pr_5 = models.CharField(max_length=255)
	Ob_Pr_6 = models.CharField(max_length=255)
	Ob_Pr_7 = models.CharField(max_length=255)
	Ob_Pr_8 = models.CharField(max_length=255)
	Corr_F_1 = models.CharField(max_length=255)
	Corr_F_2 = models.CharField(max_length=255)
	Corr_F_3 = models.CharField(max_length=255)
	Corr_F_4 = models.CharField(max_length=255)
	Corr_F_5 = models.CharField(max_length=255)
	Corr_F_6 = models.CharField(max_length=255)
	Corr_F_7 = models.CharField(max_length=255)
	Corr_F_8 = models.CharField(max_length=255)
	Ob_N_V1 = models.CharField(max_length=255)
	Ob_N_V2 = models.CharField(max_length=255)
	Ob_N_V3 = models.CharField(max_length=255)
	Ob_N_V4 = models.CharField(max_length=255)
	Ob_N_V5 = models.CharField(max_length=255)
	Ob_N_V6 = models.CharField(max_length=255)
	Ob_N_V7 = models.CharField(max_length=255)
	Ob_N_V8 = models.CharField(max_length=255)
	Corr_N_V1 = models.CharField(max_length=255)
	Corr_N_V2 = models.CharField(max_length=255)
	Corr_N_V3 = models.CharField(max_length=255)
	Corr_N_V4 = models.CharField(max_length=255)
	Corr_N_V5 = models.CharField(max_length=255)
	Corr_N_V6 = models.CharField(max_length=255)
	Corr_N_V7 = models.CharField(max_length=255)
	Corr_N_V8 = models.CharField(max_length=255)
	N_Value = models.CharField(max_length=255)
	S = models.CharField(max_length=255)
	Value = models.CharField(max_length=255)
	Net_Value = models.CharField(max_length=255)

	def __unicode__(self):
	        return self.Date_of_testing + "(" + str(self.Report_id) + ")"

"""
Model for Soil_Building
"""
class Soil_Building(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	Date_of_Testing = models.CharField(max_length=100,blank=True)
	Type_of_Str = models.CharField(max_length=100,blank=True)
	Latitude_N = models.CharField(max_length=100,blank=True)
	Longitude_E = models.CharField(max_length=100,blank=True)
	Presence_1 = models.CharField(max_length=100,blank=True)
	Presence_2 = models.CharField(max_length=100,blank=True)
	Submitted_1 = models.CharField(max_length=100,blank=True)
	Submitted_2 = models.CharField(max_length=100,blank=True)
	Submitted_3 = models.CharField(max_length=100,blank=True)
	Site_Name = models.CharField(max_length=100,blank=True)
	Site_Name = models.CharField(max_length=100,blank=True)
	Submitted_1 = models.CharField(max_length=100,blank=True)
	Submitted_2 = models.CharField(max_length=100,blank=True)
	Submitted_3 = models.CharField(max_length=100,blank=True)
	Date_of_Testing = models.CharField(max_length=100,blank=True)
	Presence_1 = models.CharField(max_length=100,blank=True)
	Presence_2 = models.CharField(max_length=100,blank=True)
	Type_of_Str = models.CharField(max_length=100,blank=True)
	Wall_Dt = models.CharField(max_length=100,blank=True)
	Wall_B = models.CharField(max_length=100,blank=True)
	Col_Df = models.CharField(max_length=100,blank=True)
	Col_L = models.CharField(max_length=100,blank=True)
	Col_B = models.CharField(max_length=100,blank=True)
	Gama_wall = models.CharField(max_length=100,blank=True)
	Wall_C = models.CharField(max_length=100,blank=True)
	Wall_Phay = models.CharField(max_length=100,blank=True)
	Wall_Phay_Fe = models.CharField(max_length=100,blank=True)
	Wall_Nc = models.CharField(max_length=100,blank=True)
	Wall_Nq = models.CharField(max_length=100,blank=True)
	Wall_Ny = models.CharField(max_length=100,blank=True)
	Wall_Sc = models.CharField(max_length=100,blank=True)
	Wall_Sq = models.CharField(max_length=100,blank=True)
	Wall_Sy = models.CharField(max_length=100,blank=True)
	Wall_dc = models.CharField(max_length=100,blank=True)
	Wall_dq_dy = models.CharField(max_length=100,blank=True)
	Wall_w = models.CharField(max_length=100,blank=True)
	Gama_wall = models.CharField(max_length=100,blank=True)
	Wall_peq = models.CharField(max_length=100,blank=True)
	Wall_Total = models.CharField(max_length=100,blank=True)
	Wall_T_2 = models.CharField(max_length=100,blank=True)
	Col_Df = models.CharField(max_length=100,blank=True)
	Col_L = models.CharField(max_length=100,blank=True)
	Col_B = models.CharField(max_length=100,blank=True)
	Col_Sc = models.CharField(max_length=100,blank=True)
	Col_Sq = models.CharField(max_length=100,blank=True)
	Col_Sy = models.CharField(max_length=100,blank=True)
	Col_dc = models.CharField(max_length=100,blank=True)
	Col_dq_dy = models.CharField(max_length=100,blank=True)
	Col_peq = models.CharField(max_length=100,blank=True)
	Col_Total = models.CharField(max_length=100,blank=True)
	Col_T_2 = models.CharField(max_length=100,blank=True)
	Dt_1 = models.CharField(max_length=100,blank=True)
	Dt_2 = models.CharField(max_length=100,blank=True)
	Dt_3 = models.CharField(max_length=100,blank=True)
	Dt_4 = models.CharField(max_length=100,blank=True)
	Dt_5 = models.CharField(max_length=100,blank=True)
	Dt_6 = models.CharField(max_length=100,blank=True)
	Dt_7 = models.CharField(max_length=100,blank=True)
	Dt_8 = models.CharField(max_length=100,blank=True)
	Ob_Pr_1 = models.CharField(max_length=100,blank=True) 
	Ob_Pr_2 = models.CharField(max_length=100,blank=True)
	Ob_Pr_3 = models.CharField(max_length=100,blank=True)
	Ob_Pr_4 = models.CharField(max_length=100,blank=True)
	Ob_Pr_5 = models.CharField(max_length=100,blank=True)
	Ob_Pr_6 = models.CharField(max_length=100,blank=True)
	Ob_Pr_7 = models.CharField(max_length=100,blank=True)
	Ob_Pr_8 = models.CharField(max_length=100,blank=True)
	Corr_F_1 = models.CharField(max_length=100,blank=True)
	Corr_F_2 = models.CharField(max_length=100,blank=True)
	Corr_F_3 = models.CharField(max_length=100,blank=True)
	Corr_F_4 = models.CharField(max_length=100,blank=True)
	Corr_F_5 = models.CharField(max_length=100,blank=True)
	Corr_F_6 = models.CharField(max_length=100,blank=True)
	Corr_F_7 = models.CharField(max_length=100,blank=True)
	Corr_F_8 = models.CharField(max_length=100,blank=True)
	Ob_N_V1 = models.CharField(max_length=100,blank=True)
	Ob_N_V2 = models.CharField(max_length=100,blank=True)
	Ob_N_V3 = models.CharField(max_length=100,blank=True)
	Ob_N_V4 = models.CharField(max_length=100,blank=True)
	Ob_N_V5 = models.CharField(max_length=100,blank=True)
	Ob_N_V6 = models.CharField(max_length=100,blank=True)
	Ob_N_V7 = models.CharField(max_length=100,blank=True)
	Ob_N_V8 = models.CharField(max_length=100,blank=True)
	Corr_N_V1 = models.CharField(max_length=100,blank=True)
	Corr_N_V2 = models.CharField(max_length=100,blank=True)
	Corr_N_V3 = models.CharField(max_length=100,blank=True)
	Corr_N_V4 = models.CharField(max_length=100,blank=True)
	Corr_N_V5 = models.CharField(max_length=100,blank=True)
	Corr_N_V6 = models.CharField(max_length=100,blank=True)
	Corr_N_V7 = models.CharField(max_length=100,blank=True)
	Corr_N_V8 = models.CharField(max_length=100,blank=True)
	Wall_Net_V = models.CharField(max_length=100,blank=True)
	Wall_Value = models.CharField(max_length=100,blank=True)
	Wall_G_V = models.CharField(max_length=100,blank=True)
	Col_Value = models.CharField(max_length=100,blank=True)
	Col_Net_V = models.CharField(max_length=100,blank=True)
	Col_G_V = models.CharField(max_length=100,blank=True)
	Col_N_V = models.CharField(max_length=100,blank=True)
	Wall_N_V = models.CharField(max_length=100,blank=True)
	Water_Table = models.CharField(max_length=100,blank=True)	

	def __unicode__(self):
	        return self.Date_of_testing + "(" + str(self.Report_id) + ")"

"""
Model for ADMIXTURE 
"""
class Admixture(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	S_No = models.CharField(max_length=100,blank=True)
	Physical_state = models.CharField(max_length=100,blank=True)	
	Specific_Gravity = models.CharField(max_length=100,blank=True)	
	PH_Value = models.CharField(max_length=100,blank=True)	
	Dry_Material_Content = models.CharField(max_length=100,blank=True)	
	Ash_Content = models.CharField(max_length=100,blank=True)	
	Chloride_Content = models.CharField(max_length=100,blank=True)	
	Control_Mix = models.CharField(max_length=100,blank=True)	

	def __unicode__(self):
	        return self.S_No + "(" + str(self.Report_id) + ")"
"""
###########################
# Model for Cement Report #
########################### 
"""
"""
(PPC) IS 1489-1 & 2 Fly Ash Or Clay
"""
class Cement_PPC(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	Initial_Time = models.CharField(max_length=100,blank=True)		#Setting Time(Minutes) 
	Final_Time = models.CharField(max_length=100,blank=True)
	Fineness = models.CharField(max_length=100,blank=True)
	Unaerated_Cement_Le = models.CharField(max_length=100,blank=True) 	#for Le-chat expansion(MM)
	After_7_Days_Areation_Le = models.CharField(max_length=100,blank=True)
	Unaerated_Cement_Auto = models.CharField(max_length=100,blank=True)	#for Auto Clave expansion(%)
	After_7_Days_Areation_Auto = models.CharField(max_length=100,blank=True)	
	Consistency = models.CharField(max_length=100,blank=True)	
	Hours_72 = models.CharField(max_length=100,blank=True) 			#Compressive Strength(MPa)	
	Hours_168 = models.CharField(max_length=100,blank=True)	
	Hours_672 = models.CharField(max_length=100,blank=True)	

	def __unicode__(self):
	        return self.Initial_Time + "(" + str(self.Report_id) + ")"

"""
(OPC) IS 269 33 GRADE 
"""
class Cement_OPC_33(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	Initial_Time = models.CharField(max_length=100,blank=True)		#Setting Time(Minutes) 
	Final_Time = models.CharField(max_length=100,blank=True)
	Fineness = models.CharField(max_length=100,blank=True)
	Unaerated_Cement_Le = models.CharField(max_length=100,blank=True) 	#for Le-chat expansion(MM)
	After_7_Days_Areation_Le = models.CharField(max_length=100,blank=True)
	Unaerated_Cement_Auto = models.CharField(max_length=100,blank=True)	#for Auto Clave expansion(%)
	After_7_Days_Areation_Auto = models.CharField(max_length=100,blank=True)	
	Consistency = models.CharField(max_length=100,blank=True)	
	Hours_72 = models.CharField(max_length=100,blank=True) 			#Compressive Strength(MPa)	
	Hours_168 = models.CharField(max_length=100,blank=True)	
	Hours_672 = models.CharField(max_length=100,blank=True)	

	def __unicode__(self):
	        return self.Initial_Time + "(" + str(self.Report_id) + ")"


"""
(OPC) IS 8812 43 GRADE 
"""
class Cement_OPC_43(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	Initial_Time = models.CharField(max_length=100,blank=True)		#Setting Time(Minutes) 
	Final_Time = models.CharField(max_length=100,blank=True)
	Fineness = models.CharField(max_length=100,blank=True)
	Unaerated_Cement_Le = models.CharField(max_length=100,blank=True) 	#for Le-chat expansion(MM)
	After_7_Days_Areation_Le = models.CharField(max_length=100,blank=True)
	Unaerated_Cement_Auto = models.CharField(max_length=100,blank=True)	#for Auto Clave expansion(%)
	After_7_Days_Areation_Auto = models.CharField(max_length=100,blank=True)	
	Consistency = models.CharField(max_length=100,blank=True)	
	Hours_72 = models.CharField(max_length=100,blank=True) 			#Compressive Strength(MPa)	
	Hours_168 = models.CharField(max_length=100,blank=True)	
	Hours_672 = models.CharField(max_length=100,blank=True)	

	def __unicode__(self):
	        return self.Initial_Time + "(" + str(self.Report_id) + ")"


"""
(OPC) IS 12269 53 GRADE
"""
class Cement_OPC_53(models.Model):
	ip_address = models.IPAddressField()
	Report_id = models.ForeignKey(Report)
	Initial_Time = models.CharField(max_length=100,blank=True)		#Setting Time(Minutes) 
	Final_Time = models.CharField(max_length=100,blank=True)
	Fineness = models.CharField(max_length=100,blank=True)
	Unaerated_Cement_Le = models.CharField(max_length=100,blank=True) 	#for Le-chat expansion(MM)
	After_7_Days_Areation_Le = models.CharField(max_length=100,blank=True)
	Unaerated_Cement_Auto = models.CharField(max_length=100,blank=True)	#for Auto Clave expansion(%)
	After_7_Days_Areation_Auto = models.CharField(max_length=100,blank=True)	
	Consistency = models.CharField(max_length=100,blank=True)	
	Hours_72 = models.CharField(max_length=100,blank=True) 			#Compressive Strength(MPa)	
	Hours_168 = models.CharField(max_length=100,blank=True)	
	Hours_672 = models.CharField(max_length=100,blank=True)	

	def __unicode__(self):
	        return self.Initial_Time + "(" + str(self.Report_id) + ")"
"""
Model to store pdf/image
"""
class Report(models.Model): 
	file = models.FileField(upload_to='uploads/documents') 

