grade = int(input("Enter your marks : " ))


if grade > 90 and grade <= 100:
        print("Your Grade is A")
elif grade > 80 and grade <= 90:
        print("Your Grade is B")
elif grade > 70 and grade <= 80 :
        print("Your Grade is C")
else:
        print("You are Failed")


# reverse a string 
str1 = "Abhishek"
reversed_str = str1[::-1]
print("Reversed:", reversed_str)


# check palindrome
str1 = "Abhishek"
reversed_str = str1[::-1]
print(str1 == reversed_str)

# fibonicci series 
def fibonacci(n):
        fib_series = [0,1]
        for i in range (2,n):
                fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series[:n]


print(fibonacci(10))

# even or odd

a = int(input("Enter the number :"))

if a%2 == 0:
        print("Even")
else:
        print("Odd")


# prime number
b = int(input("Enter the number to check prime or not"))
def isprime(b):
    for i in range(2,b):
        if b%i == 0:
                return False
    return True    

print(isprime(b))

# print @ at even 

for i in range(1,100):
       if i % 2 == 0:
              print("@")
       else:
              print(i)

# retrive values from dictionary
data = {
    "name": "Abhishek",
    "age": 24,
    "city": "Mumbai",
    "profession": "Software Engineer"
}

# Display available keys
print("Available keys:", list(data.keys()))

# Get user input for the key
key = input("Enter a key to retrieve its value: ")

# Display the corresponding value
if key in data:
    print(f"The value for '{key}' is: {data[key]}")
else:
    print("Key not found in dictionary.")

# collection iteration 
col = [1,2,4,5]

for i in range(0,len(col)):
       col[i] = col[i]*col[i]
print(col)

# get and display function

def get_details():
    details = {}
    details["name"] = input("Enter your name: ")
    details["age"] = int(input("Enter your age: "))
    details["city"] = input("Enter your city: ")
    details["profession"] = input("Enter your profession: ")
    return details

def display_details(details):
    print("\nUser Details:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

user_details = get_details()
display_details(user_details)