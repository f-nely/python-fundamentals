"""
Python Try Except

How try() works? 
First, the try clause is executed i.e. the code between try.
If there is no exception, then only the try clause will run, except clause is finished.
If any exception occurs, the try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn't handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
A try statement can have more than one except clause
"""

# Example 1: No exception, so the try clause will run 
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 2)

# Example 2: There is an exception so only except clause will run
# Python code to illustrate
# working of try() 
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 0)

# Example 3: it only accepts exceptions that you're meant to catch or you can check which error is occurring

# code
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
       # By this way we can know about the type of error occurring
        print("The error is: ",e)

        
divide(3, "GFG") 
divide(3,0)

# Else Clause. The code enters the else block only if the try clause does not raise an exception
# Program to depict else clause with try-except
 
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
 
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

# Finally which is always executed after the try and except blocks
# Python program to demonstrate finally 
# No exception Exception raised in try block 
try: 
    k = 5//0 # raises divide by zero exception. 
    print(k) 
   
# handles zerodivision exception     
except ZeroDivisionError:    
    print("Can't divide by zero") 
       
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed')


# Nested Try-Except Blocks. In Python, you can nest try-except blocks to handle exceptions at multiple levels
def divide_and_access(a, b):
    try:
        result = a // b
        print("Result:", result)
        
        try:
            lst = [1, 2, 3]
            print("Accessing index 5:", lst[5])  # This will raise IndexError
        except IndexError:
            print("Handled inner IndexError: Invalid index access.")
    
    except ZeroDivisionError:
        print("Handled outer ZeroDivisionError: Cannot divide by zero.")

    finally:
        print("Outer finally block always runs.")

# Testing both types of exceptions
divide_and_access(6, 2)
print("---")
divide_and_access(6, 0)

