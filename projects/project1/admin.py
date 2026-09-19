from django.contrib import admin
from .models import Students
# Register your models here.

@admin.register(Students)

class StudentAdmin (admin.ModelAdmin):
    list_display =('name','age','email','course','city')
    search_fields =('name','age','course')
    list_filter =('age','course','city',)
    ordering = ('name','email')
    readonly_fields =['name']
    # list_per_page =2

    


