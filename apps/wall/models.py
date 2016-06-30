from __future__ import unicode_literals
from ..login_reg.models import User
from django.db import models

class MessageManager(models.Manager):

	def addMessage(self, wall_id, message, user):
		print wall_id
		print message
		print user
		print "IN ADD MESSAGE MODEL MANAGER"
		errors = {}
		if len(message) < 1:
			errors['message'] = "Message cannot be blank"
		if errors:
			return (False, errors)
		else:
			user = User.userManager.getOne(user)
			wall = User.userManager.getOne(wall_id)
			print user.id
			print wall.id
			self.create(message=message, wall=wall, user=user)
			return (True, True)

	def getAll(self, wall_id):
		return self.filter(wall = wall_id)

	def getOne(self,msg_id):
		return self.filter(id = msg_id)


class CommentManager(models.Manager):
	def addComment(self, msg_id, comment, user):
		errors = {}
		if len(comment) < 1:
			errors['comment'] = "Comment cannot be blank"
		if errors:
			return (False, errors)
		else:
			msg = Message.messageManager.getOne(msg_id)[0]
			user = User.userManager.getOne(user)
			print "Message - ",msg
			print "USER - ",user
			self.create(comment=comment, user = user, message = msg)
			return (True, True)

	def getAll(self):
		return self.all()

# Create your models here.
class Message(models.Model):
	message = models.TextField()
	wall = models.ForeignKey(User, related_name = "wall")
	user = models.ForeignKey(User, related_name = "user")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	messageManager = MessageManager()
	objects = models.Manager()
	def __str__(self):
		return self.message
	class Meta:
		db_table = "messages"

class Comment(models.Model):
	comment = models.TextField()
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	commentManager = CommentManager()
	objects = models.Manager()
	def __str__(self):
		return self.comment
	class Meta:
		db_table = "comments"