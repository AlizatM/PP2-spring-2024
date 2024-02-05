#Python Tuples
#1
mytuple = ("apple", "banana", "cherry")

#2
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#3
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#4
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#5
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#6
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#7
tuple1 = ("abc", 34, True, 40, "male")

#8
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#9
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#10
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Access Tuples
#1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Update Tuples
#1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Unpacking Tuples
#1
fruits = ("apple", "banana", "cherry")

#2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#4

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop Tuples
#1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Tuples
#1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found




