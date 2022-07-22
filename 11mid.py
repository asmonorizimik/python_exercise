def mid(s):
    i=0
    a=""
    while i<len(s):
        if len(s)%2==0:
            return repr(a)
        else:
            a=len(s)//2
            return repr((s[i+a]))
        i+=1
print(mid(s=input("enter the string value: ")))