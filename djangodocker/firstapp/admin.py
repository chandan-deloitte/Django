from django.contrib import admin
from firstapp.models import Projects
from firstapp.models import Issues

class firstappAdmin(admin.ModelAdmin):
    list_display=('projects_id','projects_description','projects_title','projects_creator') 

admin.site.register(Projects,firstappAdmin)

class firstappAdmin(admin.ModelAdmin):
    list_display=('issues_id','issues_type','issues_title','issues_description','issues_reporter','issues_assignee','issues_status') 

admin.site.register(Issues,firstappAdmin)



# Register your models here.
