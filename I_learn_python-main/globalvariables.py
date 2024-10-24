#variable outside a function is called a global variable
x = "Jeevan"
print ("There is a student named ",x)

#Now lets create a function and initiate a value to x inside function 
def myfunc():
    x = "Yoshi"
    print("That student used to have a friend nick-named", x)
myfunc()

#The value of x in the function is used only for the print variable of x inside a function

#Now lets create another function
y = "Benz"

#now lets create function actually here
def my_func():
    y = "Porsche"
    print("I Love Driving This", y)
    print("This", y, "is so comfortable")

#now lets change the global variables inside a function

def my__func():
    global y
    y = "BMW"
    print("I like a guy", x, "who drives", y)
# calling the modified function
my_func()
my__func()
