from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Habit
        fields = ['id','owner','place','time','action','is_rewarding','related','periodicity_days','reward','duration_seconds','is_public','created_at']
