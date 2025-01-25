#NAME:SHALINI GEORGE
#ROLL NO:45

#Python program for a simple calculator

def add(x,y):
    sum=x+y
    return sum
def subtract(x,y):
    difference=x-y
    return difference
def multiply(x,y):
    product=x*y
    return product
def divide(x,y):
    quotient=x/y
    return quotient
print('''OPERATIONS
      1.Addition
      2.Subtraction
      3.Multiplication
      4.Division''')
a=int(input("Select operation:"))
5
x= int(input("Enter first number: "))
y= int(input("Enter second number: "))

if a== 1:
    print(x,"+", y,"=",add(x,y))

elif a== 2:
    print(x,"-",y,"=",subtract(x,y))

elif a== 3:
    print(x,"*",y,"=",multiply(x,y))

elif a== 4:
    print(x,"/",y, "=",divide(x,y))
else:
    print("Invalid input")