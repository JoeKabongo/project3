# Generated by Django 2.0.3 on 2019-02-04 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20190202_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastorder',
            name='dinnerplatter',
        ),
        migrations.RemoveField(
            model_name='pastorder',
            name='pasta',
        ),
        migrations.RemoveField(
            model_name='pastorder',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='pastorder',
            name='salad',
        ),
        migrations.RemoveField(
            model_name='pastorder',
            name='sub',
        ),
        migrations.RemoveField(
            model_name='pastorder',
            name='user',
        ),
        migrations.DeleteModel(
            name='PastOrder',
        ),
    ]