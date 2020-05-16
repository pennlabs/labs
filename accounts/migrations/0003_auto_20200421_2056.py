# Generated by Django 3.0.3 on 2020-04-22 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20200213_1711"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="graduation_year",
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name="user",
            name="preferred_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
                ),
                ("primary_number", models.BooleanField(default=False)),
                ("verified", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("primary_email", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254)),
                ("verified", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="emails",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
