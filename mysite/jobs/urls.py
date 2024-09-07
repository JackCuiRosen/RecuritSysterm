from django.urls import path

from . import views

urlpatterns = [
     path('jobs/<page_num>/', views.jobs, name = 'job'),
     path('<job_place>/details/',views.jobdetatils,name = 'jobdetails'),
     path('position',views.jobshow,name = "jobshow"),
     path('ajax/get_data/',views.get_jobdata,name='get_data'),
     path('editcandidate/',views.edit_candidate,name = 'edit_candidate'),
     path('mycandidate/',views.mycandidate,name='mycandidate'),
     path('application/',views.acceptRecord,name='accept_record')
]