"""
%% choices.py %%

This file is a static file that shows the choices in a particular Drop down list. This conatin the state choices, year, month and day choices.
"""

#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::::::::::::#
from django.utils.translation import ugettext as _
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE CHOICES HERE:::::::::::::::::::::::::::::::::#

STATES_CHOICES = (
    ('Andhra Pradesh', _('Andhra Pradesh')),
    ('Arunachal Pradesh', _('Arunachal Pradesh')),
    ('Assam', _('Assam')),
    ('Bihar', _('Bihar')),
    ('Chhattisgarh', _('Chhattisgarh')),
    ('Goa', _('Goa')),
    ('Gujarat', _('Gujarat')),
    ('Haryana', _('Haryana')),
    ('Himachal Pradesh', _('Himachal Pradesh')),
    ('Jammu and Kashmir', _('Jammu and Kashmir')),
    ('Jharkhand', _('Jharkhand')),
    ('Karnataka', _('Karnataka')),
    ('Kerala', _('Kerala')),
    ('Madhya Pradesh', _('Madhya Pradesh')),
    ('Maharashtra', _('Maharashtra')),
    ('Manipur', _('Manipur')),
    ('Meghalaya', _('Meghalaya')),
    ('Mizoram', _('Mizoram')),
    ('Nagaland', _('Nagaland')),
    ('Orissa', _('Orissa')),
    ('Punjab', _('Punjab')),
    ('Rajasthan', _('Rajasthan')),
    ('Sikkim', _('Sikkim')),
    ('Tamil Nadu', _('Tamil Nadu')),
    ('Tripura', _('Tripura')),
    ('Uttar Pradesh', _('Uttar Pradesh')),
    ('Uttarakhand', _('Uttarakhand')),
    ('West Bengal', _('West Bengal')),
) 

MONTH_CHOICES = ( 
	('January', _('January')),
	('February', _('February')),
	('March',_('March')),
	('April', _('April')),
	('May', _('May')),
	('June',_('June')),
	('July', _('July')),
	('August', _('August')),
	('September',_('September')),
	('October', _('October')),
	('November', _('November')),
	('December',_('December')),
)
YEAR_CHOICES = ( 
	('2012', _('2012')),
	('2013', _('2013')),
	('2014', _('2014')),
	('2015', _('2015')),
	('2016', _('2016')),
	('2017', _('2017')),
	('2018', _('2018')),
	('2019', _('2019')),
	('2020', _('2020')),
	('2021', _('2021')),
)

DAY_CHOICES = ( 
	('01', _('01')),
	('02', _('02')),
	('03', _('03')),
	('04', _('04')),
	('05', _('05')),
	('06', _('06')),
	('07', _('07')),
	('08', _('08')),
	('09', _('09')),
	('10', _('10')),
	('11', _('11')),
	('12', _('12')),
	('13', _('13')),
	('14', _('14')),
	('15', _('15')),
	('16', _('16')),
	('17', _('17')),
	('18', _('18')),
	('19', _('19')),
	('20', _('20')),
	('21', _('21')),
	('22', _('22')),
	('23', _('23')),
	('24', _('24')),
	('25', _('25')),
	('26', _('26')),
	('27', _('27')),
	('28', _('28')),
	('29', _('29')),
	('30', _('30')),
	('31', _('31')),
)
DAILY_CHOICES = ( 
	('CASH', _('CASH')),
	('CHEQUE/DD/ONLINE',_('CHEQUE/DD/ONLINE')),
)

ORGANISATION_CHOICES = (
	('GOVERNMENT', _('GOVERNMENT')),
	('SEMI-GOVERNMENT', _('SEMI-GOVERNMENT')),
	('PRIVATE', _('PRIVATE'))
)
