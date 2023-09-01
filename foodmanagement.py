import datetime

# Create a list to store customers and delivery orders
customers = []
delivery_orders = []

# Customer class to represent customer information
class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

# DeliveryOrder class to represent delivery orders
class DeliveryOrder:
    def __init__(self, order_id, customer, delivery_address, delivery_date, status="Pending"):
        self.order_id = order_id
        self.customer = customer
        self.delivery_address = delivery_address
        self.delivery_date = delivery_date
        self.status = status

# Function to add a customer
def add_customer():
    print("Add Customer:")
    name = input("Customer Name: ")
    address = input("Customer Address: ")
    phone = input("Customer Phone: ")

    customer = Customer(name, address, phone)
    customers.append(customer)
    print("Customer added successfully!\n")

# Function to add a delivery order
def add_delivery_order():
    print("Add Delivery Order:")
    order_id = input("Order ID: ")
    customer_name = input("Customer Name: ")

    # Check if the customer exists
    customer = next((c for c in customers if c.name == customer_name), None)

    if customer is None:
        print("Customer not found. Please add the customer first.")
        return

    delivery_address = input("Delivery Address: ")
    delivery_date = input("Delivery Date (YYYY-MM-DD): ")

    try:
        delivery_date = datetime.datetime.strptime(delivery_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    order = DeliveryOrder(order_id, customer, delivery_address, delivery_date)
    delivery_orders.append(order)
    print("Delivery order added successfully!\n")

# Function to view customers
def view_customers():
    if not customers:
        print("No customers found.\n")
        return

    print("Customers:")
    for index, customer in enumerate(customers, start=1):
        print(f"Customer {index}:")
        print(f"Name: {customer.name}")
        print(f"Address: {customer.address}")
        print(f"Phone: {customer.phone}")
        print()

# Function to view delivery orders
def view_delivery_orders():
    if not delivery_orders:
        print("No delivery orders found.\n")
        return

    print("Delivery Orders:")
    for index, order in enumerate(delivery_orders, start=1):
        print(f"Order {index}:")
        print(f"Order ID: {order.order_id}")
        print(f"Customer: {order.customer.name}")
        print(f"Delivery Address: {order.delivery_address}")
        print(f"Delivery Date: {order.delivery_date.strftime('%Y-%m-%d')}")
        print(f"Status: {order.status}")
        print()

# Function to update delivery order status
def update_delivery_status(order_id):
    for order in delivery_orders:
        if order.order_id == order_id:
            new_status = input(f"Update status for Order {order_id} (Delivered/In Transit/Cancelled): ")
            if new_status.lower() in ['delivered', 'in transit', 'cancelled']:
                order.status = new_status.capitalize()
                print(f"Order {order_id} status updated successfully!\n")
                return
    print(f"Order {order_id} not found.\n")

# Main program loop
while True:
    print("Delivery Management System")
    print("1. Add Customer")
    print("2. Add Delivery Order")
    print("3. View Customers")
    print("4. View Delivery Orders")
    print("5. Update Delivery Status")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_customer()
    elif choice == '2':
        add_delivery_order()
    elif choice == '3':
        view_customers()
    elif choice == '4':
        view_delivery_orders()
    elif choice == '5':
        order_id = input("Enter the Order ID to update status: ")
        update_delivery_status(order_id)
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
