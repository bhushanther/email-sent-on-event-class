
from django.contrib import admin
from django.urls import path
from app12 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event-email/',views.EventEmailView.as_view(), name='event-email'),
]
