from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from .forms import UserRegisterForm, UserLoginForm

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            send_mail(
                'Добро пожаловать на MyShop',
                'Спасибо за регистрацию на MyShop. Рады видеть вас!',
                settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else None,
                [self.object.email],
                fail_silently=True,
            )
        except Exception:
            pass
        return response

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:home')
