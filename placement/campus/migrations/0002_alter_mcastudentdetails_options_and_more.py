# Generated by Django 4.1.7 on 2023-02-28 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mcastudentdetails',
            options={'verbose_name_plural': 'STUDENT DETAILS'},
        ),
        migrations.AlterModelOptions(
            name='studentreg',
            options={'verbose_name_plural': 'Registration table'},
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_on', models.DateTimeField()),
                ('email', models.OneToOneField(max_length=70, on_delete=django.db.models.deletion.CASCADE, to='campus.studentreg')),
            ],
        ),
    ]
