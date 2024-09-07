from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class JobManager(models.Manager):
    def findAll(self,keyword):
        return self.filter(WorkKind__contains=keyword) | self.filter(JobDescrib__contains=keyword) |  self.filter(WorkPlace__contains=keyword) | self.filter(JobID__contains=keyword)| self.filter(JobRequire__contains=keyword)

class Job(models.Model):
    JobName = models.CharField(max_length= 10)
    WorkPlace = models.CharField(max_length=10)
    WorkKind = models.CharField(max_length=10)
    JobID = models.CharField(max_length=20)
    JobDescrib = models.TextField(max_length=1000)
    JobRequire = models.TextField(max_length=1000)
    objects = JobManager()

    def __str__(self):
        return self.JobID


class candidate(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="姓名",max_length=20)
    phone = models.CharField(verbose_name="电话",max_length=20)
    email = models.CharField(verbose_name="邮箱",max_length=20)
    job_wanted = models.CharField(verbose_name="求职意向",max_length=25)
    education = models.TextField(verbose_name="教育经历",max_length=1000,blank=True)
    project = models.TextField(verbose_name='项目经历',max_length=1000,blank=True)
    award = models.CharField(verbose_name='获得奖项',max_length=250,blank=True)
    social = models.CharField(verbose_name='社交账号',max_length=250,blank=True)
    evaluation = models.TextField(verbose_name='自我评价',max_length=1000,blank=True)
    advantage = models.TextField(verbose_name="个人优势",max_length=1000,blank=True)
    candidate_position = models.FileField(verbose_name='简历位置',blank=True)
    last_editTime = models.DateTimeField(auto_now=True)


