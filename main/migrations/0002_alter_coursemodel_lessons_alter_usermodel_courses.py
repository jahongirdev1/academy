# Generated by Django 5.1.1 on 2024-09-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='lessons',
            field=models.ManyToManyField(blank=True, related_name='courses', to='main.lessonmodel'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='main.coursemodel'),
        ),
    ]
