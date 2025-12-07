#calculator

# make fuction for add, substract, multiply and division 
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devision(a, b):
    return a / b

#instructions

print("enter for operations:")
print("1 for addition: ")
print("2 for subctration: ")
print("3 for multiplication: ")
print("4 for division: ")

#loop for multiple use

while True:
    
    # condition for choice 
    
    choice = float(input("enter number from 1, 2, 3 and 4 :"))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        try:
            num1 = float(input("enter first number :"))
            num2 = float(input("enter second number :"))
        except ValueError:
            print("invalid number plz try again : ")
            continue
        
        # condition for operations 
        
        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
            
        elif choice == 2:
             print(f"{num1} - {num2} = {substract(num1, num2)}")
             
        elif choice == 3:
             print(f"{num1} x {num2} = {multiply(num1, num2)}")
        
        elif choice == 4:
             print(f"{num1} / {num2} = {devision(num1, num2)}")   
        
        else:
            print("invalied number 3")
        
    else:
        print("try again")        