#Create a Python function that evaluatesthe strength of a password entered by theuser. Implement checks for factors such aslength, presence of uppercase andlowercase letters, digits, and specialcharacters.

import re

def check_password(password):
    # Minimum length requirement
    length = 8

    # Regular expressions to check for character types
    lowercase = re.search(r'[a-z]', password)
    uppercase = re.search(r'[A-Z]', password)
    digit = re.search(r'\d', password)
    special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Initialize a strength variable
    strength = 0

    # Check length
    if len(password) >= length:
        strength += 1

    # Check character types
    if lowercase:
        strength += 1
    if uppercase:
        strength += 1
    if digit:
        strength += 1
    if special_char:
        strength += 1

    # Evaluate the overall strength of the password
    if strength < 3:
        return "Weak"
    elif strength < 4:
        return "Moderate"
    else:
        return "Strong"

# Example usage
password = input("Enter a password: ")
strength = check_password(password)
print(f"Password strength: {strength}")
