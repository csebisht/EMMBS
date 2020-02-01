from django.contrib import admin
from .models import Employee,Building,GuestInfo,Meeting,MeetingGuest,Room,RoomEquipment


admin.site.register(Employee)
admin.site.register(Building)
admin.site.register(GuestInfo)
admin.site.register(Meeting)
admin.site.register(MeetingGuest)
admin.site.register(Room)
admin.site.register(RoomEquipment)
# Register your models here.
