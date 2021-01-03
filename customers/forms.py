from django import forms
from common.shopify_requests import ShopifyAPI
from common.utils import COUNTRIES, CURRENCY_CODES, format_data
from .models import Address, Customer


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    address = forms.CharField(required=False)
    city = forms.CharField(required=False)
    zip_code = forms.CharField(required=False)
    currency = forms.ChoiceField(choices=CURRENCY_CODES, required=False)
    country = forms.ChoiceField(choices=COUNTRIES, required=False)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        shopify = ShopifyAPI()
        cleaned_data = format_data(self.cleaned_data)
        response = shopify.create_customer(**cleaned_data)
        customer_id = response['customer']['id']
        customer = super(CustomerForm, self).save(commit=False)
        customer.customer_id = customer_id
        customer.created_at = response['customer']['created_at']
        customer.updated_at = response['customer']['updated_at']
        customer.save()
        self.cleaned_data['customer'] = customer
        address_form = AddressForm(self.cleaned_data)
        address_form.is_valid()
        address_form.save()
        return customer


class CustomerUpdateForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(disabled=True)
    address = forms.CharField(required=False)
    city = forms.CharField(required=False)
    zip_code = forms.CharField(required=False)
    currency = forms.ChoiceField(choices=CURRENCY_CODES, required=False)
    country = forms.ChoiceField(choices=COUNTRIES, required=False)

    def save(self, commit=True):
        shopify = ShopifyAPI()
        cleaned_data = format_data(self.cleaned_data)
        Address.update_address(cleaned_data)
        customer_instance = Customer.update_customer(cleaned_data['customer'])
        cleaned_data['customer']['id'] = customer_instance.customer_id
        shopify.update_customer(**cleaned_data['customer'])
        return customer_instance
