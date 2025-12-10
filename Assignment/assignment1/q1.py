# Question 1 
# Write a program that asks the user to input a password and checks its strength. 
# • Weak: Less than 6 characters 
# • Medium: 6-10 characters and contains at least one digit 
# • Strong: More than 10 characters and contains at least one digit and at least one 
# uppercase letter 
 
# Example: 
# Input: "hello123" 
# Output: "Medium password" 

def pass_strength(password):
    if len(password) > 10 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return "Strong"
    elif len(password)>=6 and any(char.isdigit() for char in password):
        return "Medium"
    else:
        return "Weak"

password = input("Enter the password: ")
print(pass_strength(password), "password")