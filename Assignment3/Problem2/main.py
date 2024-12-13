### Question: Find the Maximum Value in a List Using a Function
##Description: Write a function named find_max
# that takes a list of integers as an argument and returns the maximum value in the list.
##Do not use Python’s built-in max() function.
# The function should handle cases where the list is empty by returning None.

def find_max(numbers):
    if not numbers:  # Handle the case of an empty list
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


numbersList = [3, 5, 7, 2, 8]
print("Maximum value:", find_max(numbersList))  # Output: Maximum value: 8
empty_list = []
print("Maximum value in empty list:", find_max(empty_list))  # Output: Maximum value in empty list: None
