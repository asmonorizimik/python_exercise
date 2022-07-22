def coins(x,y):
    if x or y>=0:
        ten=10*x
        five=5*y
        print("sum of 10 rupees =",ten,"\nsum of 5 rupees ="+str(five))
        print("total rupees =",ten+five)
    else:
        print("nothing")
coins(x=int(input("no of ten rupees =")),y=int(input("no. of five rupees =")))
