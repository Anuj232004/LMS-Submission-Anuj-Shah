'''Parameters:
    - base_salary (mandatory): float/int
    - bonus_percent (optional, default 10): percentage of bonus
    - deductions (optional, default 5): percentage of deductions
    
    Returns:
    - final salary after applying bonus and deductions'''

#function
def calculate_salary(base_salary, bonus_percent=10, deductions=5):
    return (base_salary + (base_salary * bonus_percent) / 100) - (base_salary * deductions) / 100


#print
print(calculate_salary(10000))
