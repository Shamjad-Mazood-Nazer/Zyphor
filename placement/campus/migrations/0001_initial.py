# Generated by Django 4.1.7 on 2023-03-21 03:43

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AikenQuizFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='File Name')),
                ('uploaded_on', models.DateField(auto_now_add=True, verbose_name='Upload Date')),
                ('file', models.FileField(default='', upload_to='files', verbose_name='File')),
                ('time', models.CharField(default='10', max_length=10, verbose_name='Time(Minutes)')),
            ],
            options={
                'verbose_name_plural': 'Aiken Quiz File',
            },
        ),
        migrations.CreateModel(
            name='ApplyDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('full_name', models.CharField(max_length=50)),
                ('job_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Students Applied',
            },
        ),
        migrations.CreateModel(
            name='Drives',
            fields=[
                ('drive_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('salary_package', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
                ('last_date', models.DateField()),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Company Details',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('payment_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Payment Table',
            },
        ),
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=0, max_length=70)),
                ('score', models.CharField(default=0, max_length=3)),
                ('time', models.CharField(default=0, max_length=4)),
                ('correct', models.CharField(default=0, max_length=3)),
                ('wrong', models.CharField(default=0, max_length=3)),
                ('percent', models.CharField(default=0, max_length=3)),
                ('total', models.CharField(default=0, max_length=3, verbose_name='total questions')),
            ],
            options={
                'verbose_name_plural': 'Quiz - Result',
            },
        ),
        migrations.CreateModel(
            name='StudentReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admino', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=500, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Registration table',
            },
        ),
        migrations.CreateModel(
            name='Tpo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpoName', models.CharField(max_length=50)),
                ('tpoMail', models.EmailField(max_length=75)),
                ('tpoPassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MCAStudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('mca', 'MCA'), ('intmca', 'INT MCA')], max_length=50)),
                ('DoB', models.DateField(max_length=10)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
                ('mobileNoIndian', models.CharField(max_length=10)),
                ('alternativeNo', models.CharField(max_length=15)),
                ('collegeMail', models.CharField(max_length=200)),
                ('fatherName', models.CharField(max_length=50)),
                ('fatherNo', models.CharField(max_length=15)),
                ('motherName', models.CharField(max_length=30)),
                ('motherNo', models.CharField(max_length=15)),
                ('fullAddress', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('nationality', models.CharField(max_length=15)),
                ('planAfterGraduate', models.CharField(max_length=15)),
                ('sslcPer', models.FloatField(max_length=5)),
                ('sslcYoP', models.CharField(max_length=4)),
                ('sslcBoard', models.CharField(max_length=35)),
                ('hsePer', models.CharField(max_length=5)),
                ('hseYoP', models.CharField(max_length=4)),
                ('hseBoard', models.CharField(max_length=30)),
                ('nameOfUG', models.CharField(max_length=10)),
                ('ugPer', models.CharField(max_length=5)),
                ('ugCgpa', models.CharField(max_length=5)),
                ('ugYoP', models.CharField(max_length=4)),
                ('collegeNameUg', models.CharField(max_length=50)),
                ('ugUniversity', models.CharField(max_length=50)),
                ('entranceRank', models.CharField(max_length=6)),
                ('mcaAggregateCgpa', models.CharField(max_length=4)),
                ('activeArrears', models.CharField(max_length=2)),
                ('historyOfArrears', models.CharField(max_length=2)),
                ('examsNotAttended', models.CharField(max_length=2)),
                ('pgUniversity', models.CharField(max_length=50)),
                ('technicalSkills', models.CharField(max_length=500)),
                ('certifications', models.CharField(max_length=500)),
                ('internships', models.CharField(max_length=500)),
                ('workExperience', models.CharField(max_length=500)),
                ('projectGithub', models.URLField(max_length=500)),
                ('linkedIn', models.URLField(max_length=500)),
                ('achievement', models.CharField(max_length=500)),
                ('languagesKnown', models.CharField(max_length=500)),
                ('admino', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campus.studentreg')),
            ],
            options={
                'verbose_name_plural': 'STUDENT DETAILS',
            },
        ),
        migrations.CreateModel(
            name='BTechStudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('it', 'information_technology'), ('me', 'mech'), ('ce', 'civil'), ('eee', 'eee'), ('ece', 'ece'), ('ch', 'chemical'), ('cse', 'cse')], max_length=50)),
                ('DoB', models.DateField(max_length=10)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
                ('mobileNoIndian', models.CharField(max_length=10)),
                ('alternativeNo', models.CharField(max_length=15)),
                ('collegeMail', models.CharField(max_length=200)),
                ('fatherName', models.CharField(max_length=50)),
                ('motherName', models.CharField(max_length=30)),
                ('motherNo', models.CharField(max_length=15)),
                ('fatherNo', models.CharField(max_length=15)),
                ('fullAddress', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('nationality', models.CharField(max_length=15)),
                ('planAfterGraduate', models.CharField(max_length=15)),
                ('sslcPer', models.FloatField(max_length=5)),
                ('sslcYoP', models.CharField(max_length=4)),
                ('sslcBoard', models.CharField(max_length=35)),
                ('hsePer', models.CharField(max_length=5)),
                ('hseYoP', models.CharField(max_length=4)),
                ('hseBoard', models.CharField(max_length=30)),
                ('ugUniversity', models.CharField(max_length=50)),
                ('entranceRank', models.CharField(max_length=6)),
                ('AggregateCgpa', models.CharField(max_length=4)),
                ('activeArrears', models.CharField(max_length=2)),
                ('historyOfArrears', models.CharField(max_length=2)),
                ('examsNotAttended', models.CharField(max_length=2)),
                ('technicalSkills', models.CharField(max_length=500)),
                ('certifications', models.CharField(max_length=500)),
                ('internships', models.CharField(max_length=500)),
                ('workExperience', models.CharField(max_length=500)),
                ('projectGithub', models.URLField(max_length=500)),
                ('linkedIn', models.URLField(max_length=500)),
                ('achievement', models.CharField(max_length=500)),
                ('languagesKnown', models.CharField(max_length=500)),
                ('admino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campus.studentreg')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_tpo', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
