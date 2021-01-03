from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.db.models import Q

from .forms import CustomerForm
from .forms import CustomerUpdateForm
from .models import Customer


class CustomerFormView(FormView):

    form_class = CustomerForm
    template_name = 'customers/customer_form.html'

    def form_valid(self, form):
        """
        Saves the customer data in Shopify and sync data in local db.
        """
        try:
            if form.is_valid():
                instance = form.save()
            return HttpResponse(f'{instance.email} saved!')
        except Exception as e:
            print(str(e))
            return HttpResponse("Some error occured!")


class CustomerListView(ListView):

    model = Customer
    paginate_by = 10

    def get_queryset(self):
        """
        Returns the list of all customers (recent first)
        and supports the searching.
        """
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(
                email__icontains=query) | Q(
                first_name__icontains=query) | Q(
                last_name__icontains=query)
            ).order_by('created_at')
        else:
            object_list = self.model.objects.all().order_by('-created_at')
        return object_list


class CustomerDetailView(DetailView):

    model = Customer


class CustomerUpdateFormView(FormView):

    form_class = CustomerUpdateForm
    template_name = 'customers/customer_form.html'

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        customer = get_object_or_404(Customer, **self.kwargs)
        initial = customer.as_dict()
        return initial

    def form_valid(self, form):
        """
        Updates the customer data in Shopify and in local db.
        """
        try:
            if form.is_valid():
                instance = form.save()
            return HttpResponse(f'{instance.email} updated!')
        except Exception as e:
            print(str(e))
            return HttpResponse("Some error occured!")
