'''
Analyzes a list of integers by first squaring each element and then
    filtering out values that are less than or equal to 50.

    Parameters:
        intList (list of int): A list containing integer values to be processed.

    Returns:
        filter object: An iterator containing squared values greater than 50.
                       (Convert to list to view actual results.)
'''

#Function
def analyze_numbers(intList):
    squared= list(map(lambda x: x**2,intList))
    filtered= list(filter(lambda x:x>50,squared))
    return filtered

#input and print
print(analyze_numbers([1,2,3,4,5,6,7,8,9]))