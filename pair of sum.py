arr=[0,2,5,7,4,6,10,20,-10,2,2,2,2,3]
target=10
dict={}
for i in range(len(arr)):
    elem=arr[i]
    dict[elem]=i
# for value in dict.items():
#     print(value)

pair=set()
for i in range(len(arr)):
    a=arr[i]
    b=target-a
    if b in dict:
        pair.add((min(a,b),max(a,b)))
    
print(pair)
print(len(pair))
    
