from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        
    @abstractmethod
    def login(self):
        pass


class Customer(User):
    def __init__(self, id, name, email, phone):
        super().__init__(id, name, email, phone)
        self.orders = []

    def login(self):
        print(self.name, "logged in")

    def placeorder(self, order):
        self.orders.append(order)


class RestaurantOwner(User):
    def login(self):
        print(self.name, "logged in")

    def managerestaurant(self):
        print(self.name, "is manager")


class DeliveryPartner(User):
    def __init__(self, id, name, email, phone, partnerId, vehicle):
        super().__init__(id, name, email, phone)
        self.partnerId = partnerId
        self.vehicle = vehicle
        self.availabilityStatus = True
        self.currentOrder = None

    def login(self):
        print(self.name, "logged in")

    def acceptorder(self, order):
        self.currentOrder = order
        self.availabilityStatus = False
        order.setstatus("OUT_FOR_DELIVERY")

    def deliverorder(self):
        self.currentOrder.setstatus("DELIVERED")
        self.currentOrder = None
        self.availabilityStatus = True


class Admin(User):
    def login(self):
        print(self.name, "logged in")

    def managesystem(self):
        print(self.name, "is admin")
        
       
owner = RestaurantOwner(1,"Raj","raj@gmail.com","9876543210")
customer = Customer(2,"Rahul","rahul@gmail.com","9876543211")
admin = Admin(3,"Admin","admin@gmail.com","9876543212")



class FoodItem:
    def __init__(self, itemId, name, price, category, isAvailable=True):
        self.itemId = itemId
        self.name = name
        self.price = price
        self.category = category
        self.isAvailable = isAvailable

    def updateprice(self, price):
        self.price = price


class Restaurant:
    def __init__(self, restaurantId, name, location, owner):
        self.restaurantId = restaurantId
        self.name = name
        self.location = location
        self.menu = []
        self.owner = owner

    def addfooditem(self, item):
        self.menu.append(item)

    def removefooditem(self, itemId):
        for item in self.menu:
            if item.itemId == itemId:
                self.menu.remove(item)

    def updateprice(self, itemId, price):
        for item in self.menu:
            if item.itemId == itemId:
                item.updateprice(price)

    def displaymenu(self):
        for item in self.menu:
            print(item.name, ":" + str(item.price))


class Order:
    def __init__(self, orderId, customer, restaurant):
        self.orderId = orderId
        self.customer = customer
        self.restaurant = restaurant
        self.items = []
        self.__orderStatus = "PLACED"
        self.__totalAmount = 0
        self.itemTotal = 0
        self.deliveryCharge = 0
        self.tax = 0
        self.discount = 0

    def additem(self, item, quantity):
        self.items.append([item, quantity])

    def calculateitemtotal(self):
        self.itemTotal = 0

        for item, quantity in self.items:
            self.itemTotal += item.price * quantity

        return self.itemTotal

    def calculatetotal(self, discount, deliveryCharge):
        self.calculateitemtotal()

        self.discount = discount.calculatediscount(self.itemTotal)

        self.deliveryCharge = deliveryCharge

        self.tax = (self.itemTotal - self.discount) * 0.05

        self.__totalAmount = (
            self.itemTotal
            + self.deliveryCharge
            + self.tax
            - self.discount
        )

    def getstatus(self):
        return self.__orderStatus

    def setstatus(self, status):
        self.__orderStatus = status

    def gettotalamount(self):
        return self.__totalAmount


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print("processed")
        return True

    def refund(self, amount):
        print("UPI payment refunded")


class CreditCard(Payment):
    def pay(self, amount):
        print("processed")
        return True

    def refund(self, amount):
        print("Credit card payment refunded")


class CashOnDelivery(Payment):
    def pay(self, amount):
        print("pending")
        return True

    def refund(self, amount):
        print("Cash payment cancelled")


class Discount(ABC):
    @abstractmethod
    def calculatediscount(self, amount):
        pass


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculatediscount(self, amount):
        return amount * self.percentage / 100


class FlatDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def calculatediscount(self, amount):
        return min(self.amount, amount)


class NoDiscount(Discount):
    def calculatediscount(self, amount):
        return 0


class Notification:
    def send(self, customer, message):
        print("Notification:", message)




pizza = FoodItem(101,"Pizza",400,"Main Course")
burger = FoodItem(102,"Burger",200,"Main Course")
coke = FoodItem(103,"Coke",80,"Drinks")

restaurant = Restaurant(501,"Pizza Den","Hyd",owner)
restaurant.addfooditem(pizza)
restaurant.addfooditem(burger)
restaurant.addfooditem(coke)

customer.login()

restaurant.displaymenu()
order = Order(1001,customer,restaurant)

order.additem(pizza, 1)
order.additem(burger, 1)
order.additem(coke, 1)

customer.placeorder(order)
discount = FlatDiscount(100)

order.calculatetotal(discount,50)


payment = UPI()
paymentStatus = payment.pay(order.gettotalamount())
order.setstatus("CONFIRMED")

notification = Notification()

notification.send(customer,"Your order #1001 has been confirmed")

order.setstatus("PREPARING")

notification.send(customer,"Your order #1001 is being prepared")

delivery = DeliveryPartner(10,"Arjun","arjun@gmail.com","9876543213",1001,"Bike")
delivery.acceptorder(order)
notification.send(customer,"Your order #1001 is out for delivery")

delivery.deliverorder()
notification.send(customer,"Your order #1001 has been delivered")



print("Customer:", customer.name)
print("Restaurant:", restaurant.name)
print("Order:", order.orderId)
print("Items:")
for item, quantity in order.items:
    print(item.name,":" + str(item.price),":",quantity)

print("Item Total:", ":" + str(order.itemTotal))
print("Discount:", ":" + str(order.discount))
print("Delivery:", ":" + str(order.deliveryCharge))
print("Tax:", ":" + str(order.tax))
print("Tot Amount:", ":" + str(order.gettotalamount()))
print("Status:", order.getstatus())
print("Delivery Partner:", delivery.name)
print("Vehicle:", delivery.vehicle)