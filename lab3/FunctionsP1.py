#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

#3
def solve(numheads, numlegs):
    numchickens = 0
    numrabbits = 0
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        if (2*numchickens + 4*numrabbits) == numlegs:
            return numchickens, numrabbits
    return "No solution"

chickens, rabbits = solve(35, 94)
print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)

#4
