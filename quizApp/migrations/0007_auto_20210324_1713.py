# Generated by Django 3.1.7 on 2021-03-24 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0006_auto_20210321_1046'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'answer_text')},
        ),
    ]