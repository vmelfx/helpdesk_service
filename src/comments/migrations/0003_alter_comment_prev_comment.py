# Generated by Django 4.1.5 on 2023-02-11 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0002_comment_prev_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="prev_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="next",
                to="comments.comment",
            ),
        ),
    ]