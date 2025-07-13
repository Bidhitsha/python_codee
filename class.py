"""class Student:
    def data (self, name, age):
        self.name=name
        self.age= age
s1=Student()
s1.data("bidhitsha", 20)

print(s1.name)
print(s1.age)

class Student:
    def __init__(self,name,age):
        self.name =name
        self.age=age
s1=Student("Bidhitsha", 20)
print(s1.name)
print(s1.age)

class Point:
    def __init__(self,x):
        self.x=x
    def __add__ (self,other):
        return Point(self.x+other.x)

p1=Point(3)
p2=Point(4)
p3=p1+p2
print(p3.x)


class Animal:
    def speak(self):
        print("animal sound")
        
class Dog(Animal):
    def bark(self):
        print("Bark")
        
d=Dog()
print(d.speak())
print(d.bark())

class User:
    def __init__(self, role):
        self.role=role
def create_user(role):
    return User(role)

u=create_user("admin")
print(u.role)

class Singleton:
    _instance=None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance= super().__new__ (cls)
        return cls._instance
a=Singleton()
b=Singleton()

print(a is b)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          
        self.balance = balance      

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add money
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount  # Subtract money
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdraw amount must be positive!")

    def get_balance(self):
        return self.balance
    
account = BankAccount("Alice", 100)
account.deposit(50)  
account.withdraw(70)  
print("Current balance:", account.get_balance())"""

