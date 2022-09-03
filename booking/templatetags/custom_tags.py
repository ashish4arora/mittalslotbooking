from django import template
from courts.models import Courts
register = template.Library()

@register.simple_tag
def waitlist(value, arg):
    return value.bookings.filter(court = Courts.objects.get(courtname = arg)).count()

@register.simple_tag
def waitlistcourt(value, arg):
    return value.bookings.filter(court = arg).count()