# Generated by Django 4.1.7 on 2023-05-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0023_department_mcastudentdetails_class_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcastudentdetails',
            name='class_name',
            field=models.CharField(choices=[('RMCA-A', 'RMCA-A'), ('RMCA-B', 'RMCA-B'), ('INT-MCA', 'INT-MCA')], max_length=20, verbose_name='Class Name'),
        ),
    ]