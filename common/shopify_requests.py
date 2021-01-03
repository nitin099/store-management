import requests

from django.conf import settings


class ShopifyAPI:
    """
    Shopify API Client.
    This client provides access to shopify objects (orders, customers) in a generic
    way.
    You can read more about `Shopify API here
    <https://shopify.dev/docs/admin-api/rest/reference/>`_
    """

    def __init__(self):
        self.base_url = settings.STORE_URL
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def build_url(self, path, params=None):
        """
        Given a path construct the full URL.
        :param params: Should be a list of key value pairs or dictionary
        """
        url = f'{self.base_url}/{path}'
        return url

    def request(self, path, method='GET', body=None,
                params=None, **kwargs):
        """
        Makes a request and sends the response body back.
        """
        url = f'{self.base_url}/{path}'
        if method == 'GET':
            response = requests.get(url, headers=self.headers)
        elif method == 'POST':
            response = requests.post(url, json=body, headers=self.headers)
        elif method == 'UPDATE':
            response = requests.put(url, json=body, headers=self.headers)
        elif method == 'DELETE':
            response = requests.delete(url, headers=self.headers)

        # Raise an error if the response is not 2XX
        response.raise_for_status()

        return response.json()

    def get_all_customers(self, url, **kwargs):
        """
        Returns all the customres.
        """
        response = self.request('customers.json', method='GET')
        return response

    def create_customer(self, **kwargs):
        """
        Creates the a customer.
        """
        response = self.request('customers.json', body=kwargs, method='POST')
        return response

    def update_customer(self, **kwargs):
        """
        Updates the customer information.
        """
        customer_id = kwargs['customer']['id']
        path = f'customers/{customer_id}.json'
        response = self.request(path, method='UPDATE', body=kwargs)
        return response

    def get_orders(self, url):
        """
        Returns all the orders.
        """
        response = self.request('orders.json', headers=self.headers)
        return response

    def create_order(self, **kwargs):
        """
        Creates an order with given input data.
        """
        order_data = {
            'order':
            {
                'email': kwargs.get('email'),
                'line_items': [
                    {
                        'variant_id': kwargs.get('variant_id'),
                        'quantity': kwargs.get('quantity')
                    }
                ]
            }
        }
        if kwargs.get('fulfillment_status'):
            order_data['order']['fulfillment_status'] = kwargs.get('fulfillment_status')
        response = self.request('orders.json', body=order_data, method='POST')
        return response

    def create_webhook(self, **kwargs):
        """
        Creates a webhook in shopify with given topic.
        """
        response = self.request('webhooks.json', body=kwargs, method='POST')
        return response

    def delete_webhook(self, webhook_id):
        """
        Deletes the webhook.
        """
        response = self.request(f'webhooks/{webhook_id}.json', method='DELETE')
        return response
