from django.urls import path
from . import views

app_name = "manage_store_module"

urlpatterns = [
    path('webhook/', views.create_webhook, name='create_webhook'),
    path('webhook/orders/', views.order_webhook, name='orders_webhook'),
]
