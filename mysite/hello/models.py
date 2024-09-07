from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models

# Create your models here.

MAJORS = (
    ("1","软件工程"),
    ("2","计算机科学"),
    ("3","网络安全"),
    ("4","电子信息"),
    ("5","数学"),
    ("6","统计学")
)


class Person(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    age = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(150)
    ])
    province = models.CharField(max_length=25)
    city = models.CharField(max_length=25)

    hobby = models.CharField(max_length=25)

    major = models.CharField(max_length=10,choices=MAJORS)



