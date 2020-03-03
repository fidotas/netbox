# Generated by Django 2.2.10 on 2020-03-03 16:59

from django.db import migrations, models
import utilities.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0098_devicetype_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powerfeed',
            name='voltage',
            field=models.SmallIntegerField(default=120, validators=[utilities.validators.ExclusionValidator([0])]),
        ),
    ]
