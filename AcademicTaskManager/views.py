import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from AcademicTaskManager.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.paginator import Paginator
from datetime import datetime


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.type=="Student":
            classrooms=Classroom.objects.filter(students=request.user)
            studentAnnouncements=[]
            announcements=Announcement.objects.all().order_by('-date')
            for announcement in announcements:
                if announcement.classroom in classrooms:
                    studentAnnouncements.append(announcement)
            
            
            announcementPaginator = Paginator(studentAnnouncements, 4)
            announcement_page_number = request.GET.get('announcement_page')
            announcement_page_obj = announcementPaginator.get_page(announcement_page_number)
            announcements_page_range = announcementPaginator.page_range

            studentAssignments = []
            assignments=Assignment.objects.all().order_by('-dueDate')
            for assignment in assignments:
                if assignment.classroom in classrooms:
                    studentAssignments.append(assignment)

            assignmentPaginator = Paginator(studentAssignments, 4)
            assignment_page_number = request.GET.get('assignment_page')
            assignment_page_obj = assignmentPaginator.get_page(assignment_page_number)
            assignments_page_range = assignmentPaginator.page_range


            quizzes=Quiz.objects.all()
            studentQuizzes=[]
            for quiz in quizzes:
                if quiz.classroom in classrooms:
                    studentQuizzes.append(quiz)
            
            quizPaginator = Paginator(studentQuizzes, 4)
            quiz_page_number = request.GET.get('quiz_page')
            quiz_page_obj = quizPaginator.get_page(quiz_page_number)
            quizzes_page_range = quizPaginator.page_range

        else:
            return HttpResponseRedirect(reverse("classroom"))


        return render(request, "AcademicTaskManager/index.html",{"announcements": announcement_page_obj,
                                                                 "announcements_page_range": announcements_page_range,
                                                                 "assignments": assignment_page_obj,
                                                                 "assignments_page_range": assignments_page_range,
                                                                 "quizzes": quiz_page_obj,
                                                                 "quizzes_page_range": quizzes_page_range,
                                                                 })
    else:
        return render(request, "AcademicTaskManager/Login.html")

        
   




def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "AcademicTaskManager/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "AcademicTaskManager/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    majors = Major.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        type = request.POST["type"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "AcademicTaskManager/register.html", {
                "message": "Passwords must match."
            })
        
        if type == "Student":
            year = request.POST["year"]
            major = request.POST["major"]
            major = Major.objects.get(name=major)
            

            try:
                user = Student.objects.create_user(username, email, password,type=type, year=year, major=major)
                user.save()
            except IntegrityError:
                return render(request, "AcademicTaskManager/register.html", {
                    "message": "Username already taken."
                })
        else:
            try:
                user = Teacher.objects.create_user(username, email, password,type=type)
                user.save()
            except IntegrityError:
                return render(request, "AcademicTaskManager/register.html", {
                    "message": "Username already taken."
                })
    
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "AcademicTaskManager/register.html",{
            "majors": majors,

        })

@login_required(login_url='/login', redirect_field_name="/profile")
def profile(request):
    user = request.user
    if user.type == "Student":
        gradebooks=GradeBook.objects.filter(student=user)
        student = Student.objects.get(username=user.username)
        passedCreditHours = 0
        for course in gradebooks:
            if course.passed:   
                passedCreditHours=passedCreditHours+course.course.creditHours


        return render(request, "AcademicTaskManager/Profile.html",{
            "user": student,
            "passedCreditHours": passedCreditHours,
            "gradebooks": gradebooks,
        })
    else:
        teacher = Teacher.objects.get(username=user.username)
        return render(request, "AcademicTaskManager/Profile.html",{
            "user": teacher,
        })
    

            
    

def registerPage(request):
    registerdCourses=Student.objects.get(username=request.user.username).registeredCourses.all()
    availableCourses = Course.objects.all()
    userMajor = Student.objects.get(username=request.user.username).major

    classrooms= Classroom.objects.all()
    classroomCourses = []
    for classroom in classrooms:
        classroomCourses.append(classroom.course)
    

    for course in registerdCourses:
        availableCourses = availableCourses.exclude(code=course.code)

    for course in availableCourses:
        if userMajor not in course.major.all():
            availableCourses = availableCourses.exclude(code=course.code)
    
    for course in availableCourses:
        if course not in classroomCourses :
             availableCourses = availableCourses.exclude(code=course.code)
    
    return render(request, "AcademicTaskManager/registrationPage.html",{
        "availableCourses": availableCourses,
        "registerdCourses": registerdCourses,
        })


def addCourse(request):
    user = request.user
    user = Student.objects.get(username=user.username)
    if user.type == "Student":
       if request.method == "POST":
           data = json.loads(request.body)
           course = Course.objects.get(pk=data.get("id", ""))
           classroom = Classroom.objects.get(course=course)
           classroom.students.add(user)
           classroom.save()
           user.registeredCourses.add(course)
           user.save()
           gradebook=GradeBook.objects.create(student=user,course=course)
           gradebook.save()
           return JsonResponse({"message": "Course added successfully."}, status=201)
   
               
          
         
           
       

def removeCourse(request):
    user = request.user
    user = Student.objects.get(username=user.username)

    if user.type == "Student":
       if request.method == "POST":
           data = json.loads(request.body)
           course = Course.objects.get(pk=data.get("id", ""))
           user.registeredCourses.remove(course)
           user.save()
           classroom = Classroom.objects.get(course=course)
           classroom.students.remove(user)
           classroom.save()
           gradebook=GradeBook.objects.get(student=user,course=course)
           gradebook.delete()
        
           return JsonResponse({"message": "Course removed successfully."}, status=201)
       
@login_required(login_url='/login')
def classroom(request):
    user = request.user
    if user.type == "Teacher":
        teacher = Teacher.objects.get(username=user.username)
        courses = teacher.courses.all()
        classrooms = Classroom.objects.filter(teacher=teacher)
       
        return render(request, "AcademicTaskManager/classroom.html",{
                  "courses": courses,
                  "classrooms": classrooms,})
    else:
        student = Student.objects.get(username=user.username)
        classrooms = Classroom.objects.filter(students=student)
        return render(request, "AcademicTaskManager/classroom.html",{ "classrooms": classrooms,})
    
        
   

def createClassroom(request):
    user=request.user
    if user.type == "Teacher":
        if request.method == "POST":
            data = json.loads(request.body)
            course = Course.objects.get(name=data.get("course", ""))
            teacher = Teacher.objects.get(username=user.username)
            semester = data.get("semester", "")
            classroom=Classroom.objects.create(course=course, teacher=teacher, semester=semester)
            classroom.save()
            serialized_classroom = classroom.serialize()
            return JsonResponse({"message": "Classroom created successfully.",
                                 "classroom":serialized_classroom}, status=201)
        
def classroomPage(request,id):
    classroom = Classroom.objects.get(pk=id)
    announcements=Announcement.objects.filter(classroom=classroom).order_by('-date')
    quizzes=Quiz.objects.filter(classroom=classroom)
    quizSubmissions=QuizSubmission.objects.all()
    assignments=Assignment.objects.filter(classroom=classroom).order_by('dueDate')
    assignmentSubmission=AssignmentSubmission.objects.all()
    studentAssignments = []
    chats=[]



    if request.user.type == "Student":
        user = Student.objects.get(username=request.user.username)
        studentSubmissions = AssignmentSubmission.objects.filter(student=user)
        for sub in studentSubmissions:
            studentAssignments.append(sub.assignment)
    else:
        user = Teacher.objects.get(username=request.user.username)
        chats=Chat.objects.filter(teacher=user)
  
    currentTime = datetime.now()

       
    return render(request, "AcademicTaskManager/classroomPage.html",{
        "loggedinuser": user,
        "classroom": classroom,
        "announcements": announcements,
        "assignments": assignments,
        "assignmentSubmission": assignmentSubmission,
        "studentAssignments": studentAssignments,
        "quizzes": quizzes,
        "quizSubmissions": quizSubmissions,
        "chats": chats,
        "currentTime": currentTime,


    })

def chat(request,id):
    teacher = Teacher.objects.get(pk=id)
    student=Student.objects.get(username=request.user.username)

    try:
        chat=Chat.objects.get(teacher=teacher,student=student)
       
        return render(request, "AcademicTaskManager/chat.html",{
        "roomname": chat.roomname,
        "receiver": teacher.username,
        "chat": chat.message.all().order_by('date'),
        })
    except Chat.DoesNotExist:
        roomname=teacher.username+student.username
        chat=Chat.objects.create(roomname=roomname,teacher=teacher,student=student)
        chat.save()
        return render(request, "AcademicTaskManager/chat.html",{
        "roomname": roomname,
        "receiver": teacher.username,
        "chat": chat.message.all().order_by('date'),
       })
    
def teacherChat(request,id):
    student = Student.objects.get(pk=id)
    teacher=Teacher.objects.get(username=request.user.username)

    try:
        chat=Chat.objects.get(teacher=teacher,student=student)
       
        return render(request, "AcademicTaskManager/chat.html",{
        "roomname": chat.roomname,
        "receiver": student.username,
        "chat": chat.message.all().order_by('date'),
        })
    except Chat.DoesNotExist:
        roomname=teacher.username+student.username
        chat=Chat.objects.create(roomname=roomname,teacher=teacher,student=student)
        chat.save()
        chatMessages=chat.message.all().order_by('date')
        return render(request, "AcademicTaskManager/chat.html",{
            "roomname": chat.roomname,
            "receiver": student.username,
            "chat": chatMessages,
        })
  
def createAnnouncement(request):
    if request.method == "POST":
        data = json.loads(request.body)
        classroom = Classroom.objects.get(pk=data.get("classroomID", ""))
        title = data.get("title", "")
        content = data.get("content", "")
        announcement = Announcement.objects.create(classroom=classroom, title=title, content=content)
        announcement.save()
        serialized_announcement = announcement.serialize()
        return JsonResponse({"message": "Announcement created successfully.", "announcement": serialized_announcement}, status=201)
       
    
def createAssignment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        classroom = Classroom.objects.get(pk=data.get("classroomID", ""))
        title = data.get("title", "")
        marks = data.get("marks", "")
        dueDate = data.get("dueDate", "")
        assignment = Assignment.objects.create(classroom=classroom, title=title, marks=marks, dueDate=dueDate)
        assignment.save()
        return JsonResponse({"message": "Assignment created successfully."}, status=201)

def submitAssignment(request):
    if request.method == "POST":
        assignment_id = request.POST.get("assignmentID", "")
        assignment = Assignment.objects.get(pk=assignment_id)
        student = Student.objects.get(username=request.user.username)


        uploaded_file = request.FILES.get("file", None)
        if uploaded_file:
            assignment_submission = AssignmentSubmission.objects.create(
                assignment=assignment,
                student=student,
                file=uploaded_file,  
            )
            assignment_submission.save()

            print(assignment_submission.submissionTime)
            print(assignment.dueDate)
        

            if assignment_submission.submissionTime > assignment.dueDate:
                assignment_submission.late = True
                assignment_submission.save() 

          

            gradebook=GradeBook.objects.get(student=student,course=assignment.classroom.course)
            gradebook.assignments.add(assignment_submission)
            gradebook.save()
            return JsonResponse({"message": "Assignment submitted successfully."}, status=201)
        else:
            return JsonResponse({"message": "No file uploaded."}, status=400)
        

def assignmentSubmission(request,id):
    assignmentSubmission = AssignmentSubmission.objects.get(pk=id)
    return render(request, "AcademicTaskManager/assignmentSubmission.html",{
        "assignmentSubmission": assignmentSubmission,
    })

def gradeAssignment(request):
    if request.method == "POST":
        mark=request.POST["mark"]
        id=request.POST["id"]
        assignmentSubmission = AssignmentSubmission.objects.get(pk=id)
        assignmentSubmission.marks=mark
        assignmentSubmission.graded=True
        assignmentSubmission.save()
        return HttpResponseRedirect(reverse("assignmentSubmission", args=(id,)))
    

def createQuiz(request):
    if request.method == "POST":
        title=request.POST["quizTitle"]
        date=request.POST["quizDate"]
        classroom = Classroom.objects.get(pk=request.POST["classroomID"])
        course = Course.objects.get(pk=request.POST["classroomCourseID"])
        quiz = Quiz.objects.create(title=title,classroom=classroom,course=course,date=date)
        quiz.save()
        return render(request, "AcademicTaskManager/createQuiz.html",{
                  "quiz": quiz,})
    

def addQuestion(request):
    if request.method == "POST":
        data=json.loads(request.body)
        quiz = Quiz.objects.get(pk=data.get("quizID", ""))
        question = Question.objects.create(question=data.get("question", ""), A=data.get("A", ""), B=data.get("B", ""), C=data.get("C", ""), D=data.get("D", ""), correctAnswer=data.get("correctAnswer", ""), weight=data.get("weight", ""))
        quiz.questions.add(question)
        quiz.marks=int(quiz.marks)+int(question.weight)
        quiz.save()
        serialized_question = question.serialize()

        return JsonResponse({"message": "Question added successfully.", "question": serialized_question}, status=201)
    
def quiz(request,id,studentID):
    if request.method=="GET":
        quiz = Quiz.objects.get(pk=id)
        questions = quiz.questions.all()
        if request.user.type == "Student":
            try:
                quizSubmission = QuizSubmission.objects.get(quiz=quiz, student=request.user)
                StudentAnswers = StudentAnswer.objects.filter(quiz_submission=quizSubmission)
            
                return render(request, "AcademicTaskManager/quiz.html",{ "quiz": quiz, "questions": questions, "quizSubmission": quizSubmission,"StudentAnswers": StudentAnswers})
            except QuizSubmission.DoesNotExist:

                return render(request, "AcademicTaskManager/quiz.html",{
                    "quiz": quiz,
                    "questions": questions,
                })
        else:
            quizSubmission = QuizSubmission.objects.get(quiz=quiz, student=studentID)
            StudentAnswers = StudentAnswer.objects.filter(quiz_submission=quizSubmission)
            return render(request, "AcademicTaskManager/quiz.html",{
                    "quiz": quiz,
                    "questions": questions,
                    "quizSubmission": quizSubmission,
                    "StudentAnswers": StudentAnswers,

                })
        
def quizSubmission(request,id):
    if request.method == "POST":
        quiz = Quiz.objects.get(pk=id)
        student = Student.objects.get(username=request.user.username)
        quiz.answeredBy.add(student)
        quiz.save()

   
        quizSubmission = QuizSubmission.objects.create(student=student,quiz=quiz)
        quizSubmission.save()

        marks = 0
        questions = quiz.questions.all()
        for question in questions:
            studentAnswer = StudentAnswer.objects.create(student=student,question=question, quiz_submission=quizSubmission , selected_answer=request.POST["flexRadioDefault"+str(question.id)])
            studentAnswer.save()
            answer=request.POST["flexRadioDefault"+str(question.id)]
            if answer == question.correctAnswer:
                marks = marks + question.weight
                # quizSubmission.correctAnswers.add(question)
            
        quizSubmission.marks=marks
        quizSubmission.graded=True
        quizSubmission.save()
        gradebook=GradeBook.objects.get(student=request.user,course=quiz.course)
        gradebook.quizzes.add(quizSubmission)
        gradebook.save()

        return HttpResponseRedirect(reverse("quiz", args=(id,student.id,)))
    



def gradebook(request,studentID,courseID):
    if request.method=="GET":
        course=Course.objects.get(pk=courseID)
        student=Student.objects.get(pk=studentID)
        gradebook=GradeBook.objects.get(student=student,course=course)
        return render(request, "AcademicTaskManager/gradebook.html",{
            "gradebook": gradebook,
        })

    
def editFinal(request):
    if request.method == "POST":
        gradebookId=request.POST["gradebookID"]
        gradebook=GradeBook.objects.get(pk=gradebookId)
        gradebook.finalMark=request.POST["finalMark"]
        
        gradebook.save()
        return HttpResponseRedirect(reverse("gradebook", args=(gradebook.student.id,gradebook.course.id,)))
    

def editMidterm(request):
    if request.method == "POST":
        gradebookId=request.POST["gradebookID"]
        gradebook=GradeBook.objects.get(pk=gradebookId)
        gradebook.midtermMark=request.POST["midtermMark"]
        
        gradebook.save()
        return HttpResponseRedirect(reverse("gradebook", args=(gradebook.student.id,gradebook.course.id,)))
    

def finalGrade(request):
    if request.method == "POST":
        gradebookId=request.POST["gradebookID"]
        gradebook=GradeBook.objects.get(pk=gradebookId)
        gradebook.grade=request.POST["finalGrade"]
        gradebook.save()
        print(request.POST["finalGrade"])
        if gradebook.grade != "F":
            gradebook.passed=True
            gradebook.save()
        return HttpResponseRedirect(reverse("gradebook", args=(gradebook.student.id,gradebook.course.id,)))
    


        


      

       