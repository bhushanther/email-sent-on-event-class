from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Event, Employee, EmailLog
import datetime

class GetEventsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_events_with_data(self):
       
        event_date = datetime.date.today()
        employee = Employee.objects.create(
            name="bhushan ther",
            email="bhushther12@gmail.com",
        )
        employee.save()
        event = Event.objects.create(
            employee=employee,
            event_date=event_date,
            event_type="birthday",
            subject="wish",
            body="Happy birthday",
        )
        event.save()
        
        url = reverse('event-email')  
        response = self.client.get(url)

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

          