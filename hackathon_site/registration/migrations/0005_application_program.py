# Generated by Django 3.1.1 on 2020-09-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0004_auto_20200913_2202"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="program",
            field=models.CharField(
                default="other", help_text="Program or Major", max_length=255
            ),
            preserve_default=False,
        ),
    ]
