# Generated by Django 3.1.7 on 2021-04-06 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0020_auto_20210406_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makes',
            name='status',
        ),
    ]
