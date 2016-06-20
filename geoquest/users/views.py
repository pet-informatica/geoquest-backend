import random
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView #temp for mocks
from django.views.decorators.http import require_http_methods #temp for mocks

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework import filters
from rest_framework.response import Response

from .models import *
from .serializers import *
from .filters import *

from tapioca_facebook import Facebook
from allauth.socialaccount.models import *

class RankList(ListAPIView):
	serializer_class = RankSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = RankFilter
	friend_list = {}

	def get_serializer_context(self):
		return self.friend_list

	def get_queryset(self):
		user = self.request.user
		sacc = SocialAccount.objects.get(user = user) #Social Account
		stkn = SocialToken.objects.get(account = sacc) #Social Token
		api = Facebook(access_token=stkn.token)
		requests = api.user_friends(id='me').get(params={'fields':'id,picture.type(large)'})

		for request in requests().pages():
			self.friend_list[request._data['id']] = request._data['picture']['data']['url']

		return Rank.objects.filter(social_account__uid__in=self.friend_list).order_by('-points')


class StatisticsList(ListAPIView):
	serializer_class = UserStatsSerializer

	def get_queryset(self):
		user = self.request.user

		return UserStatistics.objects.filter(user = user)
