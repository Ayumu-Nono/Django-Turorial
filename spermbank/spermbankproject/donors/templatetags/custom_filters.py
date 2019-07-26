from django import template

register = template.Library()

@register.filter
def color(querydict):
    color = querydict.get('color')

    return "" if color is None else color