# Generated by Django 4.1 on 2022-08-25 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0005_alter_application_status"),
    ]

    operations = [
        migrations.RemoveField(model_name="application", name="status",),
    ]