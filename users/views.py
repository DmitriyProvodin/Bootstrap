from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserCreateSerializer, PaymentSerializer
from .models import Payment
from courses.models import Course

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('user','course','lesson').all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['course','lesson','method']
    ordering_fields = ['paid_at']
    ordering = ['-paid_at']
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Stripe integration: service is internal; if STRIPE_API_KEY not set - return mock
import stripe
stripe.api_key = settings.STRIPE_API_KEY

class StripePaymentCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        amount = getattr(course, 'price', None) or request.data.get('amount') or 0

        # If stripe key is missing - return mock response
        if not settings.STRIPE_API_KEY:
            session_id = f"mock_session_{course.id}"
            url = f"https://checkout.stripe.mock/session/{session_id}"
        else:
            # create stripe product/price/session
            product = stripe.Product.create(name=course.title)
            price = stripe.Price.create(unit_amount=int(float(amount) * 100), currency='usd', product=product.id)
            session = stripe.checkout.Session.create(payment_method_types=['card'], line_items=[{'price': price.id, 'quantity': 1}], mode='payment', success_url='https://example.com/success', cancel_url='https://example.com/cancel')
            session_id = session.id
            url = session.url

        payment = Payment.objects.create(user=request.user, course=course, amount=amount, method='transfer', stripe_session_id=session_id, stripe_payment_url=url)
        return Response({'payment_url': url, 'session_id': session_id}, status=status.HTTP_201_CREATED)

class StripePaymentStatusAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, session_id):
        if not settings.STRIPE_API_KEY:
            return Response({'status': 'mock_pending', 'session_id': session_id})
        session = stripe.checkout.Session.retrieve(session_id)
        return Response({'status': session.payment_status, 'session': session})
