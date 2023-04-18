# Generated by Django 4.1.7 on 2023-04-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0006_mcastudentdetails_plan_after_graduate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drives',
            name='pg_percentage',
            field=models.FloatField(default='60', verbose_name='PG Percent'),
        ),
        migrations.AlterField(
            model_name='drives',
            name='ug_percentage',
            field=models.FloatField(default='60', verbose_name='UG Percent'),
        ),
    ]