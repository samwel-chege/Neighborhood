# Generated by Django 3.2.7 on 2021-09-29 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0008_rename_admin_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='admin',
            new_name='profile',
        ),
    ]
