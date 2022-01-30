import stripe
from django.shortcuts import render
from django.conf import settings # new
from django.views.generic.base import TemplateView

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY # new

class HomePageView(TemplateView):
    template_name = 'app/home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context



def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'app/charge.html')