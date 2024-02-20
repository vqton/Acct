from django import template
register = template.Library()

@register.filter(name='spacefilter')
def space(value, spaces):
    # Convert the value to a string
    value = str(value)
    # Repeat the space character the number of times specified by spaces
    spaces = " " * int(spaces)
    # Return the value with the spaces added
    return spaces + value
