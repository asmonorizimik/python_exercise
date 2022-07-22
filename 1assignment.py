def assignment(start_time,complete=10):
    if start_time<complete:
        ass=3
        x=complete-start_time
        if x>=ass:
            print("yes, has",x,"hours")
        else:
            print("no, only",complete-start_time,"hour")
    else:
        print("no time for assignment")
assignment(start_time=int(input("enter time to start:")))
    