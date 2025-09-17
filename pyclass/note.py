# basics on py
"syntax"
x = 5
y = "Hello Me!"

# print(x)
# print(y)

x = str(3)  # x will be 3
y = int(6)  # y will be 6
z = float(9)  # z will be 9.0

# print(x)
# print(y)
# print(z)

# print(type(x))
# print(type(y))
# print(type(z))

def greet(name):
    return "Hello " + name 

greeting = greet ("Alice")
greet("Bob")     #because it's not assign to a variable 
# print(greeting)



def add(a, b):
    return a + b

result = add(5, 10)
# print(result)

    # print(add(result, 20)) #from the function called and when we asked for return, here the result is acting as an argument!

def computer(a, b):
    result = a * b
    if result > 18:        #sine this action is false, it moves to the next line 
        return result - 3
    return result + 4

# print(computer(3, 2))
# print(computer(5, 3))

# lambda functions are often used to create a short helper function 
# and the syntax is Lambda x(argument): x(expression); to use a lambda you have to call the keyword lambda 
# also called annonymous function because they don't have a name 


power = lambda num: num ** 2
# print(power(3))
 
def trans_lst(numbers, number):
    trans_0 = number(numbers[0])
    trans_1 = number(numbers[1])
    return [trans_0, trans_1]

total = trans_lst([4, 5], lambda num: num ** 2)

# print(total)

# filter only keeps items that meet a condition

num_lst = [2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda num: num % 2 == 0, num_lst))

# print(even)

numbers = [2, 3, 4, 5, 6, 7, 8]

Odd = list(filter(lambda num: num % 2 == 1, num_lst))

# print(Odd)

# map can take a list of any item and operate with it and accpet two parameters and has to be cast before printing

my_map = list(map(lambda num: num ** 2, numbers))

# print(my_map)

name = "Temi"
age = 25

# print("My name is", name, "and i am", age, "years old", sep=",")
# the end function help to over ride an output on a same line  
# print("Hello World", end=" " )
# print("Hello World\n")
# print("I am", name)

# help function allows to print out the documentation of a python function 
# help(print)


class Shoe:
    def myfunc(self, size):
        self.size = size
        print("My shoe size is", self.size, "\n")

    def myFunc(self, color):
        self.color = color
        print("and the color is ", self.color)

shoe_ = Shoe()

# shoe_.myfunc(40)
# shoe_.myFunc("lemon green")

class School:
    def __init__(self, Staff, Student):
        self.staff = Staff
        self.Stud = Student

    def myfunc(self):
        pass

# print("my name is you", end= " ")    
# print("You're me")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
# print(thisdict)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

# print(x)

# import introme as intro 

# intro.greeting("Fathia")
# intro.meeting("15:30")

# a = intro.person1["age"]
# print(a)

from introme import greeting
# print(greeting("Alice"))

x = min(5, 10, 25)
y = max(5, 10, 25)

# print(x)
# print(y)

x = abs(-7.25)

# print(x)
import math
x = math.trunc(-7.25)
y = math.floor(-7.25)
z = math.ceil(-7.25)
# print(x)
# print(y)
# print(z)

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
# y = json.loads(x)

# the result is a Python dictionary:
# print(y["age"])

y =  '{ "name":"John", "age":30, "city":"New York"}'

z = json.loads(y)
# print(z["name"])

i =  { "name":"John", "age":30, "city":"New York"}

j = json.dumps(i)

# print(json.dumps({"name": "John", "age": 30}))      #dict
# print(json.dumps(["apple", "bananas"]))             #list
# print(json.dumps(("apple", "bananas")))             #tuple
# print(json.dumps("hello"))                          #str
# print(json.dumps(42))                               #int
# print(json.dumps(31.76))                            #float
# print(json.dumps(True))                             #bool
# print(json.dumps(False))                            #bool
# print(json.dumps(None))                             #none


p = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


# print(json.dumps(p, indent=4, separators=(", ", " = ")))

# print(json.dumps(p, indent=2, separators=(" , ", ":")))

print(json.dumps(p, indent=2, sort_keys=True))


