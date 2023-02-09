from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from main.models import Item
from environment_variables import STRIPE_SECRET_KEY
import stripe

stripe.api_key = STRIPE_SECRET_KEY


class HomeView(ListView):
    model = Item
    template_name = 'main.html'
    context_object_name = 'items'


class DetailItemView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'


def buy(request, pk):
    item = Item.objects.get(pk=pk)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'rub',
                    'unit_amount': item.price * 100,
                    'product_data': {
                        'name': item.name
                    }
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/',
        cancel_url='http://127.0.0.1:8000/',
    )

    return JsonResponse({
        'id': checkout_session.id
    })


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
