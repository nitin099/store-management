from django.db import models
# from customers.models import Customer
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE,
                                 blank=True, null=True)
    name = models.CharField(_('Name'), max_length=128)
    email = models.EmailField(_('Email address'), max_length=256)
    order_id = models.IntegerField(_('Order id'), blank=True, null=True)
    fulfillment_status = models.CharField(_('Fulfillment status'), max_length=128,
                                          blank=True, null=True)
    phone = models.CharField(_('Phone number'), max_length=20, blank=True, null=True)
    number = models.IntegerField(_('Order number'), blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    variant_id = models.IntegerField(blank=True, null=True)
    order_status_url = models.URLField(_('Order status'), blank=True, null=True)
    confirmed = models.BooleanField(_('Confirmed'), blank=True, null=True)
    total_price = models.FloatField(_('Price'), blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.order_id} _ {self.email}'

    @classmethod
    def save_order(cls, **kwargs):
        email = kwargs.get('email')
        customer_instance = Customer.objects.get(email=email)
        kwargs['customer'] = customer_instance
        return cls.objects.create(**kwargs)
