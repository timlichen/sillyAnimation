from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    details = models.TextField()
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
