from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

User = settings.AUTH_USER_MODEL

payment_choice = (
    ('paid', 'paid'),
    ('not paid', 'not paid'),
)

nationality_choice = (
    ('Indian', 'Indian'),
    ('American', 'American'),
    ('British', 'British'),
    ('Canadian', 'Canadian'),
    ('Australian', 'Australian'),
    ('Bangladeshi', 'Bangladeshi'),
)

sslc_yop_choice = (
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
)

sslc_board_choice = (
    ('CBSE', 'CBSE'),
    ('ICSE', 'ICSE'),
    ('State Board of Kerala', 'State Board of Kerala'),
    ('State Board of Andhra Pradesh', 'State Board of Andhra Pradesh'),
    ('State Board of Tamil Nadu', 'State Board of Tamil Nadu'),
    ('State Board of Karnataka', 'State Board of Karnataka'),
)

hse_yop_choice = (
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
)

hse_board_choice = (
    ('CBSE', 'CBSE'),
    ('HSE', 'HSE'),
    ('ISC', 'ISC'),
    ('VHSE', 'VHSE'),
    ('IHRD', 'IHRD')
)

plan_after_graduate_choice = (
    ('Job', 'Job'),
    ('start-up', 'start-up'),
    ('Higher Studies', 'Higher Studies'),
)

ug_name_choice = (
    ('BCA', 'BCA'),
    ('BBA', 'BBA'),
    ('B.Sc CS', 'B.Sc CS'),
    ('B.Sc Electronics', 'B.Sc Electronics'),
    ('B.Com', 'B.Com'),
)

ug_yop_choices = (
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
)

ug_university_choices = (
    ('APJ KTU', 'APJ KTU'),
    ('Mahatma Gandhi University', 'Mahatma Gandhi University'),
    ('Kannur University', 'Kannur University'),
    ('CUSAT', 'CUSAT'),
    ('University of Kerala', 'University of Kerala'),
    ('National Institute of Technology', 'National Institute of Technology'),
)

pg_university_choice = (
    ('APJ KTU', 'APJ KTU'),
)

district_choice = (
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Kollam', 'Kollam'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Alappuzha', 'Alappuzha'),
    ('Kottayam', 'Kottayam'),
    ('Idukki', 'Idukki'),
    ('Eranakulam', 'Eranakulam'),
    ('Thrissur', 'Thrissur'),
    ('Palakkad', 'Palakkad'),
    ('Kannur', 'Kannur'),
    ('Malappuram', 'Malappuram'),
    ('Wayanad', 'Wayanad'),
    ('Kozhikkodu', 'Kozhikkodu'),
    ('Kasargod', 'Kasargod'),
)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tpo = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)


class StudentReg(models.Model):
    admino = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=500, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Registration table'


# class StudentReg(models.Model):
#     admino = models.CharField(max_length=5, unique=True, default=None)
#     email = models.EmailField(max_length=100, unique=True, null=True)
#     password = models.CharField(max_length=30, null=True)
#
#     def __str__(self):
#         return self.admino


class MCAStudentDetails(models.Model):
    branch = (
        ('mca', 'MCA'),
        ('intmca', 'INT MCA'),
    )
    gender = (
        ('male', 'male'),
        ('female', 'female'),
    )

    user = models.OneToOneField(StudentReg, null=True, blank=True, on_delete=models.CASCADE)
    universityReg = models.CharField(max_length=13, verbose_name='KTU register number')
    branch = models.CharField(max_length=50, choices=branch, verbose_name='Programme')
    DoB = models.DateField(max_length=10, verbose_name='Date of Birth')
    gender = models.CharField(max_length=6, choices=gender, verbose_name='Gender')
    mobileNoIndian = models.CharField(max_length=10, verbose_name='Primary Mobile')
    alternativeNo = models.CharField(max_length=15, verbose_name='Alternative Mobile')
    collegeMail = models.CharField(max_length=200, verbose_name='College Mail')
    fatherName = models.CharField(max_length=50, verbose_name="Father's Name")
    fatherNo = models.CharField(max_length=15, verbose_name="Father's Mobile")
    motherName = models.CharField(max_length=30, verbose_name="Mother's Name")
    motherNo = models.CharField(max_length=15, verbose_name="Mother's Mobile")
    fullAddress = models.CharField(max_length=50, verbose_name='Address')
    district = models.CharField(max_length=50, verbose_name='District', choices=district_choice)
    pincode = models.CharField(max_length=6, verbose_name='Pincode')
    nationality = models.CharField(max_length=15, verbose_name='Nationality', choices=nationality_choice)
    planAfterGraduate = models.CharField(max_length=15, verbose_name='Future Plan')
    sslcPer = models.FloatField(max_length=5, verbose_name='SSLC/10 Percent')
    sslcYoP = models.CharField(max_length=4, verbose_name='SSLC/10 Year of Pass', choices=sslc_yop_choice)
    sslcBoard = models.CharField(max_length=35, verbose_name='SSLC/10 Board', choices=sslc_board_choice)
    hsePer = models.CharField(max_length=5, verbose_name='HSE/12 Percent')
    hseYoP = models.CharField(max_length=4, verbose_name='HSE/12 Year of Pass', choices=hse_yop_choice)
    hseBoard = models.CharField(max_length=30, verbose_name='HSE/12 Board', choices=hse_board_choice)
    nameOfUG = models.CharField(max_length=50, verbose_name='UG Programme', choices=ug_name_choice)
    ugPer = models.CharField(max_length=5, verbose_name='UG Percent')
    ugCgpa = models.CharField(max_length=5, verbose_name='UG CGPA')
    ugYoP = models.CharField(max_length=4, verbose_name='UG Year of Pass', choices=ug_yop_choices)
    collegeNameUg = models.CharField(max_length=50, verbose_name='UG College Name')
    ugUniversity = models.CharField(max_length=50, verbose_name='UG University', choices=ug_university_choices)
    entranceRank = models.CharField(max_length=6, verbose_name='Entrance Rank')
    mcaAggregateCgpa = models.CharField(max_length=4, verbose_name='PG CGPA')
    mcaPer = models.CharField(max_length=5, verbose_name='PG Percent')
    activeArrears = models.CharField(max_length=2, verbose_name='Active Arrears (Count)')
    historyOfArrears = models.CharField(max_length=2, verbose_name='Arrears History(Active + Cleared)')
    examsNotAttended = models.CharField(max_length=2, verbose_name='Exam not Attended (Count)')
    pgUniversity = models.CharField(max_length=50, choices=pg_university_choice, verbose_name='PG University')
    plan_after_graduate = models.CharField(max_length=15, choices=plan_after_graduate_choice)
    technicalSkills = models.CharField(max_length=500)
    certifications = models.CharField(max_length=500)
    internships = models.CharField(max_length=500)
    workExperience = models.CharField(max_length=500)
    projectGithub = models.URLField(max_length=500, verbose_name='GitHub Profile URL')
    linkedIn = models.URLField(max_length=500, verbose_name='LinkedIn Profile URL')
    achievement = models.CharField(max_length=500)
    languagesKnown = models.CharField(max_length=500)
    profile_picture = models.ImageField(upload_to='profile picture', blank=True, verbose_name='Upload Picture')

    def __str__(self):
        return "%s" % self.user

    class Meta:
        verbose_name_plural = 'Student Details'


class BTechStudentDetails(models.Model):
    branch = (
        ('it', 'information_technology'),
        ('me', 'mech'),
        ('ce', 'civil'),
        ('eee', 'eee'),
        ('ece', 'ece'),
        ('ch', 'chemical'),
        ('cse', 'cse'),
    )
    gender = (
        ('male', 'male'),
        ('female', 'female'),
    )

    admino = models.ForeignKey(StudentReg, null=True, blank=True, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50, choices=branch)
    DoB = models.DateField(max_length=10)
    gender = models.CharField(max_length=6, choices=gender)
    mobileNoIndian = models.CharField(max_length=10)
    alternativeNo = models.CharField(max_length=15)
    collegeMail = models.CharField(max_length=200)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=30)
    motherNo = models.CharField(max_length=15)
    fatherNo = models.CharField(max_length=15)
    fullAddress = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    nationality = models.CharField(max_length=15)
    planAfterGraduate = models.CharField(max_length=15)
    sslcPer = models.FloatField(max_length=5)
    sslcYoP = models.CharField(max_length=4)
    sslcBoard = models.CharField(max_length=35)
    hsePer = models.CharField(max_length=5)
    hseYoP = models.CharField(max_length=4)
    hseBoard = models.CharField(max_length=30)
    ugUniversity = models.CharField(max_length=50)
    entranceRank = models.CharField(max_length=6)
    AggregateCgpa = models.CharField(max_length=4)
    activeArrears = models.CharField(max_length=2)
    historyOfArrears = models.CharField(max_length=2)
    examsNotAttended = models.CharField(max_length=2)
    technicalSkills = models.CharField(max_length=500)
    certifications = models.CharField(max_length=500)
    internships = models.CharField(max_length=500)
    workExperience = models.CharField(max_length=500)
    projectGithub = models.URLField(max_length=500)
    linkedIn = models.URLField(max_length=500)
    achievement = models.CharField(max_length=500)
    languagesKnown = models.CharField(max_length=500)

    def __str__(self):
        return "%s" % self.admino


class Drives(models.Model):
    company_name = models.CharField(max_length=50, verbose_name='Name', default='')
    salary_package = models.FloatField(max_length=10, verbose_name='CTC(LPA)', default='')
    description = models.TextField(blank=True, verbose_name='Job Role', default='')
    ug_percentage = models.FloatField(default='60', verbose_name='UG Percent')
    pg_percentage = models.FloatField(default='60', verbose_name='PG Percent')
    cgpa = models.FloatField(default='6', verbose_name='Required CGPA')
    backlog = models.IntegerField(default=0, verbose_name='Backlog Count')
    last_date = models.DateField(verbose_name='Last Date', default='')
    status = models.BooleanField(default=False, verbose_name='Accept Response')

    class Meta:
        verbose_name_plural = 'Drive Details'

    def __str__(self):
        return self.company_name


class ApplyDrive(models.Model):
    drive_name = models.ForeignKey(Drives, verbose_name='Drive Name', on_delete=models.CASCADE)
    user = models.ForeignKey(StudentReg, verbose_name='Student Name', on_delete=models.CASCADE)
    applied_on = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False, verbose_name='Applied')

    def __str__(self):
        return "%s" % self.drive_name

    class Meta:
        verbose_name_plural = "Students Applied Drives"


class Company_Image(models.Model):
    image = models.ImageField(upload_to='company image', verbose_name='Company Image', default='')

    class Meta:
        verbose_name_plural = "Company's Images"


class Payment(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    payment_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default='Not Paid', choices=payment_choice)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Payment Table'


class QuizResult(models.Model):
    email = models.EmailField(max_length=70, default=0)
    score = models.CharField(max_length=3, default=0)
    time = models.CharField(max_length=4, default=0)
    correct = models.CharField(max_length=3, default=0)
    wrong = models.CharField(max_length=3, default=0)
    percent = models.CharField(max_length=3, default=0)
    total = models.CharField(verbose_name='total questions', max_length=3, default=0)
    quiz_taken_on = models.DateTimeField(auto_now_add=True, verbose_name='Date & Time')

    class Meta:
        verbose_name_plural = 'Quiz - Result'

    def __str__(self):
        return self.email


class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    explanation = models.TextField(default='')

    class Meta:
        verbose_name_plural = 'Quick Test'

    def __str__(self):
        return self.question


class AikenQuizFormat(models.Model):
    name = models.CharField(max_length=255, verbose_name='Quiz Name')
    uploaded_on = models.DateField(auto_now_add=True, verbose_name='Upload Date')
    file = models.FileField(upload_to='files', verbose_name='File', default='')
    time = models.CharField(max_length=10, default='10', verbose_name='Time(Minutes)')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Aiken Quiz File'


class AikenFile(models.Model):
    name = models.CharField(max_length=255, verbose_name='Quiz Name', default='')
    uploaded_on = models.DateField(auto_now_add=True, verbose_name='Upload Date')
    file = models.FileField(upload_to='files', verbose_name='File', default='')
    time = models.CharField(max_length=10, default='10', verbose_name='Time(Minutes)')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')

    # attempts = models.IntegerField(verbose_name='Count of Attempts', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Aiken Quiz'


class Quiz(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Quiz'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    explanation = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Questions'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Answers'


class Aiken_Result(models.Model):
    # user = models.ForeignKey(StudentReg, on_delete=models.CASCADE, verbose_name='Student')
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, verbose_name='student email')
    score = models.CharField(max_length=3, default=0, verbose_name='Score')
    quiz_name = models.CharField(max_length=255, verbose_name='Name of Quiz')
    time = models.CharField(max_length=4, default=0, verbose_name='Time')
    correct = models.CharField(max_length=3, default=0, verbose_name='correct')
    wrong = models.CharField(max_length=3, default=0, verbose_name='Wrong')
    percent = models.CharField(max_length=3, default=0, verbose_name='Percent')
    total = models.CharField(verbose_name='total questions', max_length=3, default=0)
    quiz_taken_on = models.DateTimeField(auto_now_add=True, verbose_name='Date & Time')
    counter = models.IntegerField(verbose_name='counter', default=0)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Aiken Quiz Result'


class Quiz_Counter(models.Model):
    email = models.EmailField(max_length=255, verbose_name='email')
    quiz_id = models.ForeignKey(Quiz, verbose_name='quiz id', on_delete=models.CASCADE)
    counter = models.IntegerField(default=1, verbose_name='counter')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Quiz Counter'


class Message(models.Model):
    sender = models.ForeignKey(StudentReg, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Message'

