# Generated by Django 5.2 on 2025-05-27 22:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kit", "0002_alter_kit_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="kit",
            options={"ordering": ["-date_published"]},
        ),
        migrations.RenameField(
            model_name="question",
            old_name="question_text",
            new_name="question",
        ),
        migrations.AddField(
            model_name="kit",
            name="date_last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="kit",
            name="date_published",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="kit",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
