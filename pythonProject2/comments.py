# types of datatype
#1. string
# it stores texts
v1 = "sam"
print(v1)
print(type(v1))

#2. int
# it stores whole numbers
v1 = 12
print(v1)
print(type(v1))

#3. float
# it stores numbers with decimal
v1 = 1.2
print(v1)
print(type(v1))

#4. complex
# it stores numbers as well as letters
v1 = 12+78j
print(v1)
print(type(v1))

#4. boolean
# it gives truth expressions
v1 = 12
v2 = 15
v3 = v1 + v2
print(v3)
if v3 > 10:
    print(True)
else:
    print(False)

#5. list
# it stores a series of values in a single variable
# the values can be added or deleted, changeable and allow duplicate values
v1 = [1,2,3,4]
print(v1)
print(type(v1))

# 6. set
# it stores a series of value
# set items are unchangeable but we can remove or add new items
# it does not allow duplicate values
v1 = {1,2,2,3,3,4}
print(v1)
print(type(v1))

#7. tuple
# it is a collection which is ordered and unchangeable
v1 = (1,2,3,4,4)
print(v1)
print(type(v1))
print(len(v1)) # shows the number of items in a tuple

#8. array
# stores multiple values in a single variable
from array import array
v1 = array('i',[1,2,3,4])
print(v1)
print(type(v1))

#9. dict
# it stores data value in keys
# it is ordered, changeable and do not allow duplicate
thisdict = {
    "brand" :"ford",
    "year": "2019",
    "model":"mustang"
}
print(thisdict)
print(type(thisdict))
v2 = {'id':2, 'name':'sam'}
print(v2.keys())
print(v2.values())
print(type(v2))
print(v2['name'])

#operators
#relational operators
# it gives results in boolean form that is either true or false
#1. greater than
v1 = 3
v2 = 6
print(v1==v2)

#2. equals to
v1 = 12
v2 = 12
print(v1==v2)

#assignment operators
# used to assign values to a variable
v1 = 3
v1+= 2
print(v1)

#logical operators
# combine conditional statements
#and
#returns true if both are true
v1 = 3
print(v1>1 and v1>2)
#or
# returns true if one statement is true
v1 = 12
print(v1>14 or v1>11)
#not
# reverse the reult
v1 = 12
print(not(v1 >2 and v1 > 10))

#syntax
#grammar
#rules that define the structure of a language
#semantics
#logic
# the way that data and commands are represented

#nested if
num1 =1
num2= 6
num3 = 5
 if num1>num2:
     if num1>num3:
         print(num1)