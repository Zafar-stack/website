from django import template
from django.template.defaultfilters import date

register = template.Library()

@register.filter
def to_int(value):
    if value == value * 1.0:
        return int(value)
    else:
        return value



@register.filter
def lifespan(val):
    if val:
        month = val.strftime("%m")
        month_array = {1: "Jan",
                 2: "Feb",
                 3: "Mar",
                 4: "Apr",
                 5: "May",
                 6: "June",
                 7: "July",
                 8: "Aug",
                 9: "Sep",
                 10: "Oct",
                 11: "Nov",
                 12: "Dec",
                 }
        return val.strftime("%d ") + month_array[int(month)]
    else:
        return ''


register.filter("lifespan", lifespan)
register.filter("to_int", to_int)
