from django.contrib import admin

# Register your models here.

from .models import InterviewResult,resumeSubmitRecord,qqGroup

class InterviewResultManager(admin.ModelAdmin):
    list_display = ['education_background','project_experience','profession_level','interview_name','status']

class ResumeSumbitRecordManager(admin.ModelAdmin):
    list_display = ['job','user','department','qqgroup_id','final_grade']


class qqGroupManager(admin.ModelAdmin):
    list_display = ['qqGroupNum','department']

admin.site.register(InterviewResult,InterviewResultManager)

admin.site.register(resumeSubmitRecord,ResumeSumbitRecordManager)

admin.site.register(qqGroup,qqGroupManager)