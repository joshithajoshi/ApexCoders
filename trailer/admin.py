from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm


# Register your models here.
from trailer.models import *

admin.site.register(Account)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Submission)
