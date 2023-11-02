from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Route(models.Model):
    name = models.CharField(max_length=32)
    cheif = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
