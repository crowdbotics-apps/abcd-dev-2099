# Generated by Django 2.2.11 on 2020-03-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_hmhmkhh"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="hmhmkhh",),
        migrations.AddField(
            model_name="user",
            name="test",
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
