# Generated by Django 2.0.3 on 2019-02-07 23:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0012_auto_20190204_2003'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PastOrder',
            new_name='PlacedOrder',
        ),
        migrations.RemoveField(
            model_name='pasta',
            name='item',
        ),
    ]
    atomic = False
