# Generated by Django 4.1.7 on 2023-03-31 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0002_remove_aiken_result_user_aiken_result_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiken_result',
            name='counter',
            field=models.IntegerField(default=0, verbose_name='counter'),
        ),
    ]