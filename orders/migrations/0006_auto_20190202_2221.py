# Generated by Django 2.0.3 on 2019-02-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_pastorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastorder',
            name='total_price',
            field=models.FloatField(),
        ),
    ]
