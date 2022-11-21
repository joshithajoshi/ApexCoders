from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('student_login/', views.studentlogin, name="studentlogin"),
    path('student_logout/', views.studentlogout, name="studentlogout"),
    path('teacher_login/', views.teacherlogin, name="teacherlogin"),
    path('student_home/', views.studenthome, name = "studenthome"),
#     path('teacher_login/', views.teacherhome, name = "teacherhome")
#     path('teacher_course/<str:pk>/', views.Course, name = "teachercourse"),
    path('student_course/<str:pk>/', views.studentcourse, name = "studentcourse"),
#     path('create-course/', views.createCourse, name = "create-course"),
#     path('edit-course/', views.editCourse, name= "edit-course"),
#     path('delete-course/', views.deleteCourse, name= "delete-course"),
]
