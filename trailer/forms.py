from django import forms
from django.contrib.auth.models import User
from trailer.models import Account, Course, Assignment, Submission
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class Signup(UserCreationForm):
        
        username = forms.CharField(max_length=20)

        class Meta:
                model = Account
                fields = (
                        'username',
                        'password1',
                        'password2',
                        'is_teacher',
                )

class CourseForm(ModelForm):
        class Meta:
                model = Course
                fields = '__all__'

class Assignform(ModelForm):
        class Meta:
                model = Assignment
                fields = '__all__'

class Submissionform(ModelForm):
        class Meta:
                model = Submission
                fields = (
                        'file_name',
                        'subfile',
                )

class gradesub(ModelForm):
        class Meta:
                model = Submission
                fields = '__all__'

