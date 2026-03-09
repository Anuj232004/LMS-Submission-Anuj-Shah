''' Calculates the factorial of a given  integer using
    an iterative approach along with the time counter decorator.

    Parameters:
        n (int): A integer whose factorial is to be calculated.

    Returns:
        int: The factorial of n (n!) along with time taken.
                       '''

#import
import time

#function (decorator)
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # pass arguments
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

#decorated function
@execution_time
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#input and print
num = 5
print(factorial(num))