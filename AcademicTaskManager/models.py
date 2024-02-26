from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    typeChoices = (
        ("Student", "Student"),
        ("Teacher", "Teacher"),
    )
    type = models.CharField(choices=typeChoices, max_length=10, default="Student")

    def __str__(self):
        return f"{self.username} {self.type}"

class Major(models.Model):
    name = models.CharField(max_length=64)
    totalCreditHours = models.IntegerField(default=120)
    def __str__(self):
        return f"{self.name}"
    
class Course(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=10)
    major = models.ManyToManyField(Major, related_name="courseMajor")
    creditHours = models.IntegerField(default=3)
 
    def __str__(self):
        return f"{self.name} {self.code}"
    
class Student(User):
    yearChoices = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    year = models.CharField(choices=yearChoices, max_length=1, default="1")
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="studentMajor")
    registeredCourses = models.ManyToManyField(Course, blank=True, related_name="studentCourses")
    

    def __str__(self):
        return f"{self.username}"
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
class Teacher(User):
    courses = models.ManyToManyField(Course, blank=True, related_name="teacherCourses")
    def __str__(self):
        return f"{self.username}"
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
    
class Classroom(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="classroomCourse")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="classroomTeacher")
    students = models.ManyToManyField(Student, blank=True, related_name="classroomStudents")
    semesterChoices = (
        ("Fall", "Fall"),
        ("Spring", "Spring"),
        ("Summer", "Summer"),
    )
    semester = models.CharField(choices=semesterChoices, max_length=10, default="Fall")
    year = models.IntegerField(default=datetime.datetime.now().year)
    capacity = models.IntegerField(default=30)

    def serialize(self):
        return {
            "id": self.id,
            "courseCode":self.course.code,
            "courseName": self.course.name,
            "semester": self.semester,
            "year": self.year,
           
        }



    def __str__(self):
        return f"{self.course} teached by {self.teacher}"
    
class Assignment(models.Model):
    title = models.CharField(max_length=64)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="assignmentsClassroom")
    marks = models.IntegerField(default=10)
    dueDate = models.DateTimeField()
    def __str__(self):
        return f"{self.title} {self.classroom}"
  
class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="studentSubmissions")
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="assignmentSubmissions")
    file = models.FileField(upload_to='uploads/')
    marks = models.TextField(default="Not Graded")
    graded = models.BooleanField(default=False)
    submissionTime = models.DateTimeField(default=timezone.now)
    late = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.student} {self.assignment} "  

class Question(models.Model):
    question= models.TextField()
    A = models.TextField()
    B = models.TextField()
    C = models.TextField() 
    D = models.TextField()
    correctAnswer = models.TextField()
    weight = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.question}"
    
    def serialize(self):
        return {
            "id": self.id,
            "question": self.question,
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "D": self.D,
            "correctAnswer": self.correctAnswer,
            "weight": self.weight
        }
    
class Quiz(models.Model):
    title= models.CharField(max_length=64)
    questions = models.ManyToManyField(Question, related_name="quizQuestions")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="quizzesCourse")
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="quizzesClassroom")
    marks = models.IntegerField(default=0)
    date= models.DateTimeField(default=datetime.datetime.now())
    answeredBy = models.ManyToManyField(Student, blank=True, related_name="answeredby")
    def __str__(self):
        return f"{self.title} {self.course}"
    
class QuizSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="studentQuizSubmissions")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quizSubmissions")
    marks = models.TextField(default="Not Graded")
    graded = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.student} {self.quiz}"
    
class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="student_answers")
    quiz_submission = models.ForeignKey(QuizSubmission, on_delete=models.CASCADE, related_name="student_answers")
    selected_answer = models.TextField()  

    def __str__(self):
        return f"{self.student} - {self.question}"
    
class GradeBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="studentGradeBook")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courseGradeBook")
    midtermMark = models.IntegerField(default=0)
    finalMark = models.IntegerField(default=0)
    quizzes=models.ManyToManyField(QuizSubmission, related_name="quizSubmissions")
    assignments=models.ManyToManyField(AssignmentSubmission, related_name="assignmentSubmissions")
    grade_choices = (
    ("In Progress", "In Progress"),
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("F", "F"),
    )   

    grade = models.CharField(max_length=12, choices=grade_choices, default="In Progress")

    passed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.student} {self.course}"
       
class Announcement(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="announcementsClassroom")
    date= models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return f"{self.title} {self.classroom}"
    
    def serialize(self):
        return {
        "title": self.title,
        "content": self.content,
        "date": self.date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date as a string
    }
   

    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    content = models.TextField()
    date= models.DateTimeField(default=datetime.datetime.now())

class Chat(models.Model):
    roomname= models.CharField(max_length=64)
    message = models.ManyToManyField(Message, blank=True, related_name="chatMessages")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")

    def __str__(self):
        return f"{self.teacher} chatting with {self.student}"
    

    


    



