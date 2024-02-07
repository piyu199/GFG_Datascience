import math
import random
import datetime
import collections
from collections import defaultdict,OrderedDict

x=10.8
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print("-"*30)
y=8
print(math.exp(y))
print(math.log10(y))
print("-"*30)
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
print("-"*30)
print(math.factorial(5))

print("-"*10+"Random number"+"-"*10)
print(random.randrange(1,20))
print(random.random()) #between 0.0 to 1.0
print(random.randint(1,20))
print(random.choice([1,2,3,4,5,6]))
print(random.sample([1,2,3,4,5,6],2))
print(random.uniform(1.0,3.0))

print("-"*10+"Datetime"+"-"*10)
print(datetime.datetime.now().strftime("%Y-%m-%d"))
print(datetime.datetime(2023,10,28,10,30,0))
date_1=datetime.datetime(2023,11,28)
date_2=datetime.datetime(2023,10,28)
difference_between_two_datetime=date_1-date_2
print(difference_between_two_datetime)

print("-"*10+"Collections"+"-"*10)


list1=[1,2,3,1,1,1,3,4,5,6]
print(collections.Counter(list1))

#We have a ordered Dictionary in collection
ordered_dict=OrderedDict()
ordered_dict["one"]=1
ordered_dict["two"]=2
ordered_dict["three"]=3
print(ordered_dict)

#we can create a default dictionary
d = defaultdict(int)
d["a"] += 1
print(d)

print("-"*10+"strings"+"-"*10)
import string
str="Prajesh 1234 waghela"
str2="1234"
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
