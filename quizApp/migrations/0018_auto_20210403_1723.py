# Generated by Django 3.1.7 on 2021-04-03 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0017_auto_20210403_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makes',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makers', to='quizApp.quiz'),
        ),
    ]