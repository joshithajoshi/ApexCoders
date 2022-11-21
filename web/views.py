from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student,Teacher,Course
# Create your views here.

def home(request):
    return render(request, 'web/home.html')

def studentlogin(request):
        page='studentlogin'
        if request.student.is_authenticated:
                return redirect('home')
        if request.method=='POST':
                username=request.POST.get('username').lower()
                password=request.POST.get('password')

                try:
                        student = Student.objects.get(username=username)
                except:
                        messages.error(request, 'User does not exists')
                student = authenticate(request, username=username, password=password)

                if student is not None:
                        login(request, student)
                        return redirect('studenthome')
                else:
                        messages.error(request, 'Username or password does not exists')
        context={'page': page}
        return render(request, 'web/student_login.html')

def studentlogout(request):
        logout(request)
        return redirect('studentlogin')

def studenthome(request):
        q=request.GET.get('q') if request.GET.get('q') !=None else ''
        return render(request, 'web/student_home.html', {})

def studentcourse(request,pk):
        course=Course.objects.get(id=pk)
        return render(request, 'web/student_course.html',{'course':course})

# def studentregisterPage(request):
#         def registerPage(request):
#         form = UserCreationForm()
#         if request.method =='POST':
#                 form = UserCreationForm(request.POST)
#                 if form.is_valid():
#                         user = form.save(commit=False)
#                         user.username = user.username.lower()
#                         user.save()
#                         login(request, user)
#                         return redirect('home')
#                 else:
#                         messages.error(request, 'An error occured during registration')
#         return render(request, 'myapp/login_register.html' ,{'form': form})

def teacherlogin(request):
        return render(request, 'web/teacher_login.html')
        
