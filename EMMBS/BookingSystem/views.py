from django.shortcuts import render,redirect
from .models import Room,RoomEquipment,Meeting
from django.contrib import messages
# Create your views here.
def index(request):
    room = Room.objects.all()
    roomequip=RoomEquipment.objects.all()
    print(room)
    return render(request, "index.html", {"Room_detail": room,"roomEquipment":roomequip})


def BookMeeting(request):
    if request.method == 'POST':
        MeetingDate = request.POST['MeetingDate']
        StartTime = request.POST['StartTime']
        EndTime = request.POST['EndTime']
        Purpose = request.POST['Purpose']
        RoomId = request.POST['RoomId']
        #meeting = Meeting(request.POST)
        meeting = Meeting.objects.create(EmployeeId=1,MeetingDate=MeetingDate, StartTime=StartTime, EndTime=EndTime, Purpose=Purpose,RoomId=RoomId,CreationDate=MeetingDate,CreationBy=1)
        meeting.save()
        if meeting is not None:
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('MeetingList')
    return render(request ,"MeetingList.html")

def MeetingList(request):
    if request.method == 'POST':
        MeetingDate = request.POST['MeetingDate']
        StartTime = request.POST['StartTime']
        EndTime = request.POST['EndTime']
        room = Room.objects.all()
        roomequip = RoomEquipment.objects.all()
        for meeting in Meeting.objects.filter(MeetingDate=MeetingDate).filter(StartTime=StartTime).filter(EndTime=EndTime):
            print("meeting  " ,meeting)
            for Rroom in room:
                print("Room ",Rroom)
                if Rroom.id == meeting.roomId:
                     print("asd")
                else:
                     print("asdasd")
        if Meeting.objects.filter(MeetingDate=MeetingDate).filter(StartTime=StartTime).filter(EndTime=EndTime).exists():
            messages.info(request, "Meeting Booked Already")
            return redirect('/')
        else:
            return render(request,'MeetingList.html',{"Room_detail": room,"roomEquipment":roomequip,"MeetingDate":MeetingDate,"StartTime":StartTime,"EndTime":EndTime})
    return  redirect('/')

def MeetingList12(request):
    if request.method == 'POST':
        MeetingDate = request.POST['MeetingDate']
        StartTime = request.POST['StartTime']
        EndTime = request.POST['EndTime']
        room = Room.objects.all()
        roomequip = RoomEquipment.objects.all()

        if Meeting.objects.filter(MeetingDate=MeetingDate).filter(StartTime=StartTime).filter(EndTime=EndTime).exists():
            messages.info(request, "Meeting Booked Already")
            return redirect('/')
        else:
            Meeting.object.get()
            return render(request,'MeetingList.html',{"Room_detail": room,"roomEquipment":roomequip,"MeetingDate":MeetingDate,"StartTime":StartTime,"EndTime":EndTime})
    return  redirect('/')