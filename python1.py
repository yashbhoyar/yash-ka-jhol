#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.


item1='phone'
item1_price=50000
item1_qauntity=5

item1_total_price= item1_price * item1_qauntity


print(type(item1))
print(type(item1_price))
print(type(item1_qauntity))
print(type(item1_total_price))


#Here we have a item and its name , price , qauntity , total price . 
#We have diff variables of different data types to describe a single real world entity item .
#We can create a class called item which will have name , price , qaunity , total_price as member variables .
#Calculation item1_total_price as member func .
#Different items like phone ,earbuds will be the objects(instances).


random_str='abcd'           # string variable ie instance/object of a built in string class
print(random_str.upper())   # string variable method ie member function of a string class 

class String():
    def __init__(self,x):
        self.x=x

random_str1=String('abcs')  #creating a instance/object oa a String class
print(random_str1.x)        #printing  objects member variable 


#creating a class named Item

class Item :
    def calculate_total_price(self,x,y):
        return x*y

item1=Item()
item1.name="Phone"
item1.price=100
item1.qauntity=5 
print(item1.calculate_total_price(item1.price,item1.qauntity))

#here we have created a class and then its object , 
#but we dont have a set of rules for the attributes to pass in order to instantiate an instance 
'''for each item(object) it would be nice if we can call someone that will give values to an objects member variables /
and completes the procedure of instantiating an object'''

#to achieve this python have special method '__init__()' which is called as constructor 
'''Constructors are generally used for instantiating an object. 
The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. 
In Python the __init__() method is called the constructor and is always called when an object is created.'''

# Creating a class called Item with constructor.
class Items :
    def __init__(self,name,price,qauntity):
        self.name=name
        self.price=price
        self.qauntity=qauntity
        self.total_price=0

    def calc_total_price(self):
        self.total_price=self.price * self.qauntity 

phone=Items('iphone',50000,5)

print(type(phone))
print(phone.price)
print(phone.name)
print(phone.qauntity)
print(phone.total_price)
phone.calc_total_price()
print(phone.total_price)


#we can use assign 0 to any member variable , in that case we dont need to write that variable in parameter while creating an object
class Items :
    def __init__(self,name,price,qauntity=0):
        self.name=name
        self.price=price
        self.qauntity=qauntity          #we can either write it or not , value assigned will be the one written in parameteres
        self.total_price=0

    def calc_total_price(self):
        self.total_price=self.price * self.qauntity 

laptop=Items('laptop',50000)
print(laptop.qauntity)
laptop.qauntity=5
print(laptop.qauntity)


