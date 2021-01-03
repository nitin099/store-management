from django.urls import path
from . import views

app_name = "customers_module"

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('create/', views.CustomerFormView.as_view(), name='customer_form'),
    path('update/<int:pk>/', views.CustomerUpdateFormView.as_view(), name='customer_update'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
]
