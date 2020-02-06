from __future__ import unicode_literals
from django.contrib import admin
from .models import Employee,Building,GuestInfo,Meeting,MeetingGuest,Room,RoomEquipment,MeetEvent
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe



admin.site.register(Employee)
admin.site.register(Building)
admin.site.register(GuestInfo)
admin.site.register(Meeting)
admin.site.register(MeetingGuest)
admin.site.register(Room)
admin.site.register(RoomEquipment)
# Register your models here.
admin.site.register(MeetEvent)
