from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(StudentReg)
# admin.site.register(Tpo)
# admin.site.register(BTechStudentDetails)
admin.site.register(MCAStudentDetails)
admin.site.register(Drives)
admin.site.register(ApplyDrive)
admin.site.register(Payment)
admin.site.register(QuesModel)
admin.site.register(QuizResult)
# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Quiz)


class AdminAiken(admin.ModelAdmin):
    list_display = ['id', 'name', 'uploaded_on', 'file', 'start_date', 'end_date', 'time']
    ordering = ['id']


# admin.site.register(AikenQuizFormat, AdminAiken)


@admin.register(AikenFile)
class AikenFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_on', 'file', 'start_date', 'end_date', 'time')
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

                answer_text = lines[j].strip()[2:]
                if not answer_text:
                    # Answer text is empty
                    return

                is_correct = lines[j].startswith('ANSWER: ')
                answer = Answer(question=question, text=answer_text, is_correct=is_correct)
                answers.append(answer)
                print(answers)

            if len(answers) == 4:
                Answer.objects.bulk_create(answers)

