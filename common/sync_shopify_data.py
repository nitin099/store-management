import django
import os
import requests
import sys
import argparse

from datetime import datetime as dt
from django.conf import settings


sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stores.settings")

django.setup()

from customers.models import Customer, Address
from orders.models import Order


def convert_to_date(input_data):
    """
    Converts input_data (datetime with offset) to date object.
    """
    return dt.strptime(input_data.split('T')[0], '%Y-%m-%d')


def date_formatter(start_date, end_date=None):
    """
    Date formatter for the date comparision.
    """
    if start_date and end_date:
        start_date = dt.strptime(start_date, '%Y-%m-%d')
        end_date = dt.strptime(end_date, '%Y-%m-%d')
        return start_date, end_date
    elif start_date:
        start_date = dt.strptime(start_date, '%Y-%m-%d')
        return start_date, None
    else:
        return None, None


def clean_data(customers=None, orders=None):
    """
    Clears the data from Customer and Order table.
    """
    if customers:
        Customer.objects.all().delete()

    if orders:
        Order.objects.all().delete()


def insert_bulk_data(customer_objects=None,
                     order_objects=None):
    """
    Takes customer or order objects and bulk inserts in db.
    """
    if customer_objects:
        resp = Customer.objects.bulk_create(customer_objects)
        print(len(resp), 'Customers inserted.')
    else:
        resp = Order.objects.bulk_create(order_objects)
        print(len(resp), 'Orders inserted.')
    return resp


def filter_data(resp, start_date, end_date):
    """
    Filters the data based on start/end dates
    prior to import and sync to db.
    """

    if start_date and end_date:
        resp = list(filter(lambda x: convert_to_date(
            x['created_at']) > start_date and convert_to_date(
            x['created_at']) < end_date, resp))
        return resp
    elif start_date:
        resp = list(filter(lambda x: convert_to_date(
            x['created_at']) > start_date, resp))
        return resp
    else:
        return resp


def get_customers_data():
    """
    Return all the customers data from Shopify.
    """
    url = f'{settings.STORE_URL}/customers.json'
    resp = requests.get(url).json()['customers']
    return resp


def save_customer_data(start_date=None, end_date=None, clean=False):
    """
    Creates all the customer instances prior to bulk insert.
    """
    customers_data = get_customers_data()
    customers_data = filter_data(customers_data, start_date, end_date)
    if clean:
        clean_data(customers=True)
    customer_objs = [Customer(customer_id=customer['id'],
                              first_name=customer['first_name'],
                              last_name=customer['last_name'],
                              email=customer['email'],
                              phone=customer['phone'],
                              currency=customer['currency'],
                              created_at=customer['created_at'],
                              updated_at=customer['updated_at']
                              )
                     for customer in customers_data]
    insert_bulk_data(customer_objects=customer_objs)


def get_orders_data(start_date=None, end_date=None):
    """
    Return all the orders data from Shopify.
    """
    url = f'{settings.STORE_URL}/orders.json'
    resp = requests.get(url).json()['orders']
    return resp


def save_order_data(start_date=None, end_date=None, clean=False):
    """
    Creates all the order instances prior to bulk insert.
    """
    order_data = get_orders_data(start_date)
    order_data = filter_data(order_data, start_date, end_date)
    if clean:
        clean_data(orders=True)

    order_objs = [Order(order_id=order['id'],
                        name=order['name'],
                        number=order['number'],
                        email=order['email'],
                        total_price=order['total_price'],
                        confirmed=order['confirmed'],
                        fulfillment_status=order['fulfillment_status'],
                        order_status_url=order['order_status_url'],
                        phone=order['phone'],
                        cancelled_at=order['cancelled_at']
                        )
                  for order in order_data]
    insert_bulk_data(order_objects=order_objs)


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("start_date", help="Start date for the records",
                            type=str, nargs='?')
        parser.add_argument("end_date", help="End date for the records",
                            type=str, nargs='?')
        parser.add_argument("clean", help="Clean and insert data",
                            type=str, nargs='?')

        args = parser.parse_args()
        start_date, end_date = date_formatter(args.start_date, args.end_date)
        if args.clean:
            clean = True

        if start_date and end_date:
            if start_date > end_date:
                print('Invalid date (start date is greater than end date)')
                sys.exit(0)
            save_order_data(start_date, end_date, clean=clean)
            save_customer_data(start_date, end_date, clean=clean)
        elif start_date:
            save_order_data(start_date, clean=clean)
            save_customer_data(start_date, clean=clean)
        else:
            save_order_data()
            save_customer_data()

    except Exception as e:
        print(str(e))
