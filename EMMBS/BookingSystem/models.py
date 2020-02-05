from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from calendar import HTMLCalendar

from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.html import conditional_escape as esc

# Create your models here.

class GuestInfo(models.Model):
    GuestName=models.CharField(max_length=100)
    Address=models.TextField()
    City=models.TextField()
    State = models.TextField()
    Zip = models.TextField()
    Occupation = models.TextField()
    Designation = models.TextField()
    LengthOfStay = models.IntegerField()
    PhoneNo=models.IntegerField()
    IsActive=models.BooleanField(default=True)
    GuestImage = models.ImageField(upload_to='pics')
    CreationDate = models.DateField()
    CreationBy = models.IntegerField()

class Building(models.Model):
    Address1 = models.TextField()
    Address2 = models.TextField()
    City = models.TextField()
    State = models.TextField()
    Zip = models.TextField()
    Floor = models.TextField()
    IsActive=models.BooleanField(default=True)
    Image = models.ImageField(upload_to='pics')
    CreationDate = models.DateField()
    CreationBy = models.IntegerField()

class Room(models.Model):
    buildingId=models.IntegerField()
    RoomNumber=models.TextField()
    Name=models.CharField(max_length=100)
    Capacity=models.TextField()
    RoomInfo=models.TextField()
    RoomDescription = models.TextField()
    RoomImage=models.ImageField(upload_to='pics')
    IsActive = models.BooleanField(default=True)
    CreationDate = models.DateField()
    CreationBy = models.IntegerField()

class Employee(models.Model):
    EmployeeCode=models.TextField()
    Email =models.TextField()
    Name = models.TextField()
    Department = models.TextField()
    Designation = models.TextField()
    UserName=models.TextField()
    Password=models.TextField()
    Image = models.ImageField(upload_to='pics')
    IsActive = models.BooleanField(default=True)
    CreationDate = models.DateField()
    CreationBy = models.IntegerField()

class Meeting(models.Model):
    EmployeeId=models.IntegerField()
    EmployeeCode = models.TextField()
    Purpose=models.TextField()
    RoomId=models.IntegerField()
    MeetingDate=models.DateField()
    StartTime = models.TextField()
    EndTime = models.TextField()
    IsActive=models.BooleanField(default=True)
    CreationDate = models.DateField()
    CreationBy = models.IntegerField()

class MeetingGuest(models.Model):
    MeetingId=models.IntegerField()
    GuestId=models.IntegerField()
    CreationDate = models.DateField()
    CreationBy = models.IntegerField()


class RoomEquipment(models.Model):
    RoomId=models.IntegerField()
    SeatAvail=models.TextField()
    Area = models.TextField()
    Speed = models.TextField()
    Projector=models.BooleanField(default=True)
    otherEquip=models.TextField()


class Event(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (
                new_end >= fixed_start and new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))




class WorkoutCalendar(HTMLCalendar):

    def __init__(self, Event):
        super(WorkoutCalendar, self).__init__()
        self.Event = self.group_by_day(Event)

    def formatday(self, day, weekday):
        if day != 0:
            print('pradeep')
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.Event:
                cssclass += ' filled'
                body = ['<ul>']
                for Event in self.Event[day]:
                    body.append('<li>')
                    body.append('<a href="%s">' % Event.get_absolute_url())
                    body.append(esc(Event.notes))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(WorkoutCalendar, self).formatmonth(year, month)

    def group_by_day(self, Event):
        field = lambda Event: Event.performed_at.day
        return dict(
            [(day, list(items)) for day, items in groupby(Event, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)