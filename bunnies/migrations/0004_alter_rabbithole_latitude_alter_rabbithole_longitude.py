# Generated by Django 4.2 on 2023-04-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bunnies", "0003_auto_20230423_0913"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rabbithole",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="rabbithole",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
