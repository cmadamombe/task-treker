from django import template
register = template.Library()
from tasktreker.todo.models import Todo


@register.simple_tag
def totaltasks():
    return Todo.objects.all().count()


@register.simple_tag
def completedtasks():
    return Todo.objects.filter(status='Completed').count()


@register.simple_tag
def onholdtasks():
    return Todo.objects.filter(status='On Hold').count()


@register.simple_tag
def cancelledtasks():
    return Todo.objects.filter(status='Cancelled').count()

@register.simple_tag
def inprogresstasks():
    return Todo.objects.filter(status='In Progress').count()

'''
Django offers a powerful way to follow relationships in lookups, taking care of the SQL JOINs automatically behind the scenes.
To span the relationships, use the field name of the the related fields accross the models, separated by double underscores,
until you get to the field you want.
'''
