# number- 0 1 1 2 3 5 8 
# positi- 0 1 2 3 4 5 6

def fib(n):
    

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)     
    

n=int(input("Enter nth position: " ))
print(fib(n))
