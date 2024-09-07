from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from jobs.models import Job

from django.contrib.auth.models import User
from user.models import Interviewer

# Create your models here.

# class ResumeSubmitRecorde(models.Model):

STATUS_CHOICE = [
    (0, '不建议录取'),
    (1, '建议录取'),
    (2, '建议进行二面'),
    (3, '待定'),
]
GroupFor = [
    (0, '研发'),
    (1, '产品'),
    (2, '运营'),
    (3, '销售'),
    (4, '市场'),
    (5, '设计'),
]

InterviewerType = [
    (0,'一面面试官'),
    (1,'二面面试官'),
    (2,'待定'),
]


class InterviewResult(models.Model):
    education_background = models.FloatField(
        verbose_name="教育背景得分",
        validators=[MinValueValidator(0), MaxValueValidator(15)]
    )
    project_experience = models.FloatField(
        verbose_name="项目经历得分",
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )
    profession_level = models.FloatField(
        verbose_name="专业水平得分",
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )
    learning_ability = models.FloatField(
        verbose_name="学习能力得分",
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )

    english_level = models.FloatField(
        verbose_name="英语水平得分",
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    expression_ability = models.FloatField(
        verbose_name="表达能力得分",
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    cooperation_ability = models.FloatField(
        verbose_name="合作能力得分",
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

    type = models.IntegerField(verbose_name="面试类型", choices=InterviewerType,default=2)

    evaluation = models.TextField(verbose_name="面试官评价")

    interview_name = models.CharField(verbose_name="面试官", max_length=20)

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default=3)

    sumScore = models.FloatField(verbose_name='面试得分',blank=True, null=True)

    last_editTime = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        self.sumScore = sum(
            [float(self.education_background), float(self.project_experience), float(self.profession_level), float(self.learning_ability),
             float(self.english_level), float(self.expression_ability), float(self.cooperation_ability)])


        if self.sumScore < 60:
            self.status = 0
        elif self.sumScore >=60 and self.sumScore < 80 and self.type == 0:
            self.status = 2
        else:
            self.status = 1
        super().save(*args, **kwargs)

    class Meta:
        unique_together=(('user','type'),)

class resumeSubmitRecord(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(verbose_name="部门", max_length=50)
    interviewer1 = models.ForeignKey(Interviewer, null=True, on_delete=models.SET_NULL, related_name='FirstInterviewer')
    interviewResult1 = models.OneToOneField(InterviewResult, on_delete=models.SET_NULL,
                                            related_name='FirstInterviewResult', null=True, blank=True)
    interviewer2 = models.ForeignKey(Interviewer, null=True, on_delete=models.SET_NULL,
                                     related_name='SecondInterviewer')
    interviewResult2 = models.OneToOneField(InterviewResult, on_delete=models.SET_NULL,
                                            related_name='SecondInterviewResult', null=True, blank=True)

    qqgroup_id = models.CharField(verbose_name='面试通知群组', max_length=50)
    status = models.BooleanField(verbose_name='工单状态', default=False)
    final_grade = models.FloatField(verbose_name="最终成绩", blank=True, default=0)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'department'),)

    def save(self,*args,**kwargs):

        if self.interviewResult1 and self.interviewResult2:
            self.final_grade = (self.interviewResult1.sumScore + self.interviewResult2.sumScore)/2
        super().save(*args, **kwargs)



class qqGroup(models.Model):
    qqGroupNum = models.CharField(verbose_name='qq群组号', max_length=20)
    department = models.CharField(verbose_name='部门', max_length=20)

    def __str__(self):
        return self.qqGroupNum
