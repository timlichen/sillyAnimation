from __future__ import unicode_literals
from ..login_reg.models import User
from django.db import models

class MessageManager(models.Manager):
	pass

# Create your models here.
class Message(models.Model):
	title = models.CharField(max_length=200)
	message = models.TextField()
	image = models.ImageField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	messageManager = MessageManager()

