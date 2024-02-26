#  Academic Task Manager 

## Distinctiveness and Complexity 

The Academic Task Manager is a web-based platform designed to facilitate seamless communication between students, professors, and administrators in an academic setting. This project stands out for its multifaceted approach to academic management and its robust set of features.This project distinguishes itself through its user roles, comprehensive features, and user-friendly interface. Unlike other projects, the Academic Task Manager provides a holistic solution for academic institutions, bringing students, teachers, and admins together in one platform. Its complexity arises from the need to manage diverse academic tasks, including course registeration, assignments, announcements, quizzes, and grade tracking, all while maintaining user friendly interface that is mobile responsive.

Administrators play a pivotal role in the project's success, with distinct responsibilities that are vital for effective academic management. Admins have the responsibility to input course data, including titles and codes, ensuring that accurate course information is readily available. Additionally, they can assign courses to their respective teachers, a crucial step in maintaining organizational efficiency.

One of the key elements that make the Academic Task Manager project truly distinct lies in the multifaceted roles of teachers within the system. Teachers have the authority to create classrooms for courses, a feature crucial for student registration and course management. Moreover, they can effortlessly post announcements for each classroom, ensuring that students are always well-informed about important updates. What truly sets this project apart is the ability for teachers to design and deploy auto-graded MCQ quizzes, complete with scheduled start times. This not only simplifies the assessment process but also offers a level of sophistication that goes beyond standard academic management tools. Teachers can also create assignments, grade submissions, and even update students' gradebooks, automatically marking courses as 'passed' when appropriate grades are assigned. Additionally, the project allows teachers to view all student submissions under the posts they create, streamlining the grading process.

For students, the Academic Task Manager offers a distinctive set of features aimed at enhancing their academic journey. The project ensures that students can register or drop courses based on the availability of courses within their major, a feature that streamlines the registration process and minimizes confusion. Students can efficiently manage their academic profile, allowing them to track registered and completed courses, monitor credit hours, and review personal information. Students can also easily track their grades through the classrooms or gradebook pages. The ability to send private messages to instructors ensures efficient communication for academic inquiries. Moreover, the homepage provides a one-stop hub for students to stay updated with announcements, assignments, and quizzes across all registered courses. This comprehensive suite of features serves as a testament to the project's commitment to enhancing the student experience and sets it apart from conventional academic management tools.

## Files Inside the Project

# models.py

This file contains the definition of the project's data models using Django's Object-Relational Mapping (ORM) system.

User: Extends Django's built-in AbstractUser model to add a custom type field to distinguish between "Student" and "Teacher" users.

Major: Represents academic majors and includes a name and totalCreditHours field.

Course: Represents academic courses with fields for name, code, major, and creditHours.

Student: Extends the User model for students, adding fields for year, major, and a many-to-many relationship with registered courses.

Teacher: Extends the User model for teachers, adding a many-to-many relationship with courses they teach.

Classroom: Represents a class or course section, with fields for course, teacher, students, semester, year, and capacity.

Assignment: Represents assignments with fields for title, classroom, marks, and dueDate.

AssignmentSubmission: Represents student submissions for assignments, including student, assignment, file, marks, 
graded, submissionTime, and late fields.

Question: Represents quiz questions with fields for question, options A, B, C, D, correctAnswer, and weight.

Quiz: Represents quizzes with fields for title, questions, course, classroom, marks, date, and answeredBy.

QuizSubmission: Represents student submissions for quizzes with fields for student, quiz, marks, and graded.

StudentAnswer: Represents individual student answers to quiz questions with fields for student, question, 
quiz_submission, and selected_answer.

GradeBook: Represents student grades for courses, including student, course, midtermMark, finalMark, quizzes, 
assignments, grade, and passed.

Announcement: Represents announcements for classrooms with fields for title, content, classroom, and date.

Message: Represents chat messages with fields for sender, receiver, content, and date.

Chat: Represents chat rooms with fields for roomname, message, teacher, and student.


# views.py

This file contains all the views that renders html pages and all of the APIs.

index(request): This view handles the main page of the application. It checks if the user is authenticated and if they are a "Student." If so, it fetches announcements, assignments, and quizzes related to the classrooms that the student is enrolled in and paginates the results. Finally, it renders the main page with the fetched data.

login_view(request): Handles user login. It authenticates the user and logs them in if the provided credentials are valid.

logout_view(request): Logs the user out and redirects them to the main page.

register(request): Handles user registration. It creates either a "Student" or "Teacher" user based on the provided information.

profile(request): Displays the user's profile. If the user is a student, it shows their gradebooks and passed credit hours. If the user is a teacher, it displays their profile.

registerPage(request): Displays a page for user registration, allowing students to choose courses.

addCourse(request): Allows students to add courses to their registered courses.

removeCourse(request): Allows students to remove courses from their registered courses.

classroom(request): Displays the classroom page for either students or teachers, showing their respective classrooms and courses.

createClassroom(request): Creates a new classroom for a teacher and associates it with a course.

classroomPage(request, id): Displays the classroom page with announcements, assignments, quizzes, and chats.

chat(request, id): Allows students to chat with their teachers.

teacherChat(request, id): Allows teachers to chat with students.

createAnnouncement(request): Allows teachers to create announcements for their classrooms.

createAssignment(request): Allows teachers to create assignments for their classrooms.

submitAssignment(request): Allows students to submit assignments, including checking for late submissions.

assignmentSubmission(request, id): Displays the details of a submitted assignment.

gradeAssignment(request): Allows teachers to grade assignments submitted by students.

createQuiz(request): Allows teachers to create quizzes for their classrooms.

addQuestion(request): Allows teachers to add questions to a quiz.

quiz(request, id, studentID): Displays quizzes for students and teachers and allows students to submit quiz answers.

quizSubmission(request, id): Handles quiz submissions.

gradebook(request, studentID, courseID): Displays a student's gradebook for a specific course, including midterm and final grades.

editFinal(request): Allows teachers to edit final grades in the gradebook.

editMidterm(request): Allows teachers to edit midterm grades in the gradebook.

finalGrade(request): Allows teachers to assign final grades to students in the gradebook.

# url.py

This file contains URL patterns that define the routing structure, mapping specific URLs to their corresponding view functions for handling user requests and rendering appropriate content.

Index Page: When the root URL (/) is accessed, it maps to the views.index function.

Login Page: The /login URL is associated with the views.login_view function.

Logout Page: The /logout URL is linked to the views.logout_view function.

Registration Page: When users visit /register, it routes to the views.register function.

Profile Page: Accessing /profile directs users to the views.profile function.

Registration Page: The /registrationPage URL is handled by the views.registerPage function.

Add Course Page: Accessing /addCourse will invoke the views.addCourse function.

Remove Course Page: Visiting /removeCourse routes to the views.removeCourse function.

Classroom Page: The /classroom URL is associated with the views.classroom function.

Create Classroom Page: Accessing /createClassroom triggers the views.createClassroom function.

Classroom Page: URLs like /classroomPage<int:id> are handled by the views.classroomPage function, where <int:id> is a 
variable for the classroom ID.

Create Announcement Page: The /createAnnouncement URL is linked to the views.createAnnouncement function.

Create Assignment Page: Accessing /createAssignment will invoke the views.createAssignment function.

Submit Assignment Page: URLs like /submitAssignment<int:id> are handled by the views.assignmentSubmission function, where <int:id> is a variable for the assignment submission ID.

Grade Assignment Page: The /gradeAssignment URL is associated with the views.gradeAssignment function.

Create Quiz Page: Accessing /createQuiz triggers the views.createQuiz function.

Add Question Page: The /addQuestion URL is linked to the views.addQuestion function.

Quiz Page: URLs like /quiz/<int:id>/<int:studentID> are handled by the views.quiz function, where <int:id> is a variable for the quiz ID, and <int:studentID> is a variable for the student ID.

Quiz Submission Page: URLs like /quizSubmission<int:id> are handled by the views.quizSubmission function, where <int:id> is a variable for the quiz ID.

Chat Page : URLs like /chat/<int:id> are associated with the views.chat function, where <int:id> is a variable for the teacher ID.

Teacher Chat Page (with User ID): URLs like /teacherChat/<int:id> are handled by the views.teacherChat function, where <int:id> is a variable for the student ID.

Gradebook Page: URLs like /gradebook/<int:studentID>/<int:courseID> are linked to the views.gradebook function, where <int:studentID> is a variable for the student ID, and <int:courseID> is a variable for the course ID.

Edit Final Grade Page: The /editFinal URL is associated with the views.editFinal function.

Edit Midterm Grade Page: Accessing /editMidterm will invoke the views.editMidterm function.

Final Grade Page: The /finalGrade URL is linked to the views.finalGrade function.

# consumers.py

The file contains the implementation of a WebSocket consumer class called ChatConsumer.

Connect and Disconnect Methods:
The connect method is called when a WebSocket connection is established. It extracts the room_name from the URL route's kwargs and sets up a group for the chat room. It also accepts the WebSocket connection.The disconnect method is called when a WebSocket connection is closed. It removes the consumer from the group associated with the chat room.

Receive Method:
The receive method is called when the server receives a WebSocket message from the client. It processes the incoming message, extracts information such as the message content, sender, receiver, and room name, and then calls the save_message method to save the message to the database. After saving the message, it broadcasts it to all clients in the chat room.

Chat Message Method:
The chat_message method is responsible for sending chat messages to clients in the chat room. It sends a JSON object containing the message content, sender, receiver, and room name to the connected clients.

Save Message Method:
The save_message method is a synchronous method that saves the chat message to the database. It takes the message content, sender, receiver, and room name as parameters.
Inside this method, it retrieves the corresponding User and Chat objects based on the provided usernames and room name. Then, it creates a new Message object with the message content, associates it with the sender and receiver, and adds it to the chat room's messages.

# routing.py

This file contains the WebSocket URL routing.

path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()): This URL pattern maps WebSocket connections to the ChatConsumer class, which is implemented as an ASGI (Asynchronous Server Gateway Interface) consumer. The <str:room_name> part of the URL is a parameter that allows dynamic WebSocket connections based on the specified room name.

# admin.py

This file contains the registration of all the models that have been defined.

# templates folder

this folder contains all the html files that are rendered by the views.

# static folder

this folder contains all the static files such as css, js, and images.

## how to run project

Install the required dependencies using pip install -r requirements.txt.

Create a superuser with python manage.py createsuperuser to access the admin user interface.

Start the development server with python manage.py runserver.

## additional information 

I had to use an older version of Django to work with channels, I have added the exact vesions used in the requirements 
file.

I have created two extra files that were not inside the original Django project when it was created. They handle the functionality of chatting. Consumer.py handles the connection of people to chat rooms and broadcasting of the messages and routing.py handles the paths of WebSocket. I could not implement the Redis Channel Layer, so I used the In-Memory Channel Layer.
