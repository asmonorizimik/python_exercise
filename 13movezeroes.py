def move_zeroes(a):
    i=0
    c=0
    while i <len(a):
        j=0
        while j<len(a):
            if a[j]==0:
                if a[i]>a[j]:
                    c=a[j]
                    a[j]=a[i]
                    a[i]=c
            j+=1
        i+=1
    return a
print(move_zeroes([0,1,0,0,3,0,12,]))