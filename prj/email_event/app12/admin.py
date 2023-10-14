from django.contrib import admin

from .models import Employee, EmailLog, Event

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','email']
                        
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=['id','employee', 'event_type', 'event_date','subject', 'body']   


     


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display=['id','name','event_type','status','error_message', 'sent_at']     





    
