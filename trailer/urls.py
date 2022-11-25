from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login_view, name= "loginPage"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('teacherhome/', views.teacherhome, name= "teacherhome"),
    path('profileupdate/<int:vary>/', views.profileupdate, name="profileupdate"),
    path('userregister/', views.userregister, name= "userregister"),
    path('courseform/', views.courseform, name = "courseform"),
    path('course/<str:pk>/', views.coursepage, name="coursepage"),
    path('coursedelete/<str:pk>', views.coursedelete, name = "coursedelete"),
    path('assignment/<str:pk>/', views.teachassign, name="teachassign"),
    path('assigndelete/<str:pk>/', views.assigndelete, name="assigndelete"),
    path('subteach/<int:id>/', views.subteach, name="subteach"),
    path('editsub/<int:oi>/', views.editsub, name="editsub"),
    path('studenthome/', views.studenthome, name= "studenthome"),
    path('coursereg/', views.coursereg, name ="coursereg"),
    path('studentcourse/<str:pk>/', views.studentcourse, name= "studentcourse"),
    path('studentassign/<str:pk>', views.studentassign, name="studentassign"),
    path('oops/', views.wrong, name="wrong"),
    path('createassign/<str:pk>/', views.createassign, name="createassign"),
    path('createsub/<str:nm>', views.createsub, name="createsub"),
    #path('subdelete/<str:pk>', views.subdelete, name="subdelete"),
    #path('studentlogout/', views.studentlogout, name ="studentlogout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)