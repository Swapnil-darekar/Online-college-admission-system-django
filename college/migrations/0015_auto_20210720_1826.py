# Generated by Django 3.1.7 on 2021-07-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0014_auto_20210720_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='hsc_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
