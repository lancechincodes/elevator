# Generated by Django 4.1 on 2022-08-22 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("company", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("application_url", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("IP", "In Progress"),
                            ("A", "Applied"),
                            ("I", "Interviewed"),
                            ("O", "Offered"),
                            ("R", "Rejected"),
                        ],
                        default="IP",
                        max_length=2,
                    ),
                ),
                ("date_applied", models.DateField(verbose_name="date applied")),
                ("notes", models.TextField(max_length=500)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
