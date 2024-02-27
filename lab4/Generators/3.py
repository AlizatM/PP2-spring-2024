def even_numbers(N):
    for i in range(N):
        if i % 3 == 0 and i % 4 == 0:
            yield i 
        else: 
            continue   
        
    
N = int(input())
squares = even_numbers(N)
for i in squares:
    print(i)
