# Generated by Django 3.1.7 on 2021-03-21 05:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0005_auto_20210320_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_n_mark',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-250), django.core.validators.MaxValueValidator(0)]),
        ),
    ]