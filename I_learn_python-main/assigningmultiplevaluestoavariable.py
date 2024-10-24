#Assigning Multiple Values to Variables
#1. Many values to multiple variables

x, y, z = "Orange", "Banana", "Cherry"
print (x, y, z)

#2. One value to multiple variables

x = y = z = "Orange"
print(x, y, z)

#3.unpack collection

fruits = ["Orange", "Banana", "Cherry"]
x,y,z = fruits
print(x, y, z)