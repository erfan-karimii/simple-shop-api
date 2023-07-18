# Generated by Django 4.2.3 on 2023-07-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="book_language",
            field=models.CharField(
                choices=[("fa", "farsi"), ("en", "english")], default="fa", max_length=2
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="published_date",
            field=models.DateField(null=True),
        ),
        migrations.RemoveField(
            model_name="book",
            name="category",
        ),
        migrations.AddField(
            model_name="book",
            name="category",
            field=models.ManyToManyField(to="book.category"),
        ),
    ]
