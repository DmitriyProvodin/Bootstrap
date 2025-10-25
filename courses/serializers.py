from rest_framework import serializers
from .models import Course, Lesson
from users.serializers import UserSerializer

class LessonSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = ('id','course','title','description','preview','video_url','owner')

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ('id','title','preview','description','lessons_count','lessons','owner')
    def get_lessons_count(self, obj):
        return obj.lessons.count()
