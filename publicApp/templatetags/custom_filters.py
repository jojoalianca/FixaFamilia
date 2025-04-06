from django import template

register = template.Library()

@register.filter
def intcomma(value):
    """Add commas to an integer."""
    if value is None:
        return ''
    return "{:,}".format(value)