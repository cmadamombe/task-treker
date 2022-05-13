# Generated by Django 4.0.4 on 2022-05-13 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs')], max_length=10, verbose_name='Title')),
                ('staff_phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Staff Phone')),
                ('gender', models.CharField(blank=True, choices=[('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs')], max_length=12, verbose_name='Gender')),
                ('company_name', models.CharField(blank=True, max_length=100, verbose_name='Company Name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, max_length=100, null=True, verbose_name='Physical Address')),
                ('staff_profile_summary', models.TextField(blank=True, max_length=500, null=True, verbose_name='staff Profile Summary')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='client_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='client_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff Profile',
                'verbose_name_plural': 'Staff Profile',
                'ordering': ('user',),
            },
        ),
    ]
