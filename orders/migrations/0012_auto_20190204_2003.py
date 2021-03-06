# Generated by Django 2.0.3 on 2019-02-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20190204_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dinnerplatter',
            name='item',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='item',
        ),
        migrations.RemoveField(
            model_name='sub',
            name='item',
        ),
        migrations.AddField(
            model_name='dinnerplatterorder',
            name='item',
            field=models.CharField(default='Dinner Platter', max_length=65),
        ),
        migrations.AddField(
            model_name='pastaorder',
            name='item',
            field=models.CharField(default='Pasta', max_length=65),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='item',
            field=models.CharField(default='Pizza', max_length=65),
        ),
        migrations.AddField(
            model_name='saladorder',
            name='item',
            field=models.CharField(default='Salad', max_length=65),
        ),
        migrations.AddField(
            model_name='suborder',
            name='item',
            field=models.CharField(default='Sub', max_length=65),
        ),
    ]
