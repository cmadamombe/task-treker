from tasktreker.todo.models import Todo
import django_filters


class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    # year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
    # widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Todo
        fields = ['title', 'description', 'client', 'priority', 'status', 'type', 'assigned']
