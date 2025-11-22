from rest_framework.serializers import ValidationError


def validate_mutual_reward_and_linked(habit):
    if habit.get("reward") and habit.get("linked_habit"):
        raise ValidationError("Нельзя указывать и вознаграждение, и связанную привычку.")


def validate_pleasant_linked(habit):
    linked = habit.get("linked_habit")
    if linked and not linked.is_pleasant:
        raise ValidationError("Связанной может быть только приятная привычка.")


def validate_pleasant_cannot_have_reward_or_linked(habit):
    if habit.get("is_pleasant") and (habit.get("reward") or habit.get("linked_habit")):
        raise ValidationError("Приятная привычка не может иметь связанной привычки или награды.")


def validate_duration_limit(habit):
    if habit.get("duration") and habit.get("duration") > 120:
        raise ValidationError("Время выполнения не должно превышать 120 секунд.")


def validate_period(habit):
    if habit.get("period") and habit.get("period") > 7:
        raise ValidationError("Периодичность не может быть больше 7 дней.")
