from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('nihao/', views.hello, name='nihao'),
    path('', views.home, name='home'),

    # path('login/',views.login,name ='login'),
]
