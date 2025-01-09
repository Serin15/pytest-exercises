def assembly(a,b):
    "Returns the sum of two numbers"
    return a + b

def divide(a,b):
    "Splits two numbers. Raises ValueError if b is 0."
    if b == 0:
        raise ValueError("Zero division is not allowed.")
    return a / b

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return "Age is valid"

def only_str(text):
    "Accept strings only, otherwise raises TypeError"
    if not isinstance(text, str):
        raise TypeError("Only strings are supported.")
    return text.upper()