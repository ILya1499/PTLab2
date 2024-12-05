from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from datetime import datetime

from .models import Product, Purchase, Promocode

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)

class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')

class PromocodeGet(CreateView):
    model = Promocode
    fields = ['number']

    def form_valid(self, form):
        href = '<div><a href="/">Вернуться к списку товаров</a></div>'
        num = form.cleaned_data['number']
        if(Promocode.objects.filter(number=num).count()==0):
            return HttpResponse('Промокод отсутствует. ' + href)
        else:    
            obj = Promocode.objects.get(number=num)
            if(obj.date_end > datetime.today()):
                self.request.session['promo'] = obj.pk
                return HttpResponse('Промокод применён. '+ href)
            else:
                return HttpResponse('Промокод не действителен. ' + href)
