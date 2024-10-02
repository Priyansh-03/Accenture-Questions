a=int(input("Enter number a: "))
b=int(input("Enter number b: "))

def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

def lcm(a,b):
    lcm=(a*b)//gcd(a,b)
    return lcm

print(lcm(a,b))