from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import *
from geoquest.questions.models import *

class Rank(models.Model):
	points = models.IntegerField(default = 0)
	user = models.ForeignKey(User)
	social_account = models.ForeignKey(SocialAccount)

	def __unicode__(self):
		return "%s %d"  % (self.user.username, self.points)

class CategoryPoints(models.Model):
	points = models.IntegerField(default = 0)
	category = models.ForeignKey(Category)
	completed = models.FloatField(default = 0.0)

	def __unicode__(self):
		return "%s %d" % (self.category.name, self.points)


class UserStatistics(models.Model):
	user = models.ForeignKey(User)
	best_category = models.ForeignKey(Category)
	completed = models.FloatField(default = 0.0)
	categories = models.ManyToManyField(CategoryPoints)
	position = models.IntegerField(default = 0)
	last_updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%d %s" % (self.position, self.user.username)