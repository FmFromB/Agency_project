from django.shortcuts import render
from .models import *
from django.views.generic import *
from .forms import OfferForm

class OffersListView(ListView):
    model = Offer
    template_name = 'offers.html'
    context_object_name = 'offers'

class OffersDetailView(DetailView):
    model = Offer
    template_name = 'detail.html'
    context_object_name = 'get_offer'

def add_offer(request):

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()

    template = 'add_offer.html'
    context = {
        'list_offers': Offer.objects.all().order_by('-id'),
        'form': OfferForm()
    }
    return render(request, template, context)