# Hamburger Door Dash
# Fielding Demars, Parker Anderson, Mary Anna Mendez, McKenna Alder, Jesus Martinez, Bakhyt Zhekey

import random
#create an order class that picks the random amount of burgers between 1 and 20
class Order:
    def __init__(self):
        self.burger_count = self.random_burgers


    def random_burgers(self):
        return random.randint(1,20)
   
   
# create a person class that calls a customer name from the selected list
class Person:
    def __init__(self):
        self.customer_name = self.randomName()


    def randomName(self):
        asCustomers = [["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]]
        return random.choice(asCustomers)
   
   
#create a customer class that inherits the parent of person and set it to the order object
class Customer(Person):
    def __init__(self, customer_name):
        super().__init__(customer_name)
        self.order = Order()

Queue = []
Customer_dict = {}




for i in range(1, 101):
    currentCustomer = Customer('')
    Queue.append(currentCustomer)




    currentCustomerName = currentCustomer.customer_name
    if currentCustomerName in Customer_dict:
        Customer_dict[currentCustomerName] += currentCustomer.order.burger_count
    else:
        Customer_dict[currentCustomerName] = currentCustomer.order.burger_count
               
sorted_customers = sorted(Customer_dict.items(), key=lambda x: x[1], reverse=True)


for i in sorted_customers:
    print(i[0].ljust(19), i[1])


