n=int(input("Enter number: "))
# temp=1
# while(n>0):
#     temp=temp*n
#     n=n-1

# print(temp)

# start=6
# end=0
# ans=1
# jump=-1
# for i in range(start,end,jump):
#     if i >0:
#         ans=ans*i
#         i-=1
# print(ans)


def f(num):
    if num<=1:
        return 1
    if num==2:
        return 2
  
    return num*f(num-1)
print(f(n))


