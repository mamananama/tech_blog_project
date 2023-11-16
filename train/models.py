from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=True)
    article_slug = models.SlugField(
        "slug", null=False, blank=False, unique=True)
    content = HTMLField()  # models.TextField()에서 수정
    published = models.DateTimeField('Date published', default=timezone.now)
    modified = models.DateTimeField('Date modified', default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.article_slug
