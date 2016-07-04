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
        fields = ('question', 'answer', 'is_correct', 'date')

class BadgeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Badge
		fields = ('name', 'description')