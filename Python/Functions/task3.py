'''
    Calculates the nth Fibonacci number using recursion.

    Parameters:
        The position in the Fibonacci sequence (0-based index).
        Must be a non-negative integer.

    Returns:
        The nth Fibonacci number.
        '''

#function
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

#print
print([fibonacci_recursive(i) for i in range(30)])
