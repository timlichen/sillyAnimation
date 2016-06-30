from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
	def login(self, email, password):
		try:
			user = self.get(email = email)
		except:
			return (False, {"login" : "Login Failed"})

		if user and bcrypt.hashpw(password.encode('utf-8'), user.password.encode('utf-8')) == user.password:
			return (True, user)
		return (False, {"Login": "Login Failed"})


	def register(self, first_name, last_name, email, password, conf_password):
		errors = {}

		try:
			users = self.all()
		except:
			users = {}


		if len(first_name) < 2 or not NAME_REGEX.match(first_name):
			errors['first_name'] = "name cannot be less than 2 characters & must have letters only"
		if len(last_name) < 2 or not NAME_REGEX.match(last_name):
			errors['last_name'] = "name cannot be less than 2 characters & must have letters only"
		if len(email) < 1:
			errors['req_email'] = "Email is required"
		if not EMAIL_REGEX.match(email):
			errors['email'] = "Email not valid"
		if len(password) < 8:
			errors['password'] = "Password must be atleast 8 characters"
		if password != conf_password:
			errors['confirm_password'] = "passwords do not match"
		if errors:
			return (False, errors)
		else:
			password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
			if len(users) < 1:
				self.create(first_name=first_name, last_name=last_name, email=email, password=password, role = 1)
			else:
				self.create(first_name=first_name, last_name=last_name, email=email, password=password, role = 0)
			return (True, self.get(email=email))

	def getAll(self):
		return self.all()

	def getOne(self, user_id):
		return self.filter(id=user_id)[0]

	def update_profile(self, user_id, email, first_name, last_name):
		errors = {}
		if len(first_name) < 2 or not NAME_REGEX.match(first_name):
			errors['first_name'] = "name cannot be less than 2 characters & must have letters only"
		if len(last_name) < 2 or not NAME_REGEX.match(last_name):
			errors['last_name'] = "name cannot be less than 2 characters & must have letters only"
		if len(email) < 1:
			errors['req_email'] = "Email is required"
		if not EMAIL_REGEX.match(email):
			errors['email'] = "Email not valid"
		if errors:
			return (False, errors)
		else:
			self.filter(id=user_id).update(email=email, first_name=first_name, last_name=last_name)
			return (True, self.get(email=email))

	def update_profile_admin(self, user_id, email, first_name, last_name, role):
		errors = {}
		if len(first_name) < 2 or not NAME_REGEX.match(first_name):
			errors['first_name'] = "name cannot be less than 2 characters & must have letters only"
		if len(last_name) < 2 or not NAME_REGEX.match(last_name):
			errors['last_name'] = "name cannot be less than 2 characters & must have letters only"
		if len(email) < 1:
			errors['req_email'] = "Email is required"
		if not EMAIL_REGEX.match(email):
			errors['email'] = "Email not valid"
		if errors:
			return (False, errors)
		else:
			self.filter(id=user_id).update(email=email, first_name=first_name, last_name=last_name, role=role)
			return (True, self.get(email=email))

	def update_profile_pw(self, user_id, password, conf_password):
		errors = {}
		if len(password) < 1:
			errors['password'] = "password cannot be blank"
		if password != conf_password:
			errors['confirm_password'] = "passwords do not match"
		if errors:
			return (False, errors)
		else:
			password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
			self.filter(id=user_id).update(password=password)
			return (True, self.get(id=user_id))

	def update_profile_desc(self, user_id, description):
		return self.filter(id=user_id).update(description=description)

	def remove(self, user_id):
		return self.filter(id=user_id).delete()


# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	role = models.IntegerField(default=0)
	email = models.EmailField()
	description = models.TextField(max_length = 1000)
	password = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()
	def __str__(self):
		return self.first_name
	class Meta:
		db_table = "users"
