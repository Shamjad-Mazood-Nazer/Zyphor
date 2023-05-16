from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)


# Register your models here.

class StudentRegAdmin(admin.ModelAdmin):
    list_display = ('admino', 'first_name', 'last_name', 'email')
    ordering = ['id']


admin.site.register(StudentReg, StudentRegAdmin)


# admin.site.register(Tpo)

# admin.site.register(BTechStudentDetails)
class MCAStudentDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'universityReg', 'branch', 'DoB', 'gender', 'mobileNoIndian', 'alternativeNo', 'collegeMail',
        'fatherName', 'fatherNo', 'motherName', 'motherNo', 'fullAddress', 'district', 'pincode', 'nationality',
        'planAfterGraduate', 'sslcPer', 'sslcYoP', 'sslcBoard', 'hsePer', 'hseYoP', 'hseBoard', 'nameOfUG', 'ugPer',
        'ugCgpa', 'ugYoP', 'collegeNameUg', 'ugUniversity', 'entranceRank', 'mcaAggregateCgpa', 'mcaPer',
        'activeArrears', 'historyOfArrears', 'examsNotAttended', 'pgUniversity', 'plan_after_graduate',
        'technicalSkills', 'certifications', 'internships', 'workExperience', 'projectGithub', 'linkedIn',
        'achievement', 'languagesKnown',
    )
    ordering = ['id']


admin.site.register(MCAStudentDetails, MCAStudentDetailsAdmin)


class DrivesAdmin(admin.ModelAdmin):
    list_display = (
        'company_name', 'salary_package', 'description', 'ug_percentage', 'pg_percentage', 'cgpa', 'backlog',
        'last_date', 'file')


admin.site.register(Drives, DrivesAdmin)


# admin.site.register(ApplyDrive)
# admin.site.register(Company_Image)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'payment_on', 'transaction_id', 'status')
    ordering = ['id']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Payment, PaymentAdmin)

admin.site.register(QuesModel)
admin.site.register(QuizResult)


# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Quiz)
class Aiken_ResultAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'quiz_name',
        'percent',
        'quiz_taken_on',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Aiken_Result, Aiken_ResultAdmin)


class AdminAiken(admin.ModelAdmin):
    list_display = ['name', 'uploaded_on', 'file', 'start_date', 'end_date', 'time']
    ordering = ['id']


# admin.site.register(AikenQuizFormat, AdminAiken)


@admin.register(AikenFile)
class AikenFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'uploaded_on', 'time', 'start_date', 'end_date', 'file']
    ordering = ['id']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        file_path = obj.file.path
        with open(file_path, 'r') as f:
            lines = f.readlines()

        if len(lines) < 6:
            # File does not have enough lines
            return

        quiz_title = lines[0].strip()
        if not quiz_title:
            # Quiz title is empty
            return

        quiz = Quiz.objects.create(title=quiz_title)
        print(quiz)

        for i in range(1, len(lines), 6):
            if i + 5 > len(lines):
                # Not enough lines left to create another question
                return

            question_text = lines[i].strip()[:]
            if not question_text:
                # Question text is empty
                return

            question = Question.objects.create(quiz=quiz, text=question_text)
            print(question)

            answers = []
            for j in range(i + 1, i + 5):
                if j >= len(lines):
                    # Not enough lines left to create another answer
                    return

                # answer_text = lines[j].strip()[2:]
                answer_text = lines[j].strip()[3:].lstrip('. ')
                if not answer_text:
                    # Answer text is empty
                    return

                print('line[j] : ', lines[j].strip()[3:])
                print('start with : ', lines[j].startswith('*'))

                is_correct = lines[j].startswith('*')
                # print(is_correct)
                answer = Answer(question=question, text=answer_text, is_correct=is_correct)
                answers.append(answer)
                print(answers)

            if len(answers) == 4:
                Answer.objects.bulk_create(answers)

    def has_change_permission(self, request, obj=None):
        return False


import csv
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students data.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Contact Number', 'SSLC Percentage', 'HSE Percentage',
                     'Name of UG', 'UG CGPA', 'UG Percentage', 'MCA Aggregate CGPA', 'MCA Percentage', 'Active Arrears',
                     'History of Arrears', 'Exams Not Attended'])

    for apply_drive in queryset:
        student_reg = apply_drive.user
        mca_details = student_reg.mcastudentdetails

        row = [
            student_reg.first_name,
            student_reg.last_name,
            student_reg.email,
            mca_details.mobileNoIndian,
            mca_details.sslcPer,
            mca_details.hsePer,
            mca_details.nameOfUG,
            mca_details.ugCgpa,
            mca_details.ugPer,
            mca_details.mcaAggregateCgpa,
            mca_details.mcaPer,
            mca_details.activeArrears,
            mca_details.historyOfArrears,
            mca_details.examsNotAttended
        ]

        writer.writerow(row)

    return response


export_to_csv.short_description = "Export selected drives to CSV"


class ApplyDriveAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

    list_display = ['drive_name', 'user', 'applied_on', 'status']
    list_filter = ['drive_name', 'status']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']

    # ... your other admin configurations

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ApplyDrive, ApplyDriveAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'department')
    ordering = ['id']


admin.site.register(Teacher, TeacherAdmin)

# admin.site.register(Department)
