from rest_framework import serializers
from .models import Course, Lesson
from users.serializers import UserSerializer
from .validators import validate_no_external_links

class LessonSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    video_url = serializers.URLField(allow_blank=True, required=False, validators=[validate_no_external_links])
    class Meta:
        model = Lesson
        fields = ('id','course','title','description','preview','video_url','owner')

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ('id','title','preview','description','price','lessons_count','lessons','owner','is_subscribed','updated_at')
    def get_lessons_count(self, obj):
        return obj.lessons.count()
    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request or not request.user or not request.user.is_authenticated:
            return False
        return obj.subscriptions.filter(user=request.user).exists()
