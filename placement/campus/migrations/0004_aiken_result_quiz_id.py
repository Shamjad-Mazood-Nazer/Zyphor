# Generated by Django 4.1.7 on 2023-03-31 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0003_alter_aiken_result_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='aiken_result',
            name='quiz_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='campus.quiz'),
            preserve_default=False,
        ),
    ]