# Generated by Django 4.1.7 on 2023-05-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0016_mcastudentdetails_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='drives',
            name='file',
            field=models.FileField(default='Not Available', upload_to='DriveFiles', verbose_name='Drive File'),
        ),
    ]