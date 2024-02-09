from django.urls import path

from students.views import student, student_add, student_table, set_table, uprec
from teacher.views import teacher, add_teacher, teacher_table, set_teacherTable, teacher_up
from .views import index, register, login, home, home_admin

urlpatterns = [
    path("", index, name="index"),
    path('register/', register, name="registration"),
    path("login/", login, name="login"),
    path("home/", home, name="home"),
    path("home_admin", home_admin, name="home_admin"),
    path("student/", student, name="students"),
    path("student_add", student_add, name="student_add"),
    path("student_table", student_table, name="student_table"),
    path('set_table/<int:id>', set_table),
    path('update/uprec/<int:id>/', uprec, name='uprec'),
    path('teacher/', teacher, name='teacher_home'),
    path('add_teacher', add_teacher, name='add_teacher'),
    path('teacher_table/', teacher_table, name="teacher_table"),
    path('teacher_table/set_teacherTable/<int:id>', set_teacherTable),
    path('update/teacher_up/<int:id>/', teacher_up, name='teacher_up')
]