from django.conf.urls import url

from . import views

app_name = 'attendance'

urlpatterns = [
    url(r'^create/$', views.attendance_create, name='attendance_create'),
    url(r'^result/$', views.attendance_success, name='attendance_success'),
    url(r'^already/$', views.already_attend, name='already_attend'),
]