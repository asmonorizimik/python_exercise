def tyres():
    b=2*bike
    c=4*car
    print(b,":tyres of bike","\n",c,":tyres of cars")
    if bike or car > 0:
        print("no. of tyres on the road is:",b+c)
    else:
        print("no vehicle")
bike=int(input("enter the number of bike:"))
car=int(input("enter the number of cars:"))
tyres()