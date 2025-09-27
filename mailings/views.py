from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        from .models import Mailing, Recipient
        context = super().get_context_data(**kwargs)
        context['mailings_count'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(status='started').count()
        context['recipients_count'] = Recipient.objects.count()
        return context
