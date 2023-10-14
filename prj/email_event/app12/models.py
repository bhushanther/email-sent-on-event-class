from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
     

    def __str__(self) -> str:
        return self.name

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    event_date = models.DateField()
    subject = models.CharField(max_length=200)
    body = models.TextField()


   

class EmailLog(models.Model):
    
    name=models.CharField(max_length=150)
    event_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    error_message = models.TextField(null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)


