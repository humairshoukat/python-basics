# Python Programming
# Humair Shoukat (BSCS - NUML)

# Python-Fundamentals
# Operators, Variables, Data Types, Strings, Precedence, Loops, List. Tuples, Dictionary, Classes, Formatting

# Variables in Python
x = 'Hello World!'
my_age = 20

print(x)
print(my_age)

# Check type of a variable  
print(type(my_age))
print(type(x))
my_age = 20.0
print(type(my_age))

my_age = 1.0 + -0.5j
print(type(my_age))
print(my_age.real)
print(my_age.imag)

# Use the 'is' check to see if the type of a variable matches what we are comparing with
print(type(my_age) is bool)
print(type(my_age) is complex)

# Type Cating in Python
age = 19.5
print(type(age))

age = int(age)
print(age)
print(type(age))

age = "19.5"
# Can't do age + 10
# Solution: Typcast to float then calculate
age = float(age)
age += 10
print(age)

# Can't do this
# age = "a19.5"
# age = float(age)

# Arithmetics & Comparisons in Python
print(5+2)
print(5-2)
print(5*10)
print(5/2)
print(5//2)
print(5**2)

print(8>9)
print(12>10 and 11>10)
a = 10
print(a==10)

# Lists only have same values
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
print(list1 == list2)
print(list1 is list2)

# Lists have same value, and also refer to the same list
list1 = [1,2,3,4,5]
list2 = list1
print(list1 == list2)
print(list1 is list2)


# Strings in Python
# -----------------
var = "Hello World!"

# Find length of the variable (number of characters)
length = len(var)
print(length)

# Replace a particular word with another, in the string
var = var.replace("World", "Dunyia")
print(var)

print(var[0])
print(var[1])
print(var[2])
print(var[3])
print(var[4])

# Extract the word "Hello"
temp = var[0:5]
print(temp)

# Extract the word "World!"
temp = var[6:]
print(temp)

# Take the Even Position Occurences of the string
temp = var[::2]
print(temp)

# Printing
print(var, "\n")
print(var, "We're at NUST!\n")
print(var, 20, False, "\n")

age = 20
print(var+"We're at NUST!\n")
print(var+" my age is: " + str(age) + "\n")

first_name = "Humair"
last_name = "Shoukat"
full_name = first_name + " " + last_name
print(full_name)

# Lists in Python
list1 = [1,2,3,4,5]
print(list1)

#List Slicing (Same as string slicing)
print(list1[2:5])
print(list1[::2])

list2 = [1, "1", "one", 1.0]
print(list2)

list3 = [1,[2], [3,4,5],[[6,7], [8,9]]]
print(list3[3])

#Converting a string into a list of characters
word = "Hello World"
print(list(word))

#Using the .append(val) function to add to the end
list4 = []
list4.append("A")
list4.append("B")
print(list4)

#Using the .insert(index,val) to insert at a particular index
list4.insert(1,"C")
print(list4)

#Delete Values

#1) Delete Particular Index
del list4[0]
print(list4)

#2) Delete First Occurence of a Particular Value
list4.remove("C")
print(list4)

list5 = [4,9,1,2,8,7,3]
list5.sort()
print(list5)
list5.sort(reverse=True)
print(list5)

# Tuples in Python
#immutable, used for unpacking
coord = (5,10)
x, y= coord
print("X: ", x)
print("Y: ", y)

# Dictionaries in Python
dic={ "Pakistan" : 40, 
      "India"    : 145, 
      "China"    : 500, 
      "Mexico"   : "None"
    }
print(dic)

print(dic["Pakistan"])
dic["Pakistan"] = 38
print(dic)

#Print the Key and Value Pair
for i, j in dic.items():
    print(i, " : ", j)

#Add a new key value pair
dic["Turkey"] = 90
print(dic)

#remove an exisiting Key Value Pair
dic.pop("Mexico")
print(dic)

#Nested Dictionary
Family = {
    
        "child1" : {
            "name":"Humair", 
            "age":22
        }, 
    
        "child2" : {
            "name":"Ali", 
            "age": 19
        }
}

print("Family: ", Family)

# Statements in Python

