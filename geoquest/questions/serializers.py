from rest_framework import serializers

from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    a = serializers.StringRelatedField(source='option_a')
    b = serializers.StringRelatedField(source='option_b')
    c = serializers.StringRelatedField(source='option_c')
    d = serializers.StringRelatedField(source='option_d')
    e = serializers.StringRelatedField(source='option_e')

    class Meta:
        model = Question
        fields = ('category', 'question', 'points', 'a', 'b', 'c', 'd', 'e', 'correct_answer', 'level')

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