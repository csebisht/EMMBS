from django.db import models

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


