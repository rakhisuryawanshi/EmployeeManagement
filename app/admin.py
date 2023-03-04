from django.contrib import admin
from .models import EmployeeManagement

@admin.register(EmployeeManagement)
class adminclassEmployee(admin.ModelAdmin):
    list_display=['First_name','last_name','EmailId','Mobile','Address','Blood_Group']

# Register your models here.
