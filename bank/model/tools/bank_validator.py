import re

def title_validator(title):
    if  not type(title_validator) == str and re.match(r"^[A-Za-z\s]{2,20}$", title):
        raise ValueError("Invalid title!")

def branch_validator(branch):
    if  not type(branch_validator) == str and re.match(r"^[A-Za-z\s]{2,20}$", branch):
        raise ValueError("Invalid branch!")

def description_validator(description):
    if  not type(description_validator) == str and re.match(r"^[A-Za-z\s]*$", description):
        raise ValueError("Invalid description!")

def balance_validator():
    if not type(balance_validator) == int or type(balance_validator) == float:
        raise ValueError("Invalid balance!")

def employee_number_validator():
    if not type(balance_validator) == int:
        raise ValueError("Invalid number of employees!")