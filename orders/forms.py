from django import forms
from common.utils import FULFILLMENT_STATUS


class OrderForm(forms.Form):
    email = forms.EmailField()
    variant_id = forms.IntegerField()
    quantity = forms.IntegerField()
    fulfillment_status = forms.ChoiceField(choices=FULFILLMENT_STATUS,
                                           required=False)
