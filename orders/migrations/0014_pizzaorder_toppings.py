# Generated by Django 2.0.3 on 2019-02-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20190207_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzaorder',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='pizza_topping', to='orders.Topping'),
        ),
    ]
