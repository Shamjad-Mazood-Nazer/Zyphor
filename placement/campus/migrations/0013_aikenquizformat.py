# Generated by Django 4.1.7 on 2023-03-12 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0012_alter_quesmodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AikenQuizFormat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='File ID')),
                ('name', models.CharField(max_length=255, verbose_name='File Name')),
                ('uploaded_on', models.DateField(auto_now_add=True, verbose_name='Upload Date')),
                ('file_path', models.FileField(upload_to='files', verbose_name='Path')),
            ],
            options={
                'verbose_name_plural': 'Aiken Quiz File',
            },
        ),
    ]
