from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from .models import Recipient, Message, Mailing, Attempt
from .forms import RecipientForm, MessageForm, MailingForm
from .services import send_mailing_now

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['mailings_count'] = Mailing.objects.count()
        ctx['active_mailings'] = Mailing.objects.filter(status='started').count()
        ctx['recipients_count'] = Recipient.objects.count()
        return ctx

class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = 'mailings/recipient_list.html'
    def get_queryset(self):
        return Recipient.objects.filter(owner=self.request.user)

class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailings/recipient_form.html'
    success_url = reverse_lazy('mailings:recipient_list')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RecipientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailings/recipient_form.html'
    success_url = reverse_lazy('mailings:recipient_list')
    def test_func(self):
        return self.get_object().owner == self.request.user

class RecipientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipient
    template_name = 'mailings/recipient_confirm_delete.html'
    success_url = reverse_lazy('mailings:recipient_list')
    def test_func(self):
        return self.get_object().owner == self.request.user

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mailings/message_list.html'
    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('mailings:message_list')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('mailings:message_list')
    def test_func(self):
        return self.get_object().owner == self.request.user

class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    template_name = 'mailings/message_confirm_delete.html'
    success_url = reverse_lazy('mailings:message_list')
    def test_func(self):
        return self.get_object().owner == self.request.user

class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailings/mailing_list.html'
    def get_queryset(self):
        if self.request.user.is_staff:
            return Mailing.objects.all()
        return Mailing.objects.filter(owner=self.request.user)

class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailings:mailing_list')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MailingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailings:mailing_list')
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.is_staff

class MailingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mailing
    template_name = 'mailings/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailings:mailing_list')
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.is_staff

class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailings/mailing_detail.html'

class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    template_name = 'mailings/attempt_list.html'
    def get_queryset(self):
        if self.request.user.is_staff:
            return Attempt.objects.all()
        return Attempt.objects.filter(mailing__owner=self.request.user)

from django.views import View
class SendMailingNowView(LoginRequiredMixin, View):
    def post(self, request, pk):
        mailing = Mailing.objects.get(pk=pk)
        send_mailing_now(mailing)
        return redirect('mailings:mailing_detail', pk=pk)
