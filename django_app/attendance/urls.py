from django.conf.urls import url

from . import views

app_name = 'attendance'

urlpatterns = [
    url(r'^check/$', views.attendance_check, name='attendance_check'),
]