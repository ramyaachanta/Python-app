# Generated by Django 3.1.7 on 2021-03-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0007_auto_20210324_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='class_name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]