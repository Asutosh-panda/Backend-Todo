# Generated by Django 3.1.6 on 2021-03-23 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_userlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlist',
            old_name='passwod1',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='userlist',
            old_name='passwod2',
            new_name='password2',
        ),
    ]