arr=[1111]*2

# for i in range(len(arr)-1):
#     if arr[i]==1:
#         for j in range(i+1,len(arr)):
#             if arr[j]==0:
#                 arr[i],arr[j]=arr[j],arr[i]
# print(arr)
zeros=0
ones=0
for i in range(len(arr)):
    if arr[i]==0:
        zeros+=1
print("number of zero = ",zeros)
ones=len(arr)-zeros
print("number of one = ",ones)
for i in range(zeros):
    arr[i]=0

for i in range(zeros, len(arr)):
    arr[i] = 1


print(arr)

    

    
        