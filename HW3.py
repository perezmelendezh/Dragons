#1.Power of a Number
def custom_power(x, y):
    """
    Computes x raised to the power y using a loop.
    """
    result = 1
    for _ in range(y):
        result *= x
    return result
# Example 
x_value = 2
y_value = 3
result = custom_power(x_value, y_value)
print(f"{x_value}^{y_value} = {result}")

#2.Minimum and Maximum
def find_min_max(numbers):
    """
    Finds the minimum and maximum values in a list of numbers.
    Args:
        numbers (list): A list of numerical values.
    Returns:
        tuple: A tuple containing the minimum and maximum values.
    """
    if not numbers:
        return None, None 
    min_value = max_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num
    return min_value, max_value
#Example
my_numbers = [5, 12, 3, 8, 20, 1]
min_val, max_val = find_min_max(my_numbers)
print(f"Minimum value: {min_val}, Maximum value: {max_val}")

#3.Check Leap Year
def is_leap_year(year):
    """
    Determines whether a year is a leap year.
    Args:
        year (int): The year to check.
    Returns:
        bool: True if it's a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#Example
input_year = 2000
if is_leap_year(input_year):
    print(f"{input_year} is a leap year.")
else:
    print(f"{input_year} is not a leap year.")
  
  #4.Calculate BMI (Body Mass Index)
def calculate_bmi(weight_kg, height_m):
    """
    Calculates the Body Mass Index (BMI) given weight (in kilograms) and height (in meters).
    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.
    Returns:
        float: The calculated BMI.
    """
    if height_m <= 0:
        raise ValueError("Height must be positive and non-zero.")
    bmi = weight_kg / (height_m ** 2)
    return bmi
#Example
weight = 70 
height = 1.75 
bmi_result = calculate_bmi(weight, height)
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi_result:.2f}")

#5.Rotating Digits
def rotate_digits(n):
    """
    Rotates the digits of an integer to the right by one position.
    Args:
        n (int): The input integer.
    Returns:
        int: The rotated integer.
    """
    last_digit = n % 10 
    remaining_digits = n // 10
    rotated_n = last_digit * (10 ** (len(str(n)) - 1)) + remaining_digits
    return rotated_n
#Example
input_number = 12345
rotated_result = rotate_digits(input_number)
print(f"Rotated result: {rotated_result}")

#6.Minimum and Maximum but with Loops
#for a minimun
def find_min_for(numbers):
    """
    Finds the minimum value in a list of numbers using a for loop.
    Args:
        numbers (list): A list of numerical values.
    Returns:
        float or None: The minimum value or None if the list is empty.
    """
    if not numbers:
        return None
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value
#Example
my_numbers = [5, 12, 3, 8, 20, 1]
min_val_for = find_min_for(my_numbers)
print(f"Minimum value (for loop): {min_val_for}")

#for a maximun
def find_max_for(numbers):
    """
    Finds the maximum value in a list of numbers using a for loop.
    Args:
        numbers (list): A list of numerical values.
    Returns:
        float or None: The maximum value or None if the list is empty.
    """
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
#Example:
max_val_for = find_max_for(my_numbers)
print(f"Maximum value (for loop): {max_val_for}")

#for a minimun using a loop
def find_min_while(numbers):
    """
    Finds the minimum value in a list of numbers using a while loop.
    Args:
        numbers (list): A list of numerical values.
    Returns:
        float or None: The minimum value or None if the list is empty.
    """
    if not numbers:
        return None
    min_value = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < min_value:
            min_value = numbers[i]
        i += 1
    return min_value
#Example:
min_val_while = find_min_while(my_numbers)
print(f"Minimum value (while loop): {min_val_while}")

#For a Maximun using a loop
def find_max_while(numbers):
    """
    Finds the maximum value in a list of numbers using a while loop.
    Args:
        numbers (list): A list of numerical values.
    Returns:
        float or None: The maximum value or None if the list is empty.
    """
    if not numbers:
        return None
    max_value = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > max_value:
            max_value = numbers[i]
        i += 1
    return max_value
#Example
max_val_while = find_max_while(my_numbers)
print(f"Maximum value (while loop): {max_val_while}")

#7.Vowels
def vowel_count(input_string):
    """
    Counts the number of vowels (a, e, i, o, u) in a given string.
    Args:
        input_string (str): The input string.
    Returns:
        int: The total count of vowels.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
#Example
user_input = "UC Berkeley"
total_vowels = vowel_count(user_input)
print(f"Total vowels in '{user_input}': {total_vowels}")

#8.Digital Root
def digital_root(n):
    """
    Calculates the digital root (sum of digits) of an integer.
    Args:
        n (int): The input integer.
    Returns:
        int: The digital root.
    """
    if n < 10:
        return n
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digital_root(digit_sum)
#Example
input_number = 12345
result = digital_root(input_number)
print(f"Digital root of {input_number}: {result}")









