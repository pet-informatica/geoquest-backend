import django_filters

from .models import *

class RankFilter(django_filters.FilterSet):

	class Meta:
		model = Rank