# Generated by Django 5.0.6 on 2024-07-05 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountLog",
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
                ("action", models.CharField(default="VIEW_HOME", max_length=64)),
                ("action_time", models.CharField(max_length=64)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
            ],
            options={
                "db_table": "account_log",
            },
        ),
    ]