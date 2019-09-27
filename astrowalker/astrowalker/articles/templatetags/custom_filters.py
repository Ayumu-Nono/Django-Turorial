from django import template

register = template.Library()

@register.filter
def tags(querydict):
    tags = querydict.get('tags1')

    return "" if tags is None else tags
