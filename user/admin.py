from django.contrib import admin
from .models import Course,Studentdetails,Teacherdetails
# Register your models here.




admin.site.register(Course)

admin.site.register(Studentdetails)
admin.site.register(Teacherdetails)
