def faster(bike,car):
    if bike<car:
        print("BIKE :",car-bike,"minutes faster than car")
    elif bike ==car:
        print("ANY VEHICLE")
    else:
        print("CAR :",bike-car,"minutes faster than bike")
bike=int(input("minutes taken by bike"))
car=int(input("minuts taken by car"))
faster(bike,car)