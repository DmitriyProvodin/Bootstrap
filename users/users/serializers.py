from rest_framework import serializers
from .models import User, Payment
from courses.serializers import CourseSerializer, LessonSerializer

class PaymentModelSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    lesson = LessonSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = ('id','user','paid_at','course','lesson','amount','method')

class UserProfileSerializer(serializers.ModelSerializer):
    payments = PaymentModelSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','email','phone','city','avatar','payments')
