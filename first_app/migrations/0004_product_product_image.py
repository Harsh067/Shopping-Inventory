# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-15 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20181015_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_Image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/%Y/%m/%D/'),
        ),
    ]
