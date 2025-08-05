from django.contrib import admin
from .models import Student, Query

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['fname', 'email', 'contact']
    search_fields = ['fname', 'email']

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email']
    readonly_fields = ['name', 'email', 'message']
