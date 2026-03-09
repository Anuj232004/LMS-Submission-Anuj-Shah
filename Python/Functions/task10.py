"""
    Applies a dynamic operation ('add', 'subtract', 'multiply', 'divide')
    to a list of numbers using lambda functions.
    
    Parameters:
    - numbers: list of numbers
    - operation: string, one of "add", "subtract", "multiply", "divide"
    
    Returns:
    - result of applying the operation to all numbers
    """

#import
from functools import reduce  # To apply operation cumulatively

#function
def dynamic_function(numbers, operation):
    
    
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else float('inf')
    }
    

    if operation not in operations:
        raise ValueError(f"Invalid operation '{operation}'. Choose from add, subtract, multiply, divide.")
    
  
    result = reduce(operations[operation], numbers)
    return result


#input and print
nums1 = [10, 5, 2]
nums2 = [1, 2, 3, 4]

print("Add:", dynamic_function(nums1, "add"))    
print("Subtract:", dynamic_function(nums1, "subtract"))     
print("Multiply:", dynamic_function(nums2, "multiply")) 
print("Divide:", dynamic_function(nums1, "divide"))   