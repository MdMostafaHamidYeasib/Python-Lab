"""
x="python is awesome"
print(x)
"""
"""
x = "python"
y = "is"
z = "awesome"
print (x,y,z)
"""
"""
x = 5
y =10
print(x+y)
"""
"""
x = 5
y = "yeasib"
print(x,y)
"""
"""
#global variable

x = "awesome"
def myfunc() :
    print("paython is " + x) 
myfunc()
"""
"""
#global & local variable
x = "awesome"
def myfunc() :
    x = "fantastic"
    print("paython is " + x) 
myfunc()
print("python is " +x)
"""
"""
#user input
name = input("Enter name:")
print("name is: " + name)
print(type(name))
"""
"""
#if...else
a=28
b=11
if a>b:
    print("a is greater than b")
"""
"""

a=28
b=111
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
"""

"""
a = 28
b = 28
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
"""

"""
#logical operation
a=28
b=11
c=2001
if a>b and c>a:
    print("both conditions are true")
"""
"""
a=28
b=11
c=2001
if a>b or c>a:
    print("one conditions are true")
"""
"""
#nested if
x=28
if x>10:
    print("Above ten ")
    if x>20:
        print ("and also above 20 ")
else:
    print("but not above 20 ")
"""
"""
#pass statement
a= 11
b=28
if b>a:
    pass
else:
    print("printing else")

print("without printing else") 
"""
"""
a= 2001
b=28
if b>a:
    pass
else:
    print("printing else")

print("without printing else")  
"""
"""
#match statement
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("This is Weekend")

day = 6
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("This is Weekend")

day = 7
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("This is Weekend")
"""
"""
month = 4
day = 5
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
"""
"""
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
"""
"""
month = 6
day = 5
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
"""
month = 6
day = 4
match month:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")





