from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

ANSWER_CHOICES = (
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),
	('D', 'D'),
	('E', 'E'),
)

LEVEL_CHOICES = (
	(1, '1'),
	(2, '2'),
	(3, '3'),
)

class Category(models.Model):
	name = models.CharField(verbose_name="Name", max_length=100)
	description = models.CharField(verbose_name="Description", max_length=200, blank=True)

	def __unicode__(self):
		return self.name

class Question(models.Model):

	category = models.ForeignKey(Category)

	question = models.TextField(verbose_name='Question')

	points = models.IntegerField(default = 5)

	option_a = models.CharField(verbose_name='Option A', max_length=500)
	option_b = models.CharField(verbose_name='Option B', max_length=500)
	option_c = models.CharField(verbose_name='Option C', max_length=500)
	option_d = models.CharField(verbose_name='Option D', max_length=500)
	option_e = models.CharField(verbose_name='Option E', max_length=500)

	correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)

	level = models.IntegerField(verbose_name='Level', choices=LEVEL_CHOICES)

	def __unicode__(self):
		return self.question

class Answer(models.Model):

	user = models.ForeignKey(User)

	question = models.ForeignKey(Question)

	answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)

	is_correct = models.BooleanField(default = False)

	date = models.DateTimeField(auto_now_add=True)

class Badge(models.Model):
	
	category = models.ForeignKey(Category)

	name = models.CharField(verbose_name="Name", max_length=100)

	description = models.CharField(verbose_name="Description", max_length=200)

	def __unicode__(self):
		return self.name