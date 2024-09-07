from django import forms

import hashlib

from django.conf import settings
from django.forms import ModelForm


class BootstrapForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label

            else:
                field.widget.attrs = {
                    "class":"form-control",
                    "placeholder":field.label
                }




def md5(password):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(password.encode('utf-8'))

    return obj.hexdigest()

import string
import random


# 生成指定长度的随机数
def gen_random_str(length: int = 4, is_digits: bool = True) -> str:
    words = string.digits if is_digits else string.ascii_letters + string.digits
    return ''.join(random.sample(words, length))
