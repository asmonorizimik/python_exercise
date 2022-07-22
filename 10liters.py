def litres(k,x):
    if k>x:
        a=k-x
        print("need",a,"more litres to fill")
    elif k==x:
        print("full")
    else:
        print(x-k,"litre overflow")
k=int(input("capacity of the bucket:"))
x=int(input("in the bucket:"))
litres(k,x)