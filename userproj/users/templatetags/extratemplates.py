from django import template

register = template.Library()

def axo (value,arg):
    if arg == 'a':
        return value[:-1].replace(arg,"e")

register.filter('axO',axo)
