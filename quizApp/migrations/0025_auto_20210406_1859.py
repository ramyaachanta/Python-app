# Generated by Django 3.1.7 on 2021-04-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0024_auto_20210406_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takes',
            name='times_taken',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]