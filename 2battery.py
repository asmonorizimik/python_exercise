def battery(num):
    a=[]
    i=0
    low=15
    while i<num:
        batt=int(input("enter batt percentage:"))
        a.append(batt)
        i+=1
    print(a)
    print("print \'yes\' if battary is low or \'no\' if above 15%")
    j=0
    while j<len(a):
        if a[j]<=low:
            print(a[j],": yes")
        else:
            print(a[j],": no")
        j+=1
battery(num=int(input("enter no. of phones:")))