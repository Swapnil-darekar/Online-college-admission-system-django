# Generated by Django 3.1.7 on 2021-07-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application_status',
            name='condition',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], max_length=100, null=True),
        ),
    ]
