from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from common.utils import COUNTRIES, CURRENCY_CODES
from orders.models import Order


class Customer(models.Model):
    customer_id = models.IntegerField()
    first_name = models.CharField(_('First name'), max_length=128, blank=True, null=True)
    last_name = models.CharField(_('Last name'), max_length=128, blank=True, null=True)
    email = models.EmailField(_('Email address'), unique=True, max_length=256)
    phone = models.CharField(_('Phone number'), max_length=64, blank=True, null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    synced_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.email}-{self.customer_id}'

    @property
    def total_spent(self):
        """
        Returns amount total spent by a customer.
        """
        total_sum = Order.objects.filter(
            email=self.email).aggregate(
            Sum('total_price')
        ).get('total_price__sum')
        return round(total_sum, 4) if total_sum else 0

    @property
    def orders_count(self):
        """
        Return order count for a customer.
        """
        return Order.objects.filter(email=self.email).count()

    @classmethod
    def get_customer(cls, email):
        """
        Returns the customer instance.
        """
        return cls.objects.get(email=email)

    @classmethod
    def update_customer(cls, customer_data):
        """
        Update the customer data.
        """
        customer_instance = cls.get_customer(customer_data['email'])
        for field_name, values in customer_data:
            setattr(customer_instance, field_name, values)
        customer_instance.save()
        return customer_instance

    def as_dict(self):
        """
        Consolidates the customer and address received from the form.
        """
        dict_data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'orders_count': self.orders_count,
            'currency': self.currency,
        }
        address_instance = Address.objects.filter(customer=self).first()
        if address_instance:
            dict_data.update({'address': address_instance.address,
                              'city': address_instance.city,
                              'country': address_instance.city,
                              'zip_code': address_instance.zip_code
                              })
        return dict_data


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(_("Address"), max_length=256, blank=True, null=True)
    city = models.CharField(_("City"), max_length=256, blank=True, null=True)
    state = models.CharField(_("State"), max_length=256, blank=True, null=True)
    zip_code = models.CharField(_("Post/Zip-code"), max_length=64, blank=True, null=True)
    country = models.CharField(max_length=3, choices=COUNTRIES, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Address'

    @classmethod
    def update_address(cls, address_data):
        """
        Updates the address data in db.
        """
        address_instance = cls.objects.get(email=address_data['customer']['email'])
        address_data = address_data.get('addresses')
        for field_name, values in address_data:
            setattr(address_instance, field_name, values)
        address_instance.save()
        return address_instance.save()
