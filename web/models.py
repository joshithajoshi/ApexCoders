from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey

class Student(models.Model):
        username = models.IntegerField(null = True)
        name = models.CharField(max_length=200, null=True)
        password = models.CharField(max_length=8, null=False)
        date_enrolled = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.name
class Teacher(models.Model):
        username = models.IntegerField(null = True)
        name = models.CharField(max_length=200, null=True)
        password = models.CharField(max_length=8, null=False)

        def __str__(self):
                return self.name

class Course(models.Model):
        name = models.CharField(max_length=200, null=True)
        professor = models.ForeignKey(Teacher, on_delete = models.SET_NULL, null=True)
        students = models.ManyToManyField(Student)
        description = models.TextField(blank=True)
        coursecode=models.CharField(max_length=10,default = '')
        updated = models.DateTimeField(auto_now=True)
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
                ordering = ['-updated', '-created']

        def __str__(self):
                return self.name

class question(models.Model):
        name = models.CharField(max_length=200, null=True)
        updated = models.DateTimeField(auto_now=True)
        #ikkada submission link and question description pettali

class assignment(models.Model):
        name = models.CharField(max_length=200, null=False)
        # ikkada assignment deni meda base ayyindo rayali
        questions = models.ManyToManyField(question, blank = False)
        maxmarks = models.IntegerField(default=100)
        weightage = models.IntegerField(default=0)
        course = models.ForeignKey(Course, on_delete = models.CASCADE)
        deadline = models.DateTimeField(blank = False)
        updated = models.DateTimeField(auto_now=True)
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.name
