# Generated by Django 4.0.4 on 2022-05-13 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0004_alter_staff_gender'),
        ('clients', '0004_remove_clients_created_by_remove_clients_modified_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
                ('datecompleted', models.DateTimeField(blank=True, null=True, verbose_name='Date Completed')),
                ('priority', models.CharField(choices=[('Critical', 'Critical'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=100, verbose_name='Priority')),
                ('status', models.CharField(choices=[('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold')], default='null', max_length=100, verbose_name='Status')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff', verbose_name='Assigned')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clients', verbose_name='Client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
            ],
            options={
                'verbose_name': 'Todo Profile',
                'verbose_name_plural': 'Todo Profiles',
                'ordering': ('title',),
            },
        ),
    ]
