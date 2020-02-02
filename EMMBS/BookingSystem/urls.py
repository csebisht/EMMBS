from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('MeetingList/', views.MeetingList, name='MeetingList'),
    path('BookMeeting/', views.BookMeeting, name='BookMeeting'),

]