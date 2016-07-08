from django.shortcuts import render
from rest_framework.permissions import AllowAny
import random

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework import filters

from .models import Question, Category, Answer
from .serializers import QuestionSerializer, CategorySerializer, AnswerSerializer
from .filters import *

class QuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = QuestionFilter
    permission_classes = (AllowAny,)

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

class AnswerList(ListCreateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        user = self.request.user
        return Answer.objects.filter(user = user)

    def create(self, request, *args, **kwargs):
        user = request.user
        return Answer.objects.all()


class RandomQuestion(ListAPIView):
    
    """
        Returns a random question to the User
    """

    serializer_class = QuestionSerializer
    
    def get_queryset(self):

        #Filters
        category = self.request.GET.get('category',None)
        level = self.request.GET.get('level', None)

        #The user that is requesting the data
        user = self.request.user

        #If the user is not authenticated it will get no questions
        if user.is_anonymous():
            return {}

        #Getting the list of questions already answered by the requester
        answered_questions = Answer.objects.filter(user = user, is_correct = True).values('question')
        questions = None

        #Peforming the right query
        if category is None and level is None:
            questions = Question.objects.all().exclude(id__in = answered_questions)
        elif category is None:
            questions = Question.objects.filter(level = level).exclude(id__in = answered_questions)
        elif level is None:
            questions = Question.objects.filter(category = category).exclude(id__in = answered_questions)
        else:
            questions = Question.objects.filter(category = category, level = level).exclude(id__in = answered_questions)
        count = len(questions)


        if(count == 0):
            return {}

        position = random.randint(0, count-1)
        return [questions[position],]
