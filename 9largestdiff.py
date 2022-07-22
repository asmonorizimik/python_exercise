def largest_diff(l):
    i=0
    m=0
    s=l[i]
    while i<len(l):
        if l[i]>m:
            m=l[i]
        elif l[i]<s:
            s=l[i]
        i+=1
    x=m-s
    return x
print(largest_diff([3,2,1,4]))