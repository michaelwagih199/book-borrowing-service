# Generated by Django 5.0.2 on 2024-02-23 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_book_remove_todo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isBowered',
            new_name='isAvailable',
        ),
    ]