from rest_framework import serializers

from .models import *

class RankSerializer(serializers.ModelSerializer):
	name = serializers.StringRelatedField(source='user.get_full_name')
	picture = serializers.SerializerMethodField()

	class Meta:
		model = Rank
		fields = ('points', 'name', 'picture')

	def get_picture(self, obj):
		return self.context[obj.social_account.uid]