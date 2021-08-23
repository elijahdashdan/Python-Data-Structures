
##### 1
items = {"item1": "test","item2": "test2"}

for key,value in items.items():
    print(key, value)


##### 2
import json

books = {}
books["book1"] = {
    "title" :"hey",
    "pages" : 23
}

books["book2"] = {
    "title": "hey2",
    "pages": 24
}
s = json.dumps(books)

print(s)
#### 3
print(books["book1"]["title"])

#### 4
# f = open("")
# s= f.read()
#json.loads(s
# 

#### 5
# __name__ #entry point where you run the python code

#### 6

# Class -> Properties -> Methods
# Object is instance of class

class Human:
    def __init__(self,name,occupation):
        self.name = name #properties
        self.occupation = occupation #properties
    
    def do_work(self): #Methods
        if self.occupation == "tennis player":
            print(self.name, " plays tennis")
        elif self.occupation == "actor":
            print(self.name, " shoots a film")
    
    def speaks(self):
        print(self.name, " how are you")

tom = Human("tom", "actor") #Objects, instance of Class
tom.do_work()
tom.speaks()

### 7

class Vehicle:
    def general(self):
        print("general use")

class Car(Vehicle): #Inheritance
    def __init__(self):
        print("Im car")
        self.wheels = 4
        self.has_roof = True
    
    def specific(self):
        print("commute to work")

class Motorcycle(Vehicle):
    def __init__(self):
        print("Im Motor")
        self.wheels = 2
        self.has_roof = False
    
    def specific(self):
        print("leisure")

c = Car()
c.general()
c.specific()

#### 8
# isinstance
# issubclass

#### 9

class Father():
    def skills(self):
        print("gardening")


class Mother():
    def skills(self):
        print("cooking")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c = Child()
c.skills()

#### 10

class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def handle(self):
        print("user", self.msg)

try:
    raise Accident("Crash")
except Accident as e:
    e.handle()

#### 11

# def process():

#     try: 
#         f= open("")
#         x=1/0
#     except FileNotFoundError as e:
#         print(e)
#     finally:
#         f.close()


### ITERATOR
### GENERATOR is better

def remote():
    yield "a"
    yield "b"

itr = remote()
next(itr)
next(itr)

def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b
    
for f in fib():
    if f>13:
        break
    print(f)

###  14

num = [1,2,3] #LIST COMPREHENSION

sqr = [i*i for i in num]
print(sqr)

### 15
s = set([1,2,3,4,5,2,3]) #SET COMPREHENSION
print(s)

even ={i for i in s if i%2==0}
print(even)

### 16
cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]

z = zip(cities, countries)# returns tuple
d = {city:country for city, country in zip(cities,countries)}
print(d)

### 17
x = {"a","b","c"}
y = {"c","d","e"}

z = x.symmetric_difference(y) # present in both
# Check other methods

### 18
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number 1", help="first no.")
    parser.add_argument("number 2", help="first no.")
    parser.add_argument("--operation", help="operation", choices=["add", "subtract"]) #optional

    args= parser.parse_args()

    print(args.number1)

### 19
# Decorators
# https://www.youtube.com/watch?v=IVWZxr0kOyI&list=PLeo1K3hjS3uv5U-Lmlnucd7gqF-3ehIh0&index=28