# Generated by Django 5.0.2 on 2024-02-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_rename_isbowered_book_isavailable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isAvailable',
            field=models.BooleanField(default=True),
        ),
    ]