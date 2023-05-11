# Generated by Django 3.1.7 on 2021-07-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_remove_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Application_Status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
    ]