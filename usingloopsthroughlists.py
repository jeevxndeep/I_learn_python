thislist = ["BMW", "Porsche", "Toyota"]
for x in thislist:
    print(x) #this is looping through list

thislist1 = ["apple", "mango", "strawberry"]
for i in range (len(thislist1)):
    print(thislist1[i]) #looping through index

thislist2 = [1, 2, 3, 4, 5]
i = 0
while i < len(thislist2):
    print(thislist2[i]) #using while loop with lists
    i = i + 1

#we can also use shorthand for loop to print all the in the list
[print(x) for x in thislist2] #this is called list comprehension

#using conditions

newlist= [x for x in thislist2 if x < 3]
print (newlist)

#lets create a list using range function
newlist2 = [x for x in range(10)]
print(newlist2)

newlist3 = [x for x in newlist2 if x < 6]
print (newlist3)

#changing everything into capitals
newlist4 = [x.upper() for x in thislist]
print (newlist4)

#changing all the variables into cars 
newlist5 = ["cars" for x in thislist]
print(newlist5)

#replacing porsche with nissan
newlist6 = [x if x!="Porsche" else "nissan" for x in thislist]
print(newlist6)
