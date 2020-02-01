from django.shortcuts import render
from .models import Room,RoomEquipment
# Create your views here.
def index(request):
    room = Room.objects.all()
    roomequip=RoomEquipment.objects.all()
    print(room)
    return render(request, "index.html", {"Room_detail": room,"roomEquipment":roomequip})
