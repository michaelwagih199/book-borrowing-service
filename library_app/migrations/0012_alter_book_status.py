# Generated by Django 5.0.2 on 2024-02-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0011_alter_borrow_borrowdurationfrom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(default='AVAILABLE', max_length=30),
        ),
    ]
