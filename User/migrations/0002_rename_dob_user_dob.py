# Generated by Django 3.2 on 2021-04-07 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='DOB',
            new_name='dob',
        ),
    ]
