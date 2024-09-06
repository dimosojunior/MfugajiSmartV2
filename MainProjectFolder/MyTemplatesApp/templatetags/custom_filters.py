from django import template
from datetime import timedelta
from django.utils.timezone import now

register = template.Library()

@register.filter
def timesince_days(value):
    if not value:
        return ''
    delta = now() - value
    days = delta.days
    return f"Siku: {days}" if days > 0 else "0"
