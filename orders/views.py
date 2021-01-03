from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import OrderForm
from .models import Order
from common.shopify_requests import ShopifyAPI

class OrderFormView(FormView):

    form_class = OrderForm
    template_name = 'orders/order_form.html'

    def form_valid(self, form):
        """
        Creates the order data in Shopify and sync data in local db.
        """
        try:
            data = form.cleaned_data
            shopify = ShopifyAPI()
            response = shopify.create_order(**data)
            data['order_id'] = response['order']['id']
            order_instance = Order()
            order_instance.save_order(**data)
            return HttpResponse("Success!")
        except Exception as e:
            print(str(e))
            return HttpResponse("Some error occured!")


class OrderListView(ListView):

    model = Order
    paginate_by = 10

    def get_queryset(self):
        """
        Returns the list of all orders (recent first)
        and supports the searching.
        """
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                email__icontains=query
            ).order_by('created_at')
        else:
            object_list = self.model.objects.all().order_by('-created_at')
        return object_list


class OrderDetailView(DetailView):

    model = Order
    context_object_name = 'order'
