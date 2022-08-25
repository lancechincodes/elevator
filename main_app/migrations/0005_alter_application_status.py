# Generated by Django 4.1 on 2022-08-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0004_alter_application_notes_alter_application_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="status",
            field=models.CharField(
                choices=[
                    ("IC", "Incomplete"),
                    ("A", "Applied"),
                    ("I", "Interviewed"),
                    ("O", "Offered"),
                    ("R", "Rejected"),
                ],
                default="IC",
                max_length=2,
            ),
        ),
    ]
