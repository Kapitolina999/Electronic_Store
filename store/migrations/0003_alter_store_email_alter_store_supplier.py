# Generated by Django 4.1.5 on 2023-01-22 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_alter_location_character"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="email",
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="store",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="store.store",
                verbose_name="Поставщик",
            ),
        ),
    ]