# Generated by Django 4.1.7 on 2023-05-10 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0020_payment_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreg',
            name='admino',
            field=models.CharField(max_length=255, unique=True, verbose_name='Admission Number'),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='email',
            field=models.EmailField(max_length=500, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Last Name'),
        ),
    ]