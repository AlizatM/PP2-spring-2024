import time
from math import sqrt

def sqrt_number(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

number = 25100
milliseconds = 2123
sqrt_number(number, milliseconds)
