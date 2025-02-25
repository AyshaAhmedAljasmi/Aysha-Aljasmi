from datetime import datetime
from enum import Enum
class User: #Represents the user in the system.
    def __init__(self, user_id, user_firstname, user_lastname, contact_information, recent_order_date=None):
        self._user_id = user_id
        self._user_firstname = user_firstname
        self._user_lastname = user_lastname
        self._contact_information = contact_information
        self._recent_order_date = recent_order_date
    def get_user_id(self):
        return self._user_id #Returns the users ID
    def set_user_id(self, user_id):
        self._user_id = user_id #Sets the users ID
    def get_first_name(self):
        return self._user_firstname #Returns the users first name
    def set_first_name(self, user_firstname):
        self._user_firstname = user_firstname #Sets users first name
    def get_last_name(self):
        return self._user_lastname #Returns the users last name
    def set_last_name(self, user_lastname):
        self._user_lastname = user_lastname #Sets users last name
    def get_contact_information(self):
        return self._contact_information #Returns the users contact information
    def set_contact_information(self, contact_information):
        self._contact_information = contact_information #Sets the users contact information
    def get_recent_order_date(self):
        return self._recent_order_date #Returns the recent order date of the user
    def set_recent_order_date(self, recent_order_date):
        self._recent_order_date = recent_order_date #Sets the recent order date of the user
    def place_order(self): #Places an order for the user
        pass  # Implementation to place an order
    def update_profile(self): #Updates the user's profile information
        pass  # Implementation to update the user's profile
    def display_user_info(self): #Display the user's information
        print(f"User ID: {self._user_id}")
        print(f"First Name: {self._user_firstname}")
        print(f"Last Name: {self._user_lastname}")
        print(f"Contact Information: {self._contact_information}")
        print(f"Recent Order Date: {self._recent_order_date}")

class Driver:# Represents the driver in the system.
    def __init__(self, driver_id, driver_firstname, driver_lastname, vehicle_type, nationality):
        self._driver_id = driver_id
        self._driver_firstname = driver_firstname
        self._driver_lastname = driver_lastname
        self._vehicle_type = vehicle_type
        self._nationality = nationality
    def get_driver_id(self): #Returns the driver ID
        return self._driver_id
    def set_driver_id(self, driver_id): #Sets the driver ID
        self._driver_id = driver_id
    def get_first_name(self):
        return self._driver_firstname #Returns the drivers first name
    def set_first_name(self, driver_firstname):
        self._driver_firstname = driver_firstname #Sets the drivers first name
    def get_last_name(self):
        return self._driver_lastname #Returns the drivers last name
    def set_last_name(self, driver_lastname):
        self._driver_lastname = driver_lastname #Sets the drivers last name
    def get_vehicle_type(self):
        return self._vehicle_type #Returns the vehicle type of the driver
    def set_vehicle_type(self, vehicle_type):
        self._vehicle_type = vehicle_type #Sets the vehicle type of the driver
    def get_nationality(self):
        return self._nationality #Returns the nationality of the driver
    def set_nationality(self, nationality):
        self._nationality = nationality #Sets the nationality of the driver
    def assign_delivery(self): #Assigns a delivery to the driver
        pass  # Implementation to assign a delivery
    def display_driver_info(self): #Displays the driver's information
        print(f"Driver ID: {self._driver_id}")
        print(f"First Name: {self._driver_firstname}")
        print(f"Last Name: {self._driver_lastname}")
        print(f"Vehicle Type: {self._vehicle_type}")
        print(f"Nationality: {self._nationality}")

class OrderStatus(Enum): #This would represent the status of an order
    PENDING = "Pending"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"
class Order: #Represents the order in the system.
    def __init__(self, order_id, order_date, amount_of_items, total_price, order_status=OrderStatus.PENDING):
        self._order_id = order_id
        self._order_date = order_date
        self._amount_of_items = amount_of_items
        self._total_price = total_price
        self._order_status = order_status
    def get_order_id(self):
        return self._order_id #Returns the order ID.
    def set_order_id(self, order_id):
        self._order_id = order_id #Sets the order ID
    def get_order_date(self):
        return self._order_date #Returns the order date
    def set_order_date(self, order_date):
        self._order_date = order_date #Sets the order date
    def get_amount_of_items(self):
        return self._amount_of_items #Returns the amount of items
    def set_order_id(self, amount_of_items):
        self._amount_of_items = amount_of_items #Sets the amount of items
    def get_total_price(self):
        return self._total_price #Returns the total price of the order
    def set_total_price(self, total_price):
        self._total_price = total_price #Sets the total price of the order
    def get_order_status(self):
        return self._order_status # Returns the order status
    def set_order_status(self, order_status):
        self._order_status = order_status #Sets the order status
    def add_order_item(self):
        pass  # Add an item to the order
    def calculate_total_price(self): #Calculates total price of the order
        pass  # Calculates the total price
    def display_order_info(self):
        """Displays the order's information."""
        print(f"Order ID: {self._order_id}")
        print(f"Order Date: {self._order_date}")
        print(f"Amount of Items: {self._amount_of_items}")
        print(f"Total Price:{self._total_price}")
        print(f"Order Status: {OrderStatus}")

class DeliveryStatus(Enum): #Represents the status of a delivery.
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    FAILED = "Failed"
class Delivery: #Represents the delivery in the system.
    def __init__(self, delivery_id, estimated_delivery_date, shipping_address, delivery_weight, delivery_status=DeliveryStatus.PENDING):
        self._delivery_id = delivery_id
        self._estimated_delivery_date = estimated_delivery_date
        self._shipping_address = shipping_address
        self._delivery_weight = delivery_weight
        self._delivery_status = delivery_status
    def get_delivery_id(self):
        return self._delivery_id #Returns the delivery ID
    def set_delivery_id(self, delivery_id):
        self._delivery_id = delivery_id #Sets the delivery ID
    def get_estimated_delivery_date(self):
        return self._estimated_delivery_date #Returns the estimated delivery date
    def set_estimated_delivery_date(self, estimated_delivery_date):
        self._estimated_delivery_date = estimated_delivery_date #Sets the estimated delivery date
    def get_shipping_address(self):
        return self._shipping_address #Returns the shipping address
    def set_shipping_address(self, shipping_address):
        self._shipping_address = shipping_address #Sets the shipping address
    def get_delivery_weight(self):
        return self._delivery_weight #Returns the delivery weight
    def set_delivery_weight(self, delivery_weight):
        self._delivery_weight = delivery_weight #Sets the delivery weight
    def get_delivery_status(self):
        return self._delivery_status #Returns the delivery status
    def set_delivery_status(self, delivery_status):
        self._delivery_status = delivery_status #Sets the delivery status
    def update_status(self): #Updates the delivery status
        pass  # Implementation to update the delivery status
    def update_delivery_status(self): #Updates the delivery status
        pass  # Implementation to update the delivery status
    def display_delivery_info(self): #Displays the delivery's information
        print(f"Delivery ID: {self._delivery_id}")
        print(f"Estimated Delivery Date: {self._estimated_delivery_date}")
        print(f"Shipping Address: {self._shipping_address}")
        print(f"Delivery Weight: {self._delivery_weight}")
        print(f"Delivery Status: {self._delivery_status.value}")  # Access the value of the Enum
#Test
# Creating for the class User
user1 = User(
    user_id=202317839,
    user_firstname="Sarah",
    user_lastname="Johnsom",
    contact_information="sarah.johnsom@example.com",
    recent_order_date=datetime(2025, 1, 11))
# Creating for the class Driver
driver1 = Driver(
    driver_id=201719609,
    driver_firstname="Mohamed",
    driver_lastname="Salem",
    vehicle_type="Car, mini cooper",
    nationality="Egyptian")
# Creating for the class Order
order1 = Order(
    order_id=1092,
    order_date=datetime.now(),
    amount_of_items=20,
    total_price=378.00,
    order_status=OrderStatus.PROCESSING)
# Create a Delivery
delivery1 = Delivery(
    delivery_id=2001,
    estimated_delivery_date=datetime(2025, 2, 25, 13, 0, 0),  #Feb. 25th,2025 at 1 PM
    shipping_address="45 Knowledge Avenue, UAE, Dubai",
    delivery_weight=7.25,
    delivery_status=DeliveryStatus.SHIPPED)
# Display the User Information
print("User Information:")
user1.display_user_info()
print("-" * 20)
# Display the Driver Information
print("Driver Information:")
driver1.display_driver_info()
print("-" * 20)
# Display the Order Information
print("Order Information:")
order1.display_order_info()
print("-" * 20)
# Display the Delivery Information
print("Delivery Information:")
delivery1.display_delivery_info()

