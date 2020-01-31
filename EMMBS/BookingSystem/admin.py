from django.contrib import admin
from .models import Employee,Building,GuestInfo,Meeting,MeetingGuest,Room


admin.site.register(Employee)
admin.site.register(Building)
admin.site.register(GuestInfo)
admin.site.register(Meeting)
admin.site.register(MeetingGuest)
admin.site.register(Room)
# Register your models here.
