from models import Store

def print_menu():
    print("\n1. Add Product")
    print("2. List Products")
    print("3. Add Customer")
    print("4. List Customers")
    print("5. Place Order")
    print("6. List Orders")
    print("7. Exit")

def main():
    store = Store()

    while True:
        print_menu()
        choice = input("\nEnter choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            product = store.add_product(name, price, stock)
            print(f"Product added: {product.name}, Price: {product.price}, Stock: {product.stock}")

        elif choice == '2':
            products = store.list_products()
            print("\nProduct List:")
            for product in products:
                print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Stock: {product.stock}")

        elif choice == '3':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            customer = store.add_customer(name, email)
            print(f"Customer added: {customer.name}, Email: {customer.email}")

        elif choice == '4':
            customers = store.list_customers()
            print("\nCustomer List:")
            for customer in customers:
                print(f"ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}")

        elif choice == '5':
            product_id = int(input("Enter product ID: "))
            customer_id = int(input("Enter customer ID: "))
            quantity = int(input("Enter quantity: "))
            order = store.place_order(product_id, customer_id, quantity)
            if order:
                print(f"Order placed: Product: {order.product.name}, Customer: {order.customer.name}, Quantity: {order.quantity}")
            else:
                print("Order could not be placed. Check product stock or IDs.")

        elif choice == '6':
            orders = store.list_orders()
            print("\nOrder List:")
            for order in orders:
                print(f"ID: {order.order_id}, Product: {order.product.name}, Customer: {order.customer.name}, Quantity: {order.quantity}")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
