from django.contrib import admin
from . import models

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','yoshi','kurs','guruhi')
    list_editable = ('name',)
    search_fields = ['name']
    
    