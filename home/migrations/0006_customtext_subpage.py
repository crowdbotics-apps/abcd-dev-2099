# Generated by Django 2.2.11 on 2020-03-23 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_auto_20200323_1110"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="subpage",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customtext_subpage",
                to="home.CustomText",
            ),
        ),
    ]
