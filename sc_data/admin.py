from django.contrib import admin
from .models import (Teacher, Lab, Computer, Media, 
                     Classroom, Building, Room, Unit,
                     Prerequisites, Class, Session, Schedule)

# Register your models here.

admin.site.register(Schedule)
admin.site.register(Teacher)
admin.site.register(Lab)
admin.site.register(Computer)
admin.site.register(Media)
admin.site.register(Classroom)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Unit)
admin.site.register(Prerequisites)
admin.site.register(Class)
admin.site.register(Session)






