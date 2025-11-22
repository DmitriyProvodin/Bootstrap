import pytest
from rest_framework.exceptions import ValidationError
from habits.validators import (
    validate_reward_or_related,
    validate_duration,
)

@pytest.mark.parametrize(
    "reward, related_habit, should_raise",
    [
        ("конфета", None, False),
        (None, 1, False),
        ("конфета", 1, True),
    ]
)
def test_reward_or_related_validator(reward, related_habit, should_raise):
    if should_raise:
        with pytest.raises(ValidationError):
            validate_reward_or_related(reward, related_habit)
    else:
        validate_reward_or_related(reward, related_habit)


def test_duration_validator_success():
    assert validate_duration(100) is None


def test_duration_validator_fail():
    with pytest.raises(ValidationError):
        validate_duration(200)
