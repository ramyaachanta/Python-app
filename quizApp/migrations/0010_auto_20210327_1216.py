# Generated by Django 3.1.7 on 2021-03-27 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0009_auto_20210326_1124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Option', 'verbose_name_plural': 'Options'},
        ),
        migrations.AlterModelOptions(
            name='belongs',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterModelOptions(
            name='clas',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='options',
            options={'verbose_name': 'Selected Option', 'verbose_name_plural': 'Selected Options'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['id'], 'verbose_name': 'Quiz', 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AlterModelOptions(
            name='teaches',
            options={'verbose_name': 'Assigned Faculty', 'verbose_name_plural': 'Assigned Faculty'},
        ),
        migrations.AlterModelOptions(
            name='usert',
            options={'verbose_name': 'User Type', 'verbose_name_plural': 'User Type'},
        ),
        migrations.AlterUniqueTogether(
            name='teaches',
            unique_together={('user', 'clas', 'course')},
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notification_txt', models.CharField(max_length=255)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quizApp.usert')),
            ],
        ),
    ]