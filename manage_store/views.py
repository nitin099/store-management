import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import WebhookForm
from orders.models import Order
from common.shopify_requests import ShopifyAPI
from common.utils import process_webhook_order_data


def home(request):
    """
    View for home page.
    """
    return render(request, 'home.html', {})


def create_webhook(request):
    """
    View for creating webhook for customers, orders, etc.
    """
    form = WebhookForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        shopify = ShopifyAPI()
        shopify.create_webhook(**data)
        return HttpResponse("Webhook created")
    context = {'form': form}
    return render(request, 'manage_store/webhook.html', context)


@csrf_exempt
def customer_webhook(request):
    """
    Syncs the incoming order data from shopify to Order model.
    """
    if not request.body:
        return
    order_data = process_webhook_order_data(
        json.loads(request.body))
    order_instance = Order()
    order_instance.save_order(**order_data)
