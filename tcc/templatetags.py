from models import *

from django import template

register = template.Library()

@register.inclusion_tag("lab_field_select.html")
def lab_field_select():
    lab_list = Lab.objects.all()
    return {'lab_list' : lab_list}
