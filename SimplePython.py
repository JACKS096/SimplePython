# define functions
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

 # take input from the user 
print("Select operation.") 
print("1.Add") 
print("2.Subtract") 
print("3.Multiply") 
print("4.Divide") 

 # Store input numbers 
choice = input("Enter choice(1/2/3/4): ")

 # Convert string to int for switch case 
choice = int(choice)

 # Take two numbers from the user 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
if choice == 1:  print(num1,"+",num2,"=", add(num1,num2)) 
elif choice == 2: print(num1,"-",num2,"=", subtract(num1,num2)) 
elif choice == 3: print(num1,"*",num2,"=", multiply(num1,num2)) 
elif choice == 4: print(num1,"/",num2,"=", divide(num1, num2)) 
else: print("Invalid input")
 
