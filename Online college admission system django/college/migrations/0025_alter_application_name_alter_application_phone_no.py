# Generated by Django 4.0.6 on 2022-07-26 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0024_auto_20210727_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]