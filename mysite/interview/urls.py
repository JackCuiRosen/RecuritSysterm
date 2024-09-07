
from django.urls import path

from . import views

urlpatterns = [
     path('interview/',views.interviewHome,name='interview_home'),
     path('sendresume/',views.sendResume,name='sendresume'),
     path('interview/<str:username>',views.startInterview,name='interviewHome'),
     path('interviewer/logout/',views.interviewerLogout,name='interviewLogout'),
]