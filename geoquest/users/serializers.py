from rest_framework import serializers

from .models import *

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank