# Generated by Django 4.2.4 on 2023-08-23 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='create_att',
            new_name='create_at',
        ),
    ]
