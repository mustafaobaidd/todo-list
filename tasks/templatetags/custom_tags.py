# tasks/templatetags/custom_tags.py
from django import template
from django.utils.safestring import SafeString

register = template.Library()


@register.filter(name='add_class')
def add_class(value, css_class):
    if isinstance(value, SafeString):
        return value
    return value.as_widget(attrs={'class': css_class})
