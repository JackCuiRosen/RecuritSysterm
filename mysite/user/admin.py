from django.contrib import admin
from django.contrib.auth.models import User

from user.models import userProfile, Interviewer


# Register your models here.

class userProfileAdmin(admin.ModelAdmin):
    list_display = ['nickname','phone']

class interviewerManager(admin.ModelAdmin):
    list_display = ['name','department','jobname']

admin.site.register(userProfile,userProfileAdmin)

admin.site.register(Interviewer,interviewerManager)