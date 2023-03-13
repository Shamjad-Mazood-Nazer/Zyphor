from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm
from django import forms
from django.db import transaction
from .models import *
from django.forms import ModelForm

passwordInputWidget = {
    'password': forms.PasswordInput(),
}


class RegisterForm(forms.ModelForm):
    class Meta:
        model = StudentReg
        fields = '__all__'
        widgets = [passwordInputWidget]


class LoginForm(forms.ModelForm):
    class Meta:
        model = StudentReg
        fields = ['email', 'password']
        widgets = [passwordInputWidget]


class UpdateStudent(forms.ModelForm):
    class Meta:
        model = MCAStudentDetails
        fields = ['branch', 'DoB', 'gender', 'mobileNoIndian', 'alternativeNo', 'collegeMail', 'fatherName',
                  'fatherNo', 'motherName', 'motherNo', 'fullAddress', 'pincode', 'nationality', 'planAfterGraduate',
                  'sslcPer', 'sslcYoP', 'sslcBoard',
                  'hsePer', 'hseYoP', 'hseBoard', 'nameOfUG', 'ugPer', 'ugCgpa', 'ugYoP', 'collegeNameUg',
                  'ugUniversity', 'entranceRank', 'mcaAggregateCgpa',
                  'activeArrears', 'historyOfArrears', 'examsNotAttended', 'pgUniversity', 'technicalSkills',
                  'certifications', 'internships', 'workExperience',
                  'projectGithub', 'linkedIn', 'achievement', 'languagesKnown']


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']


