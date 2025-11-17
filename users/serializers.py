from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id','email','password','telegram_chat_id')
    def create(self, validated_data):
        pwd = validated_data.pop('password')
        u = User(**validated_data)
        u.set_password(pwd)
        u.save()
        return u
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','telegram_chat_id')
