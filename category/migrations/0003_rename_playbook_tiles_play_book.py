# Generated by Django 4.1.3 on 2022-12-09 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiles',
            old_name='playbook',
            new_name='play_book',
        ),
    ]