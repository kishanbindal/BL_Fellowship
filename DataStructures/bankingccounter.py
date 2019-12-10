class Queue:

    def __init__(self):
        self.data = []

    # Insert item at the back of the queue (left most of the list)
    def enqueue(self, item):
        self.data.insert(0, item)

    # Remove item from the front of the queue (Right most element)
    def dequeue(self):
        return self.data.pop()

    # Check if the Queue is empty, return True if empty
    def is_empty(self):
        return len(self.data) == 0

    # return the number of elements in the Queue
    def size(self):
        return len(self.data)


class Person:

    def __init__(self, name, balance=500.0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Accout balance too low to withdraw {amount}")
            print(f"Balance = {self.balance}")
        else:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        return self.balance


def banking_counter():
    q = Queue()
    number_in_queue = int(input("Number of people in Queue?"))
    for i in range(1, number_in_queue+1):
        customer_name = input(f"Please Enter Customer {i}'s' Name : \n")
        customer_balance = float(input(f"Enter Customer {i}'s' Bank Balance : \n"))
        q.enqueue(Person(customer_name, customer_balance))
    while q.is_empty() is False:
        person = q.dequeue()
        print(f"\nHello {person.name}\n")
        while True:
            choice = int(input("\n1. Deposit\n2. Withdraw\n3.Check Balance\n4. Leave counter\n"))
            if choice == 1:
                amt = float(input("Enter Amount to Deposit : "))
                person.deposit(amt)
            elif choice == 2:
                amt = float(input("Enter Amount to withdraw : "))
                person.withdraw(amt)
            elif choice == 3:
                print(person.show_balance())
            else:
                print(f"Thank You {person.name}")
                break
