import math
from datetime import datetime

from django.db import models
from django.utils import timezone


class Blog(models.Model):
    SUBJECT_MAX_LENGTH = 30
    SHORT_DESCRIPTION_MAX_LENGTH = 40
    IMAGE_UPLOAD_URL = 'blog/'

    subject = models.CharField(
        max_length=SUBJECT_MAX_LENGTH,
    )

    short_description = models.CharField(
        max_length=SHORT_DESCRIPTION_MAX_LENGTH,
    )

    large_description = models.TextField()

    date = models.DateTimeField(
        default=datetime.now,
    )

    image_url = models.ImageField(
        upload_to=IMAGE_UPLOAD_URL,
    )

    def __str__(self):
        return self.subject


class Comment(models.Model):
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True, related_name='replies')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} written by {self.email}'

    # x minutes ago etc
    def when_published(self):
        now = timezone.now()

        diff = now - self.created_on

        if diff.days == 0 and 0 <= diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and 60 <= diff.seconds < 3600:
            minutes = math.floor(diff.seconds / 60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and 3600 <= diff.seconds < 86400:
            hours = math.floor(diff.seconds / 3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if 1 <= diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if 30 <= diff.days < 365:
            months = math.floor(diff.days / 30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days / 365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"
