from django.contrib.auth.models import User
from django.db import models
# Create your models here.

STATUS_CHOICES = [('운행 전', '운행 전'), ('운행 중', '운행 중'), ('운행 종료', '운행 종료')]


class Route(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    cheif = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, null=False, blank=False, default='')

    def __str__(self):
        return self.name
