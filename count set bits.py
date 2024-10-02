n=int(input("Enter decimal value: " ))

def convet_to_binary(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    
    # Recursive case: call the function with num // 2 and append num % 2
    return convet_to_binary(num // 2) + str(num % 2)
c=0
binary=convet_to_binary(n)
for i in range(len(binary)):
    if binary[i]=='1':
        c+=1
print(c)
