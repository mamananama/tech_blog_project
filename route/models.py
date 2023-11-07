from .validators import validate_file_size, validate_image_size
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


# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    file = models.FileField(upload_to='station/files/%Y/%m/%d/', blank=True,
                            null=True, max_length=None, validators=[validate_file_size])
    image = models.ImageField(upload_to='station/images/%Y/%m/%d/', blank=True,
                              null=True, max_length=None, validators=[validate_image_size])
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
