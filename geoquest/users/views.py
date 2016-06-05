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

class RankList(ListAPIView):
	serializer_class = RankSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = RankFilter

	def get_queryset(self):
		return Rank.object.none()


def mock_rank(request):
	mock_answer = """{"rank": [
		{
		  "categories": {
			"1": 365,
			"2": 200,
			"3": 11,
			"4": 0,
			"5": 0
		  },
		  "points": 576,
		  "name": "Bruno Soares da Silva",
		  "picture": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpt1/v/t1.0-1/p200x200/13165943_1433381956687402_454362039857567441_n.jpg?oh=b50040588863a35540a3d3ba588f2648&oe=57C2C1C3&__gda__=1472645566_814a2d599cdd3522c2752e35fe8c4f56"
		},
		{
		  "categories": {
			"1": 365,
			"2": 199,
			"3": 11,
			"4": 0,
			"5": 0
		  },
		  "points": 575,
		  "name": "Maria Gabriela Toledo",
		  "picture": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xtf1/v/t1.0-1/p200x200/11217160_905132349575659_3468586391287738770_n.jpg?oh=2b1029d649a1c35ba9defa29790e0d13&oe=57DFFCB3&__gda__=1477230790_9b36ceaed6ce79e0432eafb58e8f6cf3"
		},
		 {
		  "categories": {
			"1": 365,
			"2": 198,
			"3": 11,
			"4": 0,
			"5": 0
		  },
		  "points": 575,
		  "name": "Maria Julia Godoy",
		  "picture" : "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xtf1/v/t1.0-1/p200x200/11217160_905132349575659_3468586391287738770_n.jpg?oh=2b1029d649a1c35ba9defa29790e0d13&oe=57DFFCB3&__gda__=1477230790_9b36ceaed6ce79e0432eafb58e8f6cf3"
		},
		 {
		  "categories": {
			"1": 365,
			"2": 197,
			"3": 11,
			"4": 0,
			"5": 0
		  },
		  "points": 574,
		  "name": "Ruy Barbosa de Brito",
		  "picture": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpt1/v/t1.0-1/p200x200/13165943_1433381956687402_454362039857567441_n.jpg?oh=b50040588863a35540a3d3ba588f2648&oe=57C2C1C3&__gda__=1472645566_814a2d599cdd3522c2752e35fe8c4f56"
		}
	  ]
	}"""

	answer = json.loads(mock_answer)
	return JsonResponse(answer)