from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.utils import timezone

from .models import Attendance

User = get_user_model()


@login_required
def attendance_create(request):
    def is_attend(request):
        cur_year = timezone.now().year
        cur_month = timezone.now().month
        cur_day = timezone.now().day
        return Attendance.objects.filter(
            user=request.user,
            attendance_time__year=cur_year,
            attendance_time__month=cur_month,
            attendance_time__day=cur_day
        ).exists()

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
        if not (request.POST['location_lat'] or request.POST['location_lng']):
            context = {
                "google_map_api_secret": settings.GOOGLE_MAP_API_SECRET,
                "no_position": True
            }
            return render(request, 'attendance/create.html', context=context)

        current_lat = float(request.POST['location_lat'])
        current_lng = float(request.POST['location_lng'])
        distance = calc_distance(current_lat, current_lng)

        if distance <= 0.2:
            Attendance.objects.create(user=request.user)
            return redirect('attendance:attendance_success')
        else:
            context = {
                "google_map_api_secret": settings.GOOGLE_MAP_API_SECRET,
                "distance": distance * 1000
            }
            return render(request, 'attendance/create.html', context=context)
    else:
        if is_attend(request):
            return redirect('attendance:already_attend')
        print(settings.GOOGLE_MAP_API_SECRET)
        context = {
            "google_map_api_secret": settings.GOOGLE_MAP_API_SECRET
        }
        return render(request, 'attendance/create.html', context=context)


def attendance_success(request):
    context = {
        "result": "출석체크 완료! 열공하세요!"
    }
    return render(request, 'attendance/result.html', context=context)


def already_attend(request):
    context = {
        "result": "이미 출석체크 하셨습니다."
    }
    return render(request, 'attendance/result.html', context=context)


def attendance_list(request):
    user_list = User.objects.all()
    attendance_result = []
    for user in user_list:
        cur_year = timezone.now().year
        cur_month = timezone.now().month
        cur_day = timezone.now().day
        attendance_result.append([
            user.username,
            user.attendance_set.filter(
                attendance_time__year=cur_year,
                attendance_time__month=cur_month,
                attendance_time__day=cur_day
            ).exists])
    context = {
        "current_day":"{}년 {}월 {}일 출석표".format(cur_year, cur_month, cur_day),
        "attendance_result": attendance_result
    }
    return render(request, 'attendance/list.html', context=context)