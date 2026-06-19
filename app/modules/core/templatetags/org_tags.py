from django import template

register = template.Library()


@register.inclusion_tag('partials/org_subtree.html')
def render_children(unit):
    return {'children': unit.children.all()}
