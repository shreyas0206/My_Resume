from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display=['p_name','p_skills','p_details']
admin.site.register(Project,ProjectAdmin)