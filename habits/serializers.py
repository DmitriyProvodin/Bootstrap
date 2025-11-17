from rest_framework import serializers
from .models import Habit
class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user','last_performed')
    def validate(self, data):
        if data.get('reward') and data.get('related_habit'):
            raise serializers.ValidationError('Cannot set both reward and related_habit')
        if data.get('is_pleasant') and (data.get('reward') or data.get('related_habit')):
            raise serializers.ValidationError('Pleasant habit cannot have reward or related_habit')
        if data.get('duration_seconds',0) > 120:
            raise serializers.ValidationError('Duration cannot exceed 120 seconds')
        pd = data.get('periodicity_days',1)
        if pd <1 or pd>7:
            raise serializers.ValidationError('Periodicity must be between 1 and 7 days')
        return data
