from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import Signup
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from trailer.models import Account, Course, Assignment, Submission
import requests
from requests.exceptions import HTTPError
from .forms import CourseForm, Assignform


def userregister(request):
        name= "userregister"
        if request.method =='POST':
                form = Signup(request.POST)
                if form.is_valid():
                        username= form.cleaned_data.get('username')
                        password = form.cleaned_data.get('password1')
                        is_teacher = form.cleaned_data.get('is_teacher')
                        user = authenticate(username=username, password=password, is_teacher = is_teacher)
                        # profile = Profile(account = user, name=username)
                        # profile.save()
                        form.save()
                        #login(request, user)
                        print(is_teacher)
                        # if is_teacher == True:
                        #         return render(request, 'trailer/teacherhome.html', {'name':name, 'form':form})
                        # else:
                        #         return render(request, 'trailer/studenthome.html', {'name':name, 'form':form})
                        return render(request, 'trailer/login.html',{'form':form})
                else:
                
                        form = Signup()
        form = Signup()
        return render(request, 'trailer/userregister.html', {'name':name, 'form':form})

def login_view(request):
        name = 'loginPage'

        if request.user.is_authenticated:
                if request.user.is_teacher == True:
                        return redirect('teacherhome')
                elif request.user.is_teacher == False:
                        return redirect('studenthome')
                else:
                        return redirect('loginPage')
        if request.method=='POST':

                username=request.POST.get('username')
                password=request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        print(user.is_teacher)
                        if user.is_teacher==True:
                                return redirect('teacherhome')
                        else:
                                return redirect('studenthome')
                else:
                        messages.error(request, 'Username or password does not exists')
        
        return render(request, 'trailer/login.html', {'name':name})
@login_required(login_url='loginPage')
def studenthome(request):
        name= "studenthome"
        courses = Course.objects.all()
        return render(request, 'trailer/studenthome.html',{'courses':courses})

@login_required(login_url='loginPage')
def teacherhome(request):
        courses = Course.objects.all()
        name = "teacherhome"
        return render(request, 'trailer/teacherhome.html',{'courses':courses})

def courseform(request):
        form = CourseForm()
        if request.method == 'POST':
                form = CourseForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('teacherhome')
        context ={'form':form}
        return render(request, 'trailer/courseform.html', context)

def assignform(request):
        form=Assignform()
        if request.method == 'POST':
                form=Assignform(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('coursepage')
        return render(request,'trailer/assignform.html',{'form':form})

def coursepage(request,pk):
        course = Course.objects.get(name=pk)
        assign = Assignment.objects.filter(course=course)
        return render(request, 'trailer/coursepage.html',{'course':course,'assign':assign})

def teachassign(request,pk):
        assign = Assignment.objects.filter(name=pk).last()
        submiss = Submission.objects.filter(assignment = assign)
        return render(request, 'trailer/teachassign.html', {'assign':assign,'submiss':submiss})

def subteach(request,id):
        user = request.user
        submiss = Submission.objects.get(id=id)
        return render(request, 'trailer/subteach.html', {'user':user,'submiss':submiss})

def studentcourse(request,pk):
        course = Course.objects.get(name=pk)
        return render(request, 'trailer/studentcourse.html', {'course':course})

def coursedelete(request,pk):
        course = Course.objects.get(name=pk)
        if request.method == 'POST':
                course.delete()
                return redirect('teacherhome')
        return render(request, 'trailer/delete.html', {'obj':course})

def coursereg(request):
        if request.method == 'POST':
                coursecode = request.POST.get('coursecode')
                # username = request.POST.get('username')
                username = request.user.username
                course = Course.objects.get(joincode=coursecode)
                user = Account.objects.get(username=username)
                course.partipants.add(user)
                return redirect('studenthome')

        return render(request, 'trailer/coursereg.html',{})


