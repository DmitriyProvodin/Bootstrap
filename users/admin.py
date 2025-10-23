from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Payment


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'email', 'is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'paid_at', 'amount', 'method')
    list_filter = ('method',)
    search_fields = ('user__email',)
