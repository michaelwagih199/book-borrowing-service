# Generated by Django 5.0.2 on 2024-02-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0010_remove_borrow_guest_borrow_user_delete_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrowDurationFrom',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrowDurationTo',
            field=models.DateField(blank=True),
        ),
    ]
