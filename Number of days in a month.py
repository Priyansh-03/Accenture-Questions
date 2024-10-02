def dates(dd,mm,yyyy):
    if mm<=7:
        if mm%2==0:
            return 30
        else:
            return 31
    else:
        if mm%2==0:
            return 31
        else:
            return 30

date=dates(31,11,1996)
print(date)