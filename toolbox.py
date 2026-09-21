#Function 1 - double

def double(number):
    # Return the number multiplied by 2
    return number * 2

#Function 2 - is_pass

def is_pass(score):
    # Return True if the score is greater than or equal to 50, otherwise return False
    return score >= 50

#Function 3 - greet

def greet(name, greeting="Hello"):
    # Return the greeting, a comma, the name, and an exclamation mark   
    return greeting + ", " + name + "! Welcome to PLP."   

print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))
