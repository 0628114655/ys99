# Generated by Django 5.0.7 on 2024-10-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_userprofile_image_alter_userprofile_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCorrection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]