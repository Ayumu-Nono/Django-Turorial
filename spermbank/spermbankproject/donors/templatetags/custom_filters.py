from django import template

register = template.Library()

@register.filter
def color(querydict):
    color = querydict.get('color1')

    return "" if color is None else color

# def height(querydict):
#     height = querydict.get('heght')

#     return "" if height is None else height