from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Rank(models.Model):
	points = models.IntegerField(default = 0)
	user = models.ForeignKey(User)