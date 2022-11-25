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
from .forms import CourseForm, Assignform, Submissionform, gradesub


def userregister(request):
        """If the credentials are entered,and the given credentials are valid to register
                a new user will be saved in the database either as teacher or student depending
                on the role they choose while signingup.After saving, the page is redirected to the 
                loginpage bacause the decorater used above the teacherhome and studenthome function requires
                you to be logged in because the .

        """
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
                        if is_teacher==True:
                                return redirect('teacherhome')
                        # elif request.user.is_superuser==True:
                        #         return redirect('loginPage')
                        else:
                                return redirect('studenthome')
                else:
                        form = Signup()
        form = Signup()
        return render(request, 'trailer/userregister.html', {'name':name, 'form':form})


def login_view(request):
        """If the user is already authenticated, it will redirect to the respective home pages
                else if it is invalid then it stays the loginpage only.Using the username and password
                if it matches with the credentials which are already registered in the database or not 
                if the user is present,Then it logs them in and redirect to the homepages.
        
        """
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
                        elif user.is_teacher == False:
                                return redirect('studenthome')
                        else:
                                return redirect('wrong')
        
        return render(request, 'trailer/login.html', {'name':name})

def logoutuser(request):
        """I the user clicks on logout ,it redirects to the loginpage again
        """
        logout(request)
        return redirect('loginPage')

@login_required(login_url='loginpage')
def profileupdate(request,vary):
        """After getting the account via id=vary, we use a Signup form to obtain the details to which the profile is to be updated
                If the request.method is 'POST', then the instance/account obtained using "vary" as the id is updated according to the 
                responces filled in the form "Signup".If any field is empty in the form,then the old entry of that field is restored.

                :param vary: Account id
                :type vary: int 
        """
        account = Account.objects.get(id=vary)
        form = Signup(instance=account)
        if request.method=='POST':
                form = Signup(request.POST, instance=account)
                if form.is_valid():
                        form.save()
                        return redirect('loginPage')
        return render(request, 'trailer/profileupdate.html',{'form':form})


@login_required(login_url='loginPage')
def teacherhome(request):
        """If the user is teacher only then it can access the courses else it shows up the oops.html
                If the teacher is logged in,the courses registered by the teacher will be passed
                on as context along with the teacher's id.
        """
        if request.user.is_teacher==True:
                courses = Course.objects.all()
                return render(request, 'trailer/teacherhome.html',{'courses':courses,'vary':request.user.id})
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def courseform(request):
        """This is used to create courses if the user is a teacher.
                If request.method is 'POST' and the data entered in the courseform.html page is 
                stored in the "Courseform".If the form is valid then the course is created
        """
        if request.user.is_teacher==True:
                form = CourseForm()
                if request.method == 'POST':
                        form = CourseForm(request.POST)
                        if form.is_valid():
                                form.save()
                                return redirect('teacherhome')
                context ={'form':form}
                return render(request, 'trailer/courseform.html', context)
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def coursereg(request):
        """If the user is a teacher and the request.method is 'POST',using the data entered in the 
                coursereg.html which is stored in the coursecode, we register the student in a course that matches
                the coursecode and the redirect to the studenthome page
        """
        if request.user.is_teacher==False:
                if request.method == 'POST':
                        coursecode = request.POST.get('coursecode')
                        # username = request.POST.get('username')
                        username = request.user.username
                        course = Course.objects.get(joincode=coursecode)
                        user = Account.objects.get(username=username)
                        course.partipants.add(user)
                        return redirect('studenthome')

                return render(request, 'trailer/coursereg.html',{})
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def coursedelete(request,pk):
        """If the user is a teacher and it is logged in, if the request is to delete the a respective "pk" course
                in the delete.html,we use the delete function to remove it via a variable.Then it redirects to the teacherhome.

                :param pk: Course name
                :type pk: str
        """
        if request.user.is_teacher==True:
                course = Course.objects.get(name=pk)
                if request.method == 'POST':
                        course.delete()
                        return redirect('teacherhome')
                return render(request, 'trailer/delete.html', {'obj':course})
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def coursepage(request,pk):
        """If the user is a teacher and it is logged in, get the course with course name as "pk"
                All the assignments which are in the respective course will get filtered and will be 
                passed on in the context to the html page

                :param pk: Course name
                :type pk: str
        """
        if request.user.is_teacher==True:
                course = Course.objects.get(name=pk)
                assign = Assignment.objects.filter(course=course)
                return render(request, 'trailer/coursepage.html',{'course':course,'assign':assign})
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def teachassign(request,pk):
        """If the user is a teacher and it is logged in, get the assignments with assignment name as "pk"
                as a query set using "filter".Since we need an object we use .last() to obtain the
                assignment from the query set
                All the submissions which are in the respective assignment will get filtered and will be 
                passed on in the context to the html page along with the assignment

                :param pk: Assignment name
                :type pk: str
        """
        if request.user.is_teacher==True:
                assign = Assignment.objects.filter(name=pk).last()
                submiss = Submission.objects.filter(assignment = assign)
                return render(request, 'trailer/teachassign.html', {'assign':assign,'submiss':submiss})
        else:
                return render(request, 'trailer/oops.html')

# -------------------------------------------------
@login_required(login_url='loginPage')
def createassign(request,pk):
        """In the course(found via pk) to create an assignment,we take the data which we retrieved from the 
                createassign.html page and store them in respective variables.Then we create new instance 
                assignment with the newly created variables and save the instance using "save()"

                :param pk: Course name
                :type pk: str
        """
        if request.user.is_teacher==True:       
                course = Course.objects.get(name=pk)
                if request.method=='POST':
                        uploaded_file=request.FILES['assignfile']
                        filenam = request.POST.get('file_name')
                        assign_name = request.POST.get('assignname')
                        cour = course
                        temp = Assignment(name=assign_name,file_name=filenam,assignfile=uploaded_file,course=cour)
                        temp.save()
                        return redirect('coursepage',pk=course.name)
                return render(request,'trailer/createassign.html')
        else:
                return render(request, 'trailer/oops.html')

#---------------------------------------------------
@login_required(login_url='loginPage')
def assigndelete(request,pk):
        """We get assignment name which is to be deleted and the course of that assignment
                Then it is deleted with the "delete()" and redirect to the coursepage

                :param pk: Assignment name
                :type pk: str
        """
        if request.user.is_teacher==True:
                assign = Assignment.objects.filter(name=pk).last()
                course = assign.course
                if request.method == 'POST':
                        assign.delete()
                        return redirect('coursepage',pk=course.name)
                return render(request, 'trailer/assigndelete.html',{'obj':assign}) 
        else:
                return render(request, 'trailer/oops.html') 

@login_required(login_url='loginPage')
def subteach(request,id):
        """We get the respective submission by following the id and the user who is currently working
                and pass them as contexts in the subteach.html

                :param id: Submission id
                :type id: int
        """
        if request.user.is_teacher==True:
                user = request.user
                submiss = Submission.objects.get(id=id)
                return render(request, 'trailer/subteach.html', {'user':user,'submiss':submiss})
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def editsub(request,oi):
        """The submission which is obtained via id need to be edited
                The grades and feedback which are obtained from editsub.html
                will be edited in the submission if the request.method is 'POST'

                :param oi: Submission id
                :type oi: int                
        """
        if request.user.is_teacher==True:
                sub = Submission.objects.get(id=oi)
                if request.method=='POST':
                        sub.grade = request.POST['grades']
                        sub.feedback = request.POST['feedback']
                        sub.save()
                        return redirect('subteach',id=sub.id)
                return render(request, 'trailer/editsub.html')
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def studenthome(request):
        """If the user is a student and it is logged in,the courses registered under the student's name will be passed
                on as context along with the student's id.
        """
        if request.user.is_teacher==False:
                name= "studenthome"
                courses = Course.objects.all()
                return render(request, 'trailer/studenthome.html',{'courses':courses,'vary':request.user.id})
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def studentcourse(request,pk):
        """If the user is a student and it is logged in, get the course with course name as "pk"
                All the assignments which are in the respective course will get filtered and will be 
                passed on in the context to the html page

                :param pk: Course name
                :type pk: str
        """
        if request.user.is_teacher==False:
                course = Course.objects.get(name=pk)
                assign = Assignment.objects.filter(course=course)
                return render(request, 'trailer/studentcourse.html', {'course':course, 'assign':assign})
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def studentassign(request,pk):
        """If the user is a student and it is logged in,we get the assignments with assignment name as "pk"
                as a query set using "filter".Since we need an object we use .last() to obtain the
                assignment from the query set.
                All the submissions which are in the respective assignment and which are under the student's(current user) name 
                get filtered as a query_set.Using the "last()" function we get the submission object.
                Both of the objects will be passed on in the context to the html page.

                :param pk: Assignment name
                :type pk: str
        """
        if request.user.is_teacher==False:
                assign = Assignment.objects.filter(name=pk).last()
                submiss = Submission.objects.filter(assignment=assign, student=request.user).last()

                return render(request, 'trailer/studentassign.html', {'assign':assign,'submiss':submiss})
        else:
                return render(request, 'trailer/oops.html')

@login_required(login_url='loginPage')
def createsub(request,nm):
        """If the user is a student, It gets the assignment via name and the remaining variables 
                then store the class with the parameters in the temp variable and redirect to the studentassign page

                :param pk: Assignment name
                :type pk: str
        """
        if request.user.is_teacher==False:
                if request.method=='POST':
                        assign = Assignment.objects.get(name=nm)
                        # course = assign.course
                        student = request.user
                        uploaded_file=request.FILES['subfile']
                        grade=-1
                        feedback='Feedback yet to be updated'
                        temp = Submission(student=student,subfile=uploaded_file,assignment=assign,grade=grade,feedback=feedback)
                        temp.save()
                        return redirect('studentassign',pk=assign.name)
                return render(request, 'trailer/createsub.html')
        else:
                return render(request, 'trailer/oops.html')


def wrong(request):
        """If the student tries to access the teacher's pages,Then this page will be displayed.
        """
        return render(request, 'trailer/oops.html')      
