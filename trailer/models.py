from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE

class MyAccountManager(BaseUserManager):
        '''
        | :func:`create_user`
        | :func:`create_superuser`
        '''

        def create_user(self, username, password, is_teacher,is_superuser):
                """
                creates an account as specified(teacher or student)


                :param self: self
                :type self: self
                :param password: password field
                :type password: string
                :param username: name of the user
                :type username: string
                :param is_teacher: true if user is teacher
                :type is_teacher: bool

                """
                if not username:
                        raise ValueError("Please enter username")
                user = self.model(username = username, password=password,is_teacher=is_teacher,is_superuser=is_superuser)
                user.set_password(password)
                user.save(using=self._db)
                return user
        
        def create_superuser(self, username, password, is_teacher):
                """
                creates a superuser(admin)

                :param self: self
                :type self: self
                :param username: name of the user
                :type username: string
                :param password: password field
                :type password: string
                :param is_teacher: true if user is teacher
                :type is_teacher: bool
                
                """
                user = self.create_user(username=username, password=password,is_teacher=is_teacher,is_superuser = True)
                user.set_password(password)
                user.is_teacher = False
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
                user.save()
                return user

class Account(AbstractBaseUser, PermissionsMixin):

        '''
        Custom user model 

        :param AbstractBaseUser: default
        :param PermissionsMixin: default
        :fieldname: username
        :fieldname: is_teacher
        :username: name of the user
        :is_teacher: true if user is teacher and else false
        :is_admin: true if user is admin and else false
        :is_active: true if user is active and else false
        :is_staff: true if user is staff and else false
        :is_superuser: true if user is admin and else false
        :date_joined: date and time of joining of the user
        :last_login: date and time of last login of the user
        '''
        username = models.CharField(default='', max_length=60, unique=True)
        date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
        last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
        is_teacher = models.BooleanField(default =False)
        is_admin = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)

        USERNAME_FIELD = 'username'
        REQUIRED_FIELDS = ['is_teacher']

        objects = MyAccountManager()

        def _str_(self):
                return self.username





class Course(models.Model):
        '''
        course model 
        defines host,participants,joincode,name of the course for a particular course

        :name: name of the course
        :host: host model
        :partipants: students enrolled to a particular course model
        :joincode: code required to register for a course

        '''
        name = models.CharField(max_length=10)
        host = models.ForeignKey(Account, null=True,  on_delete=models.CASCADE, related_name = "host")
        partipants = models.ManyToManyField(Account, related_name = "participants")
        joincode = models.CharField(max_length=10,default = '')
        

        def _str_(self):
                return self.name

class Assignment(models.Model):
        '''
        Assignment model
        defines name of the assignment,name of the problem statement,problem statement file,course model

        :name: name of the assignment
        :file_name: problem statement file name
        :assignfile: submitted problem statement file by the teacher
        :course: course model

        '''
        name = models.CharField(max_length=128, default='')
        file_name = models.CharField(max_length=100, default= 'assignment_file')
        assignfile = models.FileField(upload_to ='assignments', blank = True)
        course = models.ForeignKey(Course, on_delete=models.CASCADE)

        def _str_(self):
                return self.name

class Submission(models.Model):
        '''
        Submission model
        defines student model,submitted file by a particular student,name of the file recieved from the student,assignment model,feedback recieved to a student from techer,grade recieved to a student
        
        :student: student model
        :subfile: submitted file
        :file_name: name of the submitting file
        :assignment: assignment model
        :feedback: comments from teacher 
        :grade: grade from teacher 
        '''
        student = models.ForeignKey(Account,on_delete=models.CASCADE)
        subfile = models.FileField(upload_to='submissions',blank=True)
        file_name = models.CharField(max_length=100,default='submission')
        assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
        feedback = models.CharField(max_length=300, default='Feedback yet to be updated')
        grade = models.IntegerField(default=-1)

        def _str_(self):
                return self.student.username + "" + self.file_name +""+ self.assignment.name
