# Generated by Django 5.1.2 on 2024-11-04 07:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baskets", "0001_initial"),
        ("orders", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="amount",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Сумма заказа"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор заказа",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="basket",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="baskets.basket",
                verbose_name="Корзина заказа",
            ),
        ),
    ]
