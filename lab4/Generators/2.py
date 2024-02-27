#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(N):
    for i in range(N):
        if i % 2 == 0:
            yield i 
        else: 
            continue   
        
    
N = int(input())
squares = even_numbers(N)
for i in squares:
    print(i)
