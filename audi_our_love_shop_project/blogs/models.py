from datetime import datetime

from django.db import models


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
