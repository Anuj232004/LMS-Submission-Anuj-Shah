'''
 Aggregates a list of numbers using a custom binary function.

    Parameters:
        intList (list of int/float): A non-empty list of numeric values.
        func (function): A function that accepts two arguments and
                         returns a single combined result (e.g., sum, product).

    Returns:
        int/float: The final aggregated result after applying the function
                   to all elements in the list.
 '''

#function
def custom_aggregate(intList, func):
    result = intList[0]  
    for num in intList[1:]:
        result = func(result, num)
    
    return result
#function
sum_result = custom_aggregate(
    [1, 2, 3, 4],
    lambda x, y: x + y
)
#function
product_result = custom_aggregate(
    [1, 2, 3, 4],
    lambda x, y: x * y
)

# print and output
print(product_result)  
print(sum_result)



