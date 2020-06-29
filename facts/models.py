import datetime

from django.db import models
from django.utils import timezone


class Fact(models.Model):
    question = models.TextField()
    answer = models.TextField()
    additional = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
