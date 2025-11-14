from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from .models import Course, Lesson, Subscription
from .serializers import CourseSerializer, LessonSerializer
from .paginators import StandardResultsSetPagination
from .tasks import send_course_update_emails

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name='moderators').exists():
            raise PermissionDenied('Moderators are not allowed to create courses.')
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        course = serializer.save()
        # enqueue sending emails to subscribers
        send_course_update_emails.delay(course.id)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='moderators').exists():
            return Course.objects.all()
        return Course.objects.filter(owner=user)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name='moderators').exists():
            raise PermissionDenied('Moderators are not allowed to create lessons.')
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='moderators').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)

class SubscriptionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        course_id = request.data.get('course')
        if not course_id:
            return Response({'detail': 'course id required'}, status=400)
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({'detail': 'course not found'}, status=404)
        subs = Subscription.objects.filter(user=user, course=course)
        if subs.exists():
            subs.delete()
            return Response({'message': 'subscription removed'})
        else:
            Subscription.objects.create(user=user, course=course)
            return Response({'message': 'subscription added'})
