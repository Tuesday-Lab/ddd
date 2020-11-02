# Generated by Django 3.1 on 2020-11-02 17:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EventModel",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(unique=True)),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("NORMAL", "Normal"),
                            ("EDU", "Edu"),
                            ("PROMOTION", "Promotion"),
                        ],
                        default="NORMAL",
                        max_length=10,
                    ),
                ),
                ("start_time", models.DateTimeField(null=True)),
                ("end_time", models.DateTimeField(null=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=11)),
                ("currency", models.CharField(max_length=3)),
                ("max_attendee_count", models.IntegerField()),
                ("main_image", models.FilePathField()),
                ("description", models.TextField()),
                ("registrable_time", models.DateTimeField(null=True)),
                ("is_visible", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "event",
            },
        ),
    ]
