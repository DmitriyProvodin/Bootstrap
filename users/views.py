from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegisterForm, UserUpdateForm

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

class ProfileView(TemplateView):
    template_name = 'users/profile.html'

class ProfileEditView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile')
    def get_object(self):
        return self.request.user
