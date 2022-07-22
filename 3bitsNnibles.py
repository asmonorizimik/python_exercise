def nibles(x,bits=4):
    n=x/bits
    print(n)
    if n==int(n):
        print("good")
    else:
        print("not good")
nibles(x=int(input("enter:")))