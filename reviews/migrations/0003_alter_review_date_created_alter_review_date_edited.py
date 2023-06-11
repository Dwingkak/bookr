# Generated by Django 4.1.2 on 2022-12-22 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="date_created",
            field=models.DateTimeField(
                help_text="The date and time the review was created."
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="date_edited",
            field=models.DateTimeField(
                help_text="The date and time the review was last edited.", null=True
            ),
        ),
    ]
