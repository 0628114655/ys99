# Generated by Django 5.0.7 on 2024-10-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_examcorrection_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examcorrection',
            name='section',
        ),
        migrations.AddField(
            model_name='examcorrection',
            name='section',
            field=models.ManyToManyField(to='home.section'),
        ),
    ]
