# Generated by Django 4.1.5 on 2023-01-07 01:15

import django.contrib.auth.validators
import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.utils.timezone
import users.managers



class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "username",
                    django.contrib.postgres.fields.citext.CICharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.ASCIIUsernameValidator],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                (
                    "email",
                    django.contrib.postgres.fields.citext.CIEmailField(
                        error_messages={"unique": "A user with that email address already exists"},
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of del",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(help_text="Show the last login date and time", verbose_name="last login"),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                (
                    "role",
                    models.CharField(
                        choices=[], help_text="Designates user role in the system", max_length=7, verbose_name="role"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
            managers=[
                ("objects", users.managers.UserManager()),
            ],
        ),
    ]
