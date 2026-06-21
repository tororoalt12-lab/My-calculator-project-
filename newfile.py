def add(a , b) :
    return (a+b)
def subtract(a, b) :
    return (a-b)
def multiply(a , b) :
    return (a*b)
def divide(a , b) :
    if b == 0:
        print("BROSKI,no no")
    else:
            return a/b  

while True:
    try:
     a =  int(input("enter a first number "))
     b  =  int(input("enter a second number "))
     operator = str(input("enter a operation +,-,*,÷, or quit? "))
    except ValueError:
        print("in numeral,try again")
        continue
    
    if operator == "quit":
        break
    if operator == "+":
        print(add(a, b))
    elif operator == "-":
        print(subtract(a, b))
    elif operator == "*":
        print(multiply(a, b))
    elif operator == "÷":
        print(divide(a, b))
    else:
        print("unvailable")


