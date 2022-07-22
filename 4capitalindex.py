def capital_index(s):
    i=0
    a=[]
    while i<len(s):
        if s[i].isupper():
            a.append(i)
        i+=1
    print(a)
capital_index(s="HeLlO")