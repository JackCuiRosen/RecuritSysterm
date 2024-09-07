from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import sys

from user.models import userProfile

sys.path.append("..")



# Create your views here.
def hello(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def home(request):

    # print(request.user.)
    template = loader.get_template('home.html')

    if request.user.id is not None:
        is_login = True

        user = userProfile.objects.filter(user__username=request.user.username).first()

        print(user)

    else:
        is_login = False
        user = None

    # print(is_login)
    context = {'is_login': is_login, 'user': user}

    return HttpResponse(template.render(context))
