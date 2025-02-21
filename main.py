a = 16
a = a // 2
print(a**2)
a: int = a + 11
print(a+1)
a = a - 3
print(a)

print((3 + 10 ** 2 / 2) or 70.0)


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


# Example usage:
print(palindrome("7489617719749244646336564429479177169847"))  # True
print(palindrome("8025833559061079503003059701609553385208"))  # True
print(palindrome("6593036601359343374664733439531066303956"))  # True
print(palindrome("5485839837501070045005400701057389385845"))  # True


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


# Given numbers
numbers = [
    "7489617719749244646336564429479177169847",
    "8025833559061079503003059701609553385208",
    "6593036601359343374664733439531066303956",
    "5485839837501070045005400701057389385845"
]

# Check which number is NOT a palindrome
for num in numbers:
    if not palindrome(num):
        print(f"NOT a palindrome: {num}")

# Example with a list (mutable)
my_list = [1, 2, 3, 4]
print("Original list:", my_list)

# Modify the list by changing an element
my_list[2] = 99
print("Modified list:", my_list)  # The list is changed in place

# Example with a string (immutable)
my_string = "hello"
print("Original string:", my_string)

# Try to modify the string by changing a character
# This will raise an error because strings are immutable
try:
    my_string[1] = 'a'  # This line will cause an error
except TypeError as e:
    print("Error:", e)

# To "modify" a string, you create a new string
new_string = my_string[:1] + 'a' + my_string[2:]
print("New string:", new_string)  # A new string is created

import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Iterate through the list and perform replacements
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    else:
        # Replace numbers less than or equal to 50 with "XX"
        random_numbers[i] = "XX"

# Print the modified list
print(random_numbers)


def is_valid_url(url):
    # Check if the URL starts with 'http://' or 'https://'
    if not (url.startswith('http://') or url.startswith('https://')):
        return False

    # Check if there is at least one '.' in the domain part
    # The domain part starts after 'http://' or 'https://'
    domain_start = url.find('://') + 3
    domain = url[domain_start:]

    if '.' not in domain:
        return False

    # Check if there is at least one character before and after the '.'
    dot_index = domain.find('.')
    if dot_index == 0 or dot_index == len(domain) - 1:
        return False

    # If all checks pass, the URL is considered valid
    return True


# Example:
print(is_valid_url("http://pleasegivemea10.com"))  # True
print(is_valid_url("https://givemea10.com"))  # True
print(is_valid_url("ftp://gimmea10please.com"))  # False
print(is_valid_url("http://com"))  # False
print(is_valid_url("http://.com"))  # False


def days_since_birth(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))

    # Get the current year (assuming the current year is 2025 as per the file name)
    current_year = 2025

    # Initialize the total days counter
    total_days = 0

    # Iterate through each year from the year after the birth year to the year before the current year
    for y in range(year + 1, current_year):
        # Check if the year is a leap year
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    return total_days


# Example usage:
birthday = "23-10-2004"
print(days_since_birth(birthday))

import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)