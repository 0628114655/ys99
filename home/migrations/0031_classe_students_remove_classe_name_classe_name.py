# Generated by Django 5.0.7 on 2024-10-12 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='students',
            field=models.ManyToManyField(to='home.student'),
        ),
        migrations.RemoveField(
            model_name='classe',
            name='name',
        ),
        migrations.AddField(
            model_name='classe',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.section'),
        ),
    ]
