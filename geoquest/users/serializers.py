from rest_framework import serializers

from .models import *
from geoquest.questions.serializers import *
from django.contrib.auth.models import User

class RankSerializer(serializers.ModelSerializer):
	name = serializers.StringRelatedField(source='user.get_full_name')
	picture = serializers.SerializerMethodField()

	class Meta:
		model = Rank
		fields = ('points', 'name', 'picture')

	def get_picture(self, obj):
		return self.context[obj.social_account.uid]

class CategoryPointsSerializer(serializers.ModelSerializer):

	category = serializers.StringRelatedField()

	class Meta:
		model = CategoryPoints
		fields = ('completed', 'points', 'category')

class UserStatsSerializer(serializers.ModelSerializer):

	categories = CategoryPointsSerializer(many = True)
	best_category = serializers.StringRelatedField()
	user = serializers.StringRelatedField(source='user.get_full_name')

	class Meta:
		model = UserStatistics
		fields = ('categories', 'best_category', 'user', 'completed', 'position', 'last_updated')


class BadgeSerializer(serializers.ModelSerializer):

	name = serializers.StringRelatedField(source='user.get_full_name')
	percentage = serializers.FloatField(source='completed')
	picture = serializers.SerializerMethodField()
	area = serializers.StringRelatedField(source='best_category.name')
	badges = BadgeSerializer(many = True)

	def get_picture(self, obj):
		return self.context

	class Meta:
		model = UserStatistics
		fields = ('name', 'percentage', 'picture', 'area', 'badges')

class ProgressSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserStatistics
		fields = ('completed',)