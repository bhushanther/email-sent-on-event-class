from django.core.mail import send_mail
import datetime
from .models import Employee, EmailLog
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class EventEmailView(APIView):
    def get(self, request):
        current_date = datetime.date.today()
        current_month, current_day = current_date.month, current_date.day

        employees = Employee.objects.filter(event__event_date__month=current_month, event__event_date__day=current_day).values('id', 'name', 'email', 'event__event_type', 'event__subject', 'event__body')
        
        
       
        if employees:
            for employee in employees:
                
                try:
                    send_mail(
                        subject=employee['event__subject'],
                        message=employee['event__body'],
                        from_email='bhushther@gmail.com',
                        recipient_list=[employee['email']],
                        
                    )
                    
                    status_value = 'delivery success'
                    error_message = 'no error'
                    
                except Exception as e:
                    status_value = 'delivery fail'
                    error_message = 'error'
                
            
                
                employee_instance = Employee.objects.get(pk=employee['id'])
                

               
                EmailLog.objects.create(
                    name=employee['name'],
                    event_type=employee['event__event_type'],
                    status=status_value,
                    error_message=error_message,
                    sent_at=current_date
                )

            return Response({'success': 'email sent'}, status=status.HTTP_200_OK)
        else:
            EmailLog.objects.create(
                    name='no event',
                    event_type='no event',
                    status='no event',
                    error_message='no event',
                    sent_at=current_date
                )
            return Response({'msg': 'no record found'}, status=status.HTTP_200_OK)
