import math
def perfectSquare(n):
    intval=floatval=float(math.sqrt(n))
    intval=int(intval)
    if intval==floatval:
        return True
    else:
        return False
print(perfectSquare(25.02))

