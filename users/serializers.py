from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Payment
User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('id','email','password','phone','city','avatar')
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','phone','city','avatar')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id','user','paid_at','course','lesson','amount','method')
        read_only_fields = ('paid_at',)
