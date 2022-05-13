# Generated by Django 4.0.4 on 2022-05-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_clients_company_name_alter_clients_modified_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='modified_by',
        ),
        migrations.AlterField(
            model_name='clients',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=12, verbose_name='Gender'),
        ),
    ]
