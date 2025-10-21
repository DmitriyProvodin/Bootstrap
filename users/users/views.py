from rest_framework import generics, permissions
from .models import User, Payment
from .serializers import UserProfileSerializer, PaymentModelSerializer

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

class PaymentListView(generics.ListCreateAPIView):
    serializer_class = PaymentModelSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Payment.objects.select_related('user','course','lesson').all()
        course_id = self.request.query_params.get('course')
        lesson_id = self.request.query_params.get('lesson')
        method = self.request.query_params.get('method')
        ordering = self.request.query_params.get('ordering')
        if course_id:
            qs = qs.filter(course__id=course_id)
        if lesson_id:
            qs = qs.filter(lesson__id=lesson_id)
        if method:
            qs = qs.filter(method=method)
        if ordering:
            qs = qs.order_by(ordering)
        else:
            qs = qs.order_by('-paid_at')
        return qs

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        from django.shortcuts import get_object_or_404
        user = get_object_or_404(User, pk=user_id)
        course = None
        lesson = None
        course_id = self.request.data.get('course')
        lesson_id = self.request.data.get('lesson')
        if course_id:
            from courses.models import Course
            course = get_object_or_404(Course, pk=course_id)
        if lesson_id:
            from courses.models import Lesson
            lesson = get_object_or_404(Lesson, pk=lesson_id)
        Payment.objects.create(user=user, course=course, lesson=lesson, amount=self.request.data.get('amount'), method=self.request.data.get('method'))
