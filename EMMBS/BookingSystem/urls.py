from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('MeetingList/', views.MeetingList, name='MeetingList'),
    path('BookMeeting/', views.BookMeeting, name='BookMeeting'),
    path('Calender/', views.CalendarView.as_view(), name='Calender'),
    path('event/', views.event, name='event_new'),
	url(r'^BookingSystem/edit/(?P<meetEvent_id>\d+)/$', views.event, name='event_edit'),

]