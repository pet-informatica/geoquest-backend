import django_filters

from .models import *

class QuestionFilter(django_filters.FilterSet):
	level = django_filters.NumberFilter(name="level")
	category = django_filters.NumberFilter(name="category")

	class Meta:
		model = Question
		fields = ['level', 'category']