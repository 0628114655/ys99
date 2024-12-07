# Generated by Django 5.0.7 on 2024-10-08 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_examcorrection_margin1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lasstname', models.CharField(max_length=50)),
                ('studentid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.DecimalField(decimal_places=4, max_digits=4)),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.section')),
            ],
        ),
    ]
