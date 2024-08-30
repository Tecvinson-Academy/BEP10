import os
import json
import random

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email
        }

class Order:
    def __init__(self, order_id, product, customer, quantity):
        self.order_id = order_id
        self.product = product
        self.customer = customer
        self.quantity = quantity

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'product_id': self.product.product_id,
            'customer_id': self.customer.customer_id,
            'quantity': self.quantity
        }

class Store:
    def __init__(self):
        self.products = {}
        self.customers = {}
        self.orders = {}
        self.customer_id_counter = 1
        self.order_id_counter = 1

        self.load_data()

    def generate_product_id(self):
        random_number = random.randint(1000, 9999)
        return f"BEP10-{random_number}"

    def save_data(self):
        with open('products.txt', 'w') as f:
            for product in self.products.values():
                f.write(json.dumps(product.to_dict()) + '\n')

        with open('customers.txt', 'w') as f:
            for customer in self.customers.values():
                f.write(json.dumps(customer.to_dict()) + '\n')

        with open('orders.txt', 'w') as f:
            for order in self.orders.values():
                f.write(json.dumps(order.to_dict()) + '\n')

    def load_data(self):
        if os.path.exists('products.txt'):
            with open('products.txt', 'r') as f:
                for line in f:
                    data = json.loads(line.strip())
                    product = Product(data['product_id'], data['name'], data['price'], data['stock'])
                    self.products[product.product_id] = product

        if os.path.exists('customers.txt'):
            with open('customers.txt', 'r') as f:
                for line in f:
                    data = json.loads(line.strip())
                    customer = Customer(data['customer_id'], data['name'], data['email'])
                    self.customers[customer.customer_id] = customer

        if os.path.exists('orders.txt'):
            with open('orders.txt', 'r') as f:
                for line in f:
                    data = json.loads(line.strip())
                    product = self.products.get(data['product_id'])
                    customer = self.customers.get(data['customer_id'])
                    if product and customer:
                        order = Order(data['order_id'], product, customer, data['quantity'])
                        self.orders[order.order_id] = order

    def add_product(self, name, price, stock):
        product_id = self.generate_product_id()
        product = Product(product_id, name, price, stock)
        self.products[product_id] = product
        self.save_data()
        return product

    def list_products(self):
        return list(self.products.values())

    def add_customer(self, name, email):
        customer = Customer(self.customer_id_counter, name, email)
        self.customers[self.customer_id_counter] = customer
        self.customer_id_counter += 1
        self.save_data()
        return customer

    def list_customers(self):
        return list(self.customers.values())

    def place_order(self, product_id, customer_id, quantity):
        product = self.products.get(product_id)
        customer = self.customers.get(customer_id)

        if not product or not customer:
            return None

        if product.stock < quantity:
            return None

        order = Order(self.order_id_counter, product, customer, quantity)
        self.orders[self.order_id_counter] = order
        self.order_id_counter += 1
        product.stock -= quantity
        self.save_data()
        return order

    def list_orders(self):
        return list(self.orders.values())
