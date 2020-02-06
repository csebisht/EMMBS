from django.shortcuts import render,redirect
from .models import Room,RoomEquipment,Meeting,MeetEvent
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from .utils import Calendar
#from datetime import datetime
from datetime import datetime , date, time,timedelta
from django.utils.safestring import mark_safe
import calendar
from .forms import EventForm
from django.urls import reverse

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

def MeetingList12(request):
    if request.method == 'POST':
        MeetingDate = request.POST['MeetingDate']
        StartTime = request.POST['StartTime']
        EndTime = request.POST['EndTime']
        RoomId = request.POST['RoomId']
        room = Room.objects.all()
        roomequip = RoomEquipment.objects.all()
        for meeting in Meeting.objects.filter(RoomId=RoomId).filter(MeetingDate=MeetingDate).filter(StartTime=StartTime).filter(EndTime=EndTime):
            print("meeting  " ,meeting)
            for Rroom in room:
                print("Room ",Rroom)
                if Rroom.id == meeting.RoomId:
                     print("Meeting Booked Already Room",meeting.RoomId)
                else:
                     print("Meeting Booked Free Room",meeting.RoomId)
        if Meeting.objects.filter(RoomId=RoomId).filter(MeetingDate=MeetingDate).filter(StartTime=StartTime).filter(EndTime=EndTime).exists():
            messages.info(request, "Meeting Booked Already")
            return redirect('/')
        else:
            messages.info(request, "Meeting Booked Successfully")
            return render(request,'MeetingList.html',{"Room_detail": room,"roomEquipment":roomequip,"MeetingDate":MeetingDate,"StartTime":StartTime,"EndTime":EndTime})
    return  redirect('/')

def MeetingList(request):
    if request.method == 'POST':
        MeetingDate = request.POST['MeetingDate']
        StartTime = request.POST['StartTime']
        EndTime = request.POST['EndTime']
        RoomId = request.POST['RoomId']
        room = Room.objects.all()
        #room=room.exclude(id=RoomId)
        roomequip = RoomEquipment.objects.all()
        for i in Meeting.objects.filter(MeetingDate=MeetingDate).filter(StartTime=StartTime).filter(EndTime=EndTime):
            print(i.id)
        if Meeting.objects.filter(RoomId=RoomId).filter(MeetingDate=MeetingDate).filter(StartTime=StartTime).filter(EndTime=EndTime).exists():
            messages.info(request, "Meeting Booked Already")
            return redirect('/')
        else:
            messages.info(request, "Meeting Booked Successfully")
            print("RoomId ", RoomId)
            return render(request,'MeetingList.html',{"Room_detail": room,"roomEquipment":roomequip,"MeetingDate":MeetingDate,"StartTime":StartTime,"EndTime":EndTime,"RoomId":RoomId})
    return  redirect('/')




class CalendarView(generic.ListView):
    model = MeetEvent
    template_name = 'Newcalendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context



def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def event(request, event_id=None):
    instance = MeetEvent()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = MeetEvent()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('Calender'))
    return render(request, 'event.html', {'form': form})
