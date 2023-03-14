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
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)


class AdminAiken(admin.ModelAdmin):
    list_display = ['id', 'name', 'uploaded_on', 'file']
    ordering = ['id']


admin.site.register(AikenQuizFormat, AdminAiken)
