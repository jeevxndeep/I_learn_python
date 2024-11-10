# Creating a list
list1 = ["Ruthvik", "Premdeep", "Jeevan", "Abhiram"]
print (list1)

#list allows duplications
#can consist of different datatypes like strings, integers and boolean value
list2 = ["Bmw", 10000000, "black color", "Bmw", "True"]

#list is changeable after creation
list1 = ["Ruthvik", "Premdeep", "Jeevan", "Abhiram", "Sandeep"]
print (list1)

#can know the type of the list
print(type(list1))

#can find the length of the list
print(len(list1), len(list2))

#to change the list into tuple which is immutable type of list
print(list((list1)))
#now no changes can be done to list1

# to access the items in the list
print(list1[1])

#negative indexing in list
print(list1[-1])

#ranges of index
#type 1
print(list1[1:4])

#type 2
print(list1[:4])

#type 3
print(list[1:])

#type 4
print(list1[-4:-1])

#checking if items existing in the list or not

if "Ruthvik" in list1:
    print("yes, 'Ruthvik' is present in this list1.")
else:
    print("No, there is no such string in the tuple")

# to access list items
thislist = ["apple", "banana", "Grape", "mango", "Guava", "avacado"]
print(thislist[1])

#negative indexing
print(thislist[-1])

#ranges of the index in lists
thislist [1:3] = ["blackcurrent", "watermelon"]
print (thislist)
#changes the value of banana and grape and replace with the given values

thislist [1:2] = ["blackberry", "Cantaloop"]
print (thislist)
#only the second value is replaced with 2 other values

thislist [1:3] = ["watermelon"]
print (thislist)
#replacing the second and third value with one single value

#now using insert function which helps to insert values without replacing the old values. for this we use insert() function
thislist.insert(2, "pineapple")
print(thislist)

"""insert items in a list
to insert items in a list we can use insert as shown in the above method.
now we use append function and keyword is .extend()
this extend() keyword helps to add even tuples, list, sets, dictionaries and etc to a existing list.
"""
seasonal = ["lichee", "sapota", "papaya"]
thislist.extend(seasonal)
print (thislist)

# now lets use .append() to insert a single element at the end of the list
thislist.append("applebear")
print (thislist)

#lets learn removal of elements 

#removing a specific item we use remove() when  items are repeated then it removes the first occured value
thislist.remove("mango")
print (thislist)

#removing specific indec
thislist.pop(1)
print(thislist)
#if we dont specify index number then it will automatically remove the last value from the list.

#clearing the list
thislist.clear()
print (thislist)
#helps in clearing elements from the list without deleting the list

#deleting the list
del thislist