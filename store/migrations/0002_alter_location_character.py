# Generated by Django 4.1.5 on 2023-01-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="character",
            field=models.CharField(
                blank=True, default=1, max_length=5, verbose_name="Литера"
            ),
            preserve_default=False,
        ),
    ]
