from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# title choices
TITLE_CHOICES = (
    ('Dr', 'Dr'),
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs')
)

# gender choices
GENDER_CHOICES = (
    ('M', 'M'),
    ('F', 'F')
)


# Create your models here.
class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=15, blank=True, null=True, choices=TITLE_CHOICES, verbose_name='Title')
    client_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Client Phone')
    gender = models.CharField(max_length=12, blank=True, choices=GENDER_CHOICES, verbose_name='Gender')
    company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Company Name')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    address = models.TextField(max_length=100, blank=True, null=True, verbose_name='Physical Address')
    client_profile_summary = models.TextField(max_length=500, blank=True, null=True, verbose_name='staff Profile Summary')
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    #modified_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False, related_name='client_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, verbose_name='Date Modified')

    class Meta:
        """Meta definition for Staff."""
        verbose_name = "Client Profile"
        verbose_name_plural = 'Client Profile'
        ordering = ('user',)

    def __str__(self):
        return '{}'.format(self.user)
