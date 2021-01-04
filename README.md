# Store Management

An application for storing, processing and reviewing orders that belong to those customers.



## Features

* Create, retrieve or update for **Customers** and **Orders** using Shopify API.

* Get and Search Customers based on name or email to retrieve their details like total orders, total spent, etc.

* Get and Search Order related details.

* Sync (**all** or with **start/end** date) the customers and orders data from Shopify store to local db.

* Add *Webhook* url specifying the topic like **order/create** or **update** etc, and sync the in real time in db.


  

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv venv
$ source venv/bin/activate
$ git clone <git-repo-url>
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Create an .env one directory up the root of the project i.e *manage.py* to store Environment variables.

```
SHOPIFY_API_KEY=<shopify_api_key>
SHOPIFY_API_PASSWORD=<shopify_api_password>
DOMAIN=<myshop>.myshopify.com/admin/api/2020-10
```



## To import the customers and orders from Shopify store.

#### Import all the data

```
$ cd common
$ python sync_shopify_data.py
```

#### Import data with in a date range

`$ python sync_shopify_data.py <start_date> <end_date>`

````
$ python sync_shopify_data.py 2020-12-01 2021-01-01
````



## Final step

```
$ python manage.py runserver
```

- Open web browser and goto `127.0.0.1:8000`.
- Goto Customers to retrieve, search all the customers, update customer details.
- Goto Orders to retrieve, search all the orders.
- Enable saving customer data from Shopify providing url `<host>/manage_store/webhook/orders/`.

## Contributing

Feel free to fix bugs, improve things, provide documentation. Just send a pull request.
