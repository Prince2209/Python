#---> ARITHMETIC operator

a = 1
b = 5
c = a + b         #  + , - , * , / , % ...
print(c)


#---> ASSIGNMENT operator

d = 4-2  # Assign 4-2 in d
print(d)
e = 5
e += 2  # it means e = e + 2 = 5 + 2 = 7 
print(e)
x = 4
x += 1  # Increment the value of x by 1 and then Assign it to x 
x -= 1  # Decrement the value of x by 1 and then Assign it to x 
x *= 1
x /= 1
x %= 1


#---> COMPARISON operator
# It gives boolean value, it means true/false.

f = 5<7    # < , > , <= , >= , == , != ...
print(f)


#---> LOGICAL operator

y = True or False
print(y)

# Some Truth Table of logical operator

# 1) "Or"
print("Truth 'Or' False is: ", True or False)
print("Truth 'Or' True is: ", True or True)
print("False 'Or' True is: ", False or True)
print("False 'Or' False is: ", False or False)

# 2) "And"
print("Truth 'And' False is: ", True and False)
print("Truth 'And' True is: ", True and True)
print("False 'And' True is: ", False and True)
print("False 'And' False is: ", False and False)

# 3) "Not"
print(not(True))