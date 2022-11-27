def sqxt(x):
    low = 0
    high  = x

    while(low<high):
        mid = low+(low+high)//2
        square = mid*mid

        if x<square:
            high  = mid-1
        else:
            low = mid+1
    return mid
sqxt(32)
