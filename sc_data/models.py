from django.db import models

# Create your models here.
COMPUTER_TYPE = [
    ("Apple", "Apple"),
    ("Windows PC", "Windows PC"),
    ("Linux PC", "Linux PC"),
    ("Tablet", "Tablet"),
]
MEDIA_TYPE = [
    ("Projector", "Projector"),
    ("Microphone", "Microphone"),
    ("Online media stream", "Online media stream"),
    ("Tv", "Tv"),
    ("Printer", "Printer"),
]
LAB_TYPE = [
    ("Network", "Network"),
    ("Web design", "Web design"),
    ("Software development", "Software development"),
]
BOARD_TYPE = [
    ("Wall-mounted", "Wall-mounted"),
    ("Mobile whiteboard", "Mobile whiteboard"),
    ("Glassboard", "Glassboard"),
    ("Glassboard", "Chalkboard"),
]
DAYS=[
    ("MON","Monday"),
    ("TUE","Tuesday"),
    ("WED","Wednesday"),
    ("THUR","Thursday"),
    ("FRI","Friday"),
    ("SAT","Saturday"),
    ("SUN","Sunday"),
]

class Schedule(models.Model):
    # year, semester, sessions, rooms, classes
    year = models.IntegerField()
    semester = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.year}-sem{self.semester}' 


class Teacher(models.Model):
    # id, name, rank, email, none, one or more classes of a unit, one or more media
    name = models.CharField(max_length=1000)
    rank = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Lab(models.Model):
    # id labtype(network, webdesign, software dept), computer or computers of diff types
    lab_type = models.CharField(max_length=1000, choices=LAB_TYPE)

    def __str__(self):
        return self.lab_type

class Computer(models.Model):
    # computertype(apple, windowspc,linxpc, tablet) desc, memorysize, processorspeed
    description = models.TextField()
    memory_size = models.CharField(max_length=1000)
    processor_speed = models.CharField(max_length=1000)
    computer_type = models.CharField(max_length=100, choices=COMPUTER_TYPE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.computer_type

class Media(models.Model):
    # mediatype(projector,microphone,online media stream, printer, tv)
    media_type = models.CharField(max_length=1000, choices=MEDIA_TYPE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.media_type} - {self.teacher.name}'


class Classroom(models.Model):
    # boardtype(wall-mounted,mobile whiteboard, glassboard, chalkboard) 
    board_type = models.CharField(max_length=1000, choices=BOARD_TYPE)

    def __str__(self):
        return self.board_type

class Building(models.Model):
    # name, Id
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Room(models.Model):
    # buildingId, RoomID, capacity, type(lab, classrom), media
    # room has one building and cannot be a lab and classroom at the same time
    # room has one or more media or none
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    capacity = models.CharField(max_length=1000)
    # room_type = models
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_type

class Prerequisites(models.Model):
    name = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Prerequisites'

    def __str__(self):
        return self.name

class Unit(models.Model):
    # unitId, unitdescription, credits, one or more classes
    # can have none one or many prerequisites
    unit_description = models.TextField()
    unit_credits = models.CharField(max_length=1000)
    prerequisites = models.ForeignKey(Prerequisites, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.unit_description



class Class(models.Model):
    # id, enrollmentlimit, units
    enrollment_limit = models.CharField(max_length=1000)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.enrollment_limit 


class Session(models.Model):
    # dayofweek, starttime, endtime, oneteacher
    day_of_week = models.CharField(max_length=1000, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.day_of_week  