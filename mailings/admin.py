from django.contrib import admin
from .models import Recipient, Message, Mailing, Attempt

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('id','email','full_name','owner')
    search_fields = ('email','full_name')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','subject','owner')
    search_fields = ('subject',)

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id','status','start_time','end_time','owner')
    list_filter = ('status',)
    search_fields = ('message__subject',)

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id','mailing','status','attempt_time')
    list_filter = ('status',)
