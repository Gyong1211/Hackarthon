from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Attendance


def attendance_create(request):
    def calc_distance(current_lat, current_lng):
        from math import sin, cos, sqrt, atan2, radians
        R = 6373.0
        lat1 = radians(37.517565)
        lng1 = radians(127.018110)
        lat2 = radians(current_lat)
        lng2 = radians(current_lng)

        dlng = lng2 - lng1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    if request.method == 'POST':
        current_lat = float(request.POST['location_lat'])
        current_lng = float(request.POST['location_lng'])
        print(calc_distance(current_lat, current_lng))
        if calc_distance(current_lat, current_lng) <= 0.4:
            Attendance.objects.create(user=request.user)
            return HttpResponse('출첵 성공')
        else:
            return HttpResponse('거리가 멀어요')
    else:
        print(settings.GOOGLE_MAP_API_SECRET)
        context = {
            "google_map_api_secret": settings.GOOGLE_MAP_API_SECRET
        }
        return render(request, 'attendance/attendance.html', context=context)
