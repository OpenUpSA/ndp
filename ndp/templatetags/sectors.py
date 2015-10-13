from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(needs_autoescape=True)
def goallist(s, autoescape=True):
    result = []
    for line in (l.strip() for l in s.split('\n')):
        if line:
            if autoescape:
                line = conditional_escape(line)
            result.append('<li>%s</li>' % line)

    return mark_safe('\n'.join(result))
