# Generated by Django 2.1 on 2018-12-06 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181206_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='author',
            new_name='writer',
        ),
    ]
