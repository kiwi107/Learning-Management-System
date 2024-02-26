from django.contrib import admin
from . models import * 

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Major)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Assignment)
admin.site.register(GradeBook)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuizSubmission)
admin.site.register(StudentAnswer)
admin.site.register(AssignmentSubmission)
admin.site.register(Announcement)
admin.site.register(Chat)
admin.site.register(Message)



