from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from tasktreker.staff.models import Staff
from tasktreker.clients.models import Clients

# Create your models here.

class Todo(models.Model):


    PRIORITY_CHOICES = (
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    STATUS_CHOICES = (
       ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
         ('On Hold', 'On Hold'),
    )

    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(max_length=100, blank=True, verbose_name='Description')
    datecompleted = models.DateTimeField(null = True, blank=True, verbose_name='Date Completed')
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, verbose_name='Priority')
    status = models.CharField(max_length=100, default= 'null', choices=STATUS_CHOICES, verbose_name='Status')
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Client')
    assigned = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='Assigned')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, verbose_name='Date Modified')

    class Meta:
        """Meta definition for Todo"""
        verbose_name = "Todo Profile"
        verbose_name_plural = 'Todo Profiles'
        ordering = ('title',)

    def __str__(self):
        return '{}'.format(self.title)


