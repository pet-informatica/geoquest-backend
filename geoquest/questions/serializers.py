from rest_framework import serializers

from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer