# Generated by Django 4.1.7 on 2023-04-18 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0009_alter_mcastudentdetails_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applydrive',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus.studentreg', verbose_name='Student Name'),
        ),
    ]
