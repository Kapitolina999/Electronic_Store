# Generated by Django 4.1.5 on 2023-01-22 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", models.CharField(max_length=255, verbose_name="Страна")),
                ("city", models.CharField(max_length=255, verbose_name="Город")),
                ("street", models.CharField(max_length=255, verbose_name="Улица")),
                ("number", models.PositiveSmallIntegerField(verbose_name="Номер дома")),
                (
                    "character",
                    models.CharField(max_length=5, null=True, verbose_name="Литера"),
                ),
            ],
            options={
                "verbose_name": "Адрес",
                "verbose_name_plural": "Адреса",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Наименование")),
                ("model", models.CharField(max_length=255, verbose_name="Модель")),
                ("date_release", models.DateField(verbose_name="Дата выхода на рынок")),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукция",
            },
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateField(
                        auto_created=True, verbose_name="Дата регистрации"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название"
                    ),
                ),
                ("email", models.EmailField(max_length=254, null=True, unique=True)),
                (
                    "level",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Завод"),
                            (1, "Дилер"),
                            (2, "Розничный магазин"),
                            (3, "ИП"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=12,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "location",
                    models.ManyToManyField(to="store.location", verbose_name="Адрес"),
                ),
                (
                    "product",
                    models.ManyToManyField(
                        blank=True, to="store.product", verbose_name="Продукция"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="store.store",
                        verbose_name="",
                    ),
                ),
            ],
            options={
                "verbose_name": "Поставщик",
                "verbose_name_plural": "Поставщики",
            },
        ),
    ]
