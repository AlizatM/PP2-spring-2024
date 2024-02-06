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
def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return list(filter(lambda x: is_prime(x), numbers))

#5
from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

#6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#8
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

#9
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

#10
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

#11
def is_palindrome(word):
    return word == word[::-1]

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

#13
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
    
    secret_number = random.randint(1, 20)
    num_guesses = 0
    
    while True:
        guess = int(input("Take a guess.\n"))
        num_guesses += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Good job, {}! You guessed my number in {} guesses!".format(name, num_guesses))
            break


print(grams_to_ounces(100))
print(fahrenheit_to_celsius(98.6))
print(solve(35, 94))
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(string_permutations("abc"))
print(reverse_words("We are ready"))
print(has_33([1, 3, 3]))
print(spy_game([1,2,4,0,0,7,5]))
print(sphere_volume(5))
print(unique_elements([1, 2, 3, 1, 2, 3]))
print(is_palindrome("madam"))
print(histogram([4, 9, 7]))
guess_the_number()


