# Generated by Django 4.1.7 on 2023-03-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0004_rename_admino_mcastudentdetails_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aikenfile',
            name='attempts',
            field=models.IntegerField(default=1, verbose_name='Count of Attempts'),
        ),
    ]
