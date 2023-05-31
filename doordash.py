# Team 11
# Hamburger Door Dash
# Fielding Demars, Parker Anderson, Mary Anna Mendez, McKenna Alder, Jesus Martinez, Bakhyt Zhekey

import random
# create an order class that picks the random amount of burgers between 1 and 20
class Order:
    def __init__(self, burger_count):
        self.burger_count = Order.random_burgers(burger_count)
    def random_burgers(self):
        return random.randint(1,20)

# create a person class that calls a customer name from the selected list
class Person:
    def __init__(self, customer_name):
        self.customer_name = Person.randomName(customer_name)


    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return str(random.choice(asCustomers))
   
# create a customer class that inherits the parent of the Person class and set it to the order object
class Customer(Person):
    def __init__(self, customer_name, order):
        super().__init__(customer_name)
        self.order = Order(order)

# initialize the list for the queue
# initialize the dictionary to be able to look up the customers on the burger count
Queue = []
Customer_dict = {}

# making a for loop to add 100 customers to the queue
for i in range(0, 101):
    currentCustomer = Customer('', 0)
    Queue.append(currentCustomer)

	# if customer is not in the dictionary, add them to the dictionary with their burger count. If they ARE in the dictionary, add burger count
    if Queue[i].customer_name in Customer_dict:
        Customer_dict[Queue[i].customer_name] += Queue[i].order.burger_count
    else:
        Customer_dict[Queue[i].customer_name] = Queue[i].order.burger_count

# use this to sort the customers in the dictionary by creating a new list. Makes the list of most number of burgers to least number of burgers.          
sorted_customers = sorted(Customer_dict.items(), key=lambda x: x[1], reverse=True)

# print customer name with the burger count with the justified spacing given to us
for i in sorted_customers:
    print(i[0].ljust(19), i[1])
