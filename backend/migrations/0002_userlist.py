# Generated by Django 3.1.6 on 2021-03-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('passwod1', models.CharField(max_length=122)),
                ('passwod2', models.CharField(max_length=122)),
            ],
        ),
    ]
