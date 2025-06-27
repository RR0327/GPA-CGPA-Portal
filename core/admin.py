from django.contrib import admin
from .models import SemesterResult, Subject

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

@admin.register(SemesterResult)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('user', 'semester_name', 'gpa', 'total_credits')
    inlines = [SubjectInline]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('semester', 'name', 'mark', 'credit')
