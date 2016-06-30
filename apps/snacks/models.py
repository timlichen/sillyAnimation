from __future__ import unicode_literals

from django.db import models

from ..login_reg.models import User

class SnackManager(models.Manager):

     def snack_request(self, id):
            errors = {}

            if len(snack_request)<1:
                errors['snack_request'] = "Snack Request is too short"

            if errors:
                # print errors
                return (False, errors)

            else:
                self.create(request_snack=request_snack, user=id)
                return (True, self.get(user_email=user_email))

# Create your models here.
class Snack(models.Model):
    snack_request = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    SnackManager = SnackManager()
