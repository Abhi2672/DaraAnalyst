# 1. Single Inheritance
class Parent:
    def func1(self):
        print("This is Parent class")

class Child(Parent):
    def func2(self):
        print("This is Child class")

obj = Child()
obj.func1()  # Accessing parent class method
obj.func2()

# 2. Multiple Inheritance
class Parent1:
    def func1(self):
        print("This is Parent1 class")

class Parent2:
    def func2(self):
        print("This is Parent2 class")

class Child(Parent1, Parent2):
    def func3(self):
        print("This is Child class")

obj = Child()
obj.func1()
obj.func2()
obj.func3()

# 3. Multilevel Inheritance
class Grandparent:
    def func1(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def func2(self):
        print("This is Parent class")

class Child(Parent):
    def func3(self):
        print("This is Child class")

obj = Child()
obj.func1()
obj.func2()
obj.func3()

# 4. Hierarchical Inheritance
class Parent:
    def func1(self):
        print("This is Parent class")

class Child1(Parent):
    def func2(self):
        print("This is Child1 class")

class Child2(Parent):
    def func3(self):
        print("This is Child2 class")

obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()

# 5. Hybrid Inheritance (Combination of Multiple and Multilevel)
class Base:
    def func1(self):
        print("This is Base class")

class Derived1(Base):
    def func2(self):
        print("This is Derived1 class")

class Derived2(Base):
    def func3(self):
        print("This is Derived2 class")

class Hybrid(Derived1, Derived2):
    def func4(self):
        print("This is Hybrid class")

obj = Hybrid()
obj.func1()
obj.func2()
obj.func3()
obj.func4()



class MathOperations:
    def add(self, a, b=0, c=0):  
        return a + b + c

obj = MathOperations()
print(obj.add(5))       
print(obj.add(5, 10))   
print(obj.add(5, 10, 15)) 


class Parent:
    def show(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):  
        print("This is the Child class")

obj = Child()
obj.show()  

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          
        self._account_type = "Savings"  
        self.__balance = balance    

    def deposit(self, amount):  
        self.__balance += amount
        print(f"Deposited {amount}, New Balance: {self.__balance}")

    def get_balance(self):  
        return self.__balance


account = BankAccount("Alice", 5000)


print(account.owner)  


print(account._account_type)  



print(account.get_balance())  


account.deposit(1000)  

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):  # Overriding the parent method
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):  # Overriding the parent method
        print("Cat meows")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.make_sound()  # Calls the overridden method


class MathOperations:
    def add(self, a, b=0, c=0):  # Using default values
        return a + b + c

math_obj = MathOperations()
print(math_obj.add(5))        # Output: 5
print(math_obj.add(5, 10))    # Output: 15
print(math_obj.add(5, 10, 15)) # Output: 30

