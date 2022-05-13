# Generated by Django 4.0.4 on 2022-05-13 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0002_alter_clients_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='modified_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='title',
            field=models.CharField(blank=True, choices=[('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs')], max_length=15, null=True, verbose_name='Title'),
        ),
    ]
