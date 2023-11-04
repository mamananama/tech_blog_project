from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_size, validate_image_size
from route.models import Route
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
