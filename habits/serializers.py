from rest_framework import serializers
from .models import Habit
from .validators import (
    validate_mutual_reward_and_linked,
    validate_pleasant_linked,
    validate_pleasant_cannot_have_reward_or_linked,
    validate_duration_limit,
    validate_period
)


class HabitSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = "__all__"

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        if not user.is_authenticated:
            return False
        return obj.user == user

    def validate(self, attrs):
        validate_mutual_reward_and_linked(attrs)
        validate_pleasant_linked(attrs)
        validate_pleasant_cannot_have_reward_or_linked(attrs)
        validate_duration_limit(attrs)
        validate_period(attrs)
        return attrs
