# Generated by Django 4.1.2 on 2022-12-20 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                (
                    "title",
                    models.CharField(help_text="The title of the book.", max_length=70),
                ),
                (
                    "publication_date",
                    models.DateField(verbose_name="Date the book was published."),
                ),
                (
                    "isbn",
                    models.CharField(
                        max_length=20, verbose_name="ISBN number of the book"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contributor",
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
                (
                    "first_names",
                    models.CharField(
                        help_text="The contributor's first name or names.",
                        max_length=50,
                    ),
                ),
                (
                    "last_names",
                    models.CharField(
                        help_text="The contributors's  last names or names.",
                        max_length=50,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="The contact email for the contributor",
                        max_length=254,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
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
                (
                    "name",
                    models.CharField(
                        help_text="The name of the Publishers.", max_length=50
                    ),
                ),
                ("website", models.URLField(help_text="The Publisher's website.")),
                (
                    "email",
                    models.EmailField(
                        help_text="The Publisher's email address.", max_length=254
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookContributor",
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
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("AUTHOR", "Author"),
                            ("CO_AUTHOR", "Co-Author"),
                            ("EDITOR", "Editor"),
                        ],
                        max_length=20,
                        verbose_name="The role this contributor had in the book",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="reviews.book"
                    ),
                ),
                (
                    "contributor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reviews.contributor",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="contributors",
            field=models.ManyToManyField(
                through="reviews.BookContributor", to="reviews.contributor"
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reviews.publisher"
            ),
        ),
    ]