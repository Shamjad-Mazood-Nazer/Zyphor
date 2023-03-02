# Generated by Django 4.1.7 on 2023-03-02 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0006_quesmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quesmodel',
            options={'verbose_name_plural': 'Quiz - Questions'},
        ),
        migrations.AlterField(
            model_name='mcastudentdetails',
            name='admino',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campus.studentreg'),
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('time', models.IntegerField()),
                ('correct', models.IntegerField()),
                ('wrong', models.IntegerField()),
                ('percent', models.IntegerField()),
                ('total', models.IntegerField()),
                ('email', models.ManyToManyField(max_length=70, to='campus.studentreg')),
            ],
            options={
                'verbose_name_plural': 'Quiz - Result',
            },
        ),
    ]
