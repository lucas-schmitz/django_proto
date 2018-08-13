# Generated by Django 2.1 on 2018-08-13 16:29

from django.db import migrations, models
import django_proto.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bokeh_plots', '0002_auto_20180811_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bokeh',
            name='script',
            field=models.FileField(upload_to='bokeh_scripts/', validators=[django_proto.validators.is_python]),
        ),
    ]
