from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("registrationPage", views.registerPage, name="registrationPage"),
    path("addCourse", views.addCourse, name="addCourse"),
    path("removeCourse", views.removeCourse, name="removeCourse"),
    path("classroom", views.classroom, name="classroom"),
    path("createClassroom", views.createClassroom, name="createClassroom"),
    path("classroomPage<int:id>", views.classroomPage, name="classroomPage"),
    path("createAnnouncement", views.createAnnouncement, name="createAnnouncement"),
    path("createAssignment", views.createAssignment, name="createAssignment"),
    path("submitAssignment", views.submitAssignment, name="submitAssignment"),
    path("assignmentSubmission<int:id>", views.assignmentSubmission, name="assignmentSubmission"),
    path("gradeAssignment", views.gradeAssignment, name="gradeAssignment"),
    path("createQuiz", views.createQuiz,name="createQuiz"),
    path("addQuestion", views.addQuestion, name="addQuestion"),
    path("quiz/<int:id>/<int:studentID>", views.quiz, name="quiz"),
    path("quizSubmission<int:id>", views.quizSubmission, name="quizSubmission"),
    path("chat/<int:id>", views.chat, name="chat"),
    path("teacherChat/<int:id>", views.teacherChat, name="teacherChat"),
    path("gradebook/<int:studentID>/<int:courseID>", views.gradebook, name="gradebook"),
    path("editFinal", views.editFinal, name="editFinal"),
    path("editMidterm", views.editMidterm, name="editMidterm"),
    path("finalGrade", views.finalGrade, name="finalGrade"),
]


