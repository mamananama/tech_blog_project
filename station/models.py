from django.db import models
from .validators import validate_file_size, validate_image_size
# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    tag = models.CharField(max_length=32)
    file = models.FileField(upload_to='station/files/%Y/%m/%d/', blank=True,
                            null=True, max_length=None, validators=[validate_file_size])
    image = models.ImageField(upload_to='station/images/%Y/%m/%d/', blank=True,
                              null=True, max_length=None, validators=[validate_image_size])

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title
