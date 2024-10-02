def box(r,c):
        for i in range(0,r):
            print("\n",end="")
            for j in range(0,c):
                if j==0 or j==c-1 or i==0 or i==r-1 or j==r-1 or j==c-1:
                     print("1",end="")
                else:
                     print("0",end="")
                     

    # for i in range(0,c+1):
    #     print(" ")
    #     for j in range(0,r+1):
    #         if i==0 or i==c:
    #             print(1)
box(10,4)