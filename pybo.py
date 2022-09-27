# FIBONACCI PYTHON LIBRARY
import math

# INITIALIZE A FUNCTION USING A FIBONACCI FORMULA
def fibo(n):
    return (((1 + math.sqrt(5))/2)**n - ((1 - math.sqrt(5))/2)**n)/math.sqrt(5) # A CODE FROM A FORMULA OF FIBONACCI SEQUENCE

# PROCESS A FIBONACCI FUNCTION
def fibonacci(n):
    for yr in range(n+1):
        print(str(yr) + ". " + str(int(fibo(yr))))
        
# CALL A FIBONACCI FUNCTION
fibonacci(100)
