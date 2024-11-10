#we use .sort() keyword to sort alphanumerically, ascending by default 
#here we used the case insensitive sorting where strings starting with capital letters gets sorted then followed by the small letters words
thislist=["Orange", "mango", "Kiwi", "pineapple" , "banana"]
thislist.sort()
print(thislist)

#lets sort numbers now
numbers = [100, 10 ,50,69, 29, 6]
numbers.sort()
print(numbers)

#sort decending for this we use the function reverse = True
numbers.sort(reverse=True)
print(numbers)
#the same applies to lists containing strings

"""
Customize sort function:
you can customize your own function by using the keyword arguement key = function
"""

def myfunc(n):
    return abs(n-50)
number = [100, 50, 65, 82, 23]
number.sort(key=myfunc)
print(number)

#copy methods in python
oldfruits = ["mango", "apple","Grapes"]
newfruits = oldfruits.copy()
print(newfruits)

#method 2
newfruits = list(oldfruits)
print(newfruits)

#using slicing operator
newfruits = oldfruits[:]
print(newfruits)

#joining lists using operators

list1=["a","b","c","d"]
list2 = [1, 2, 3, 4, 5]
list3 = list1 + list2
print (list3)

#method2 using append() to join lists
for x in list2:
    list1.append(x)
print(list1)

#or if we ever wanted to add the list in the last of other list we can directly use the extend() function
list1.extend(list2)
print(list1)

"""all builtin methods for list in python are
1. append()
2. sort()
3. clear()
4. copy()
5. count()
6. extend()
7. index()
8. insert()
9. pop()
10. remove()
11. reverse()"""