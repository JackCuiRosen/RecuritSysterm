from django.contrib.auth.models import User
from django.db import models

# Create your models here.


InterviewerType = [
    (0,'一面面试官'),
    (1,'二面面试官'),
    (2,'待定'),
]

class userProfile(models.Model):

    nickname = models.CharField(verbose_name="昵称",max_length=20)
    avatar = models.ImageField(verbose_name="头像", blank=True)
    phone = models.CharField(verbose_name="电话",blank=True,max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
   

class Interviewer(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=20)
    department = models.CharField(verbose_name="部门",max_length=20)
    jobname = models.CharField(verbose_name="工作",max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.IntegerField(verbose_name="面试官类型",choices=InterviewerType,default=2)


    def __str__(self):
        return self.name

