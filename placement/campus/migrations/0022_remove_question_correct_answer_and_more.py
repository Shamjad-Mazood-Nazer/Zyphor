# Generated by Django 4.1.7 on 2023-05-14 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0021_alter_studentreg_admino_alter_studentreg_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='explanation',
        ),
    ]