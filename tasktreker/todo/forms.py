from email.policy import default
from django import forms
from django.forms import ModelForm #We import the ModelForm class, which will do all the heavy lifting for us.
from tasktreker.todo.models import Todo
from tasktreker.clients.models import Clients
from tasktreker.staff.models import Staff

PRIORITY_CHOICES = (
    ('Critical', 'Critical'),
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)

STATUS_CHOICES = (
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
    ('On Hold', 'On Hold'),
    ('Continuous', 'Continuous'),
    )

# added type choices 16 May 2022 - Chuck
TYPE_CHOICES = (
    ('Business', 'Business'),
    ('Personal', 'Personal'),
)


class AddTodoForm(ModelForm): #inherits from ModelForm.

    title = forms.CharField(required=True, disabled = False)
    description = forms.CharField(required=True, disabled=False,
                                             widget=forms.Textarea(attrs={'rows': 2, 'cols': 6}))
    status = forms.ChoiceField(required=True, choices=STATUS_CHOICES)
    priority = forms.ChoiceField(required=True, choices=PRIORITY_CHOICES)
    type = forms.ChoiceField(required=True, choices=TYPE_CHOICES)
    client = forms.ModelChoiceField(queryset=Clients.objects.all(), required=True)
    assigned = forms.ModelChoiceField(queryset=Staff.objects.all(), required=True)

    class Meta: #The ModelForm class has an internal Meta class which we use to pass in the metadata options the ModelForm class needs to render our form:
        model = Todo
        fields = ['title', 'description', 'client', 'assigned', 'priority', 'status', 'type']


class UpdateTodoForm(ModelForm): #inherits from ModelForm.

    title = forms.CharField(required=False, disabled = False)
    description = forms.CharField(required=False, disabled=False,
                                             widget=forms.Textarea(attrs={'rows': 2, 'cols': 6}))
    status = forms.ChoiceField(required=False, choices=STATUS_CHOICES)
    priority = forms.ChoiceField(required=False, choices=PRIORITY_CHOICES)
    type = forms.ChoiceField(required=False, choices=TYPE_CHOICES)
    client = forms.ModelChoiceField(queryset=Clients.objects.all(), required=False)
    assigned = forms.ModelChoiceField(queryset=Staff.objects.all(), required=False)
    datecompleted = forms.DateField(input_formats=['%d/%m/%Y'], required=False)

    class Meta: #The ModelForm class has an internal Meta class which we use to pass in the metadata options the ModelForm class needs to render our form:
        model = Todo
        fields = ['title', 'description', 'client', 'assigned', 'priority', 'status', 'type', 'datecompleted']
