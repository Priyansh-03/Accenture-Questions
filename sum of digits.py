def sumOfDigits(n,s):
    while(n!=0):
        temp=n%10
        s+=temp
        n=n//10
    return s

s=0
print(sumOfDigits(123,s))