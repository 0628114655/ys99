# Generated by Django 5.0.7 on 2024-09-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
