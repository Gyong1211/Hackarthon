from django.conf.urls import url

from . import views

app_name = 'attendance'

urlpatterns = [
    url(r'^create/$', views.attendance_create, name='attendance_check'),
]