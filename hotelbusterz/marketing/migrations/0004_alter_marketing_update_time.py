# Generated by Django 5.0.6 on 2024-07-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("marketing", "0003_marketing_update_time_alter_marketing_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marketing",
            name="update_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
