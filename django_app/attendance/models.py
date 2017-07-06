from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_time = models.DateTimeField(auto_now_add=True)

