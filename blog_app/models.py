from django.db import models
from django.utils import timezone
import datetime


class Post(models.Model):
    def __str__(self):
        return self.post_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    app_label = 'blog_app'
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateTimeField("date published")
