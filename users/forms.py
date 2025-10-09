from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','avatar','phone','country')
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','avatar','phone','country')
