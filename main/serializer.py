from rest_framework import serializers
from .models import BabyWeek

class BabyWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyWeek
        fields = ['week_number', 'image', 'average_weight', 'average_size']
