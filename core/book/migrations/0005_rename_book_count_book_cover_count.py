# Generated by Django 4.2.3 on 2023-07-27 09:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0004_book_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="book_count",
            new_name="cover_count",
        ),
    ]
