list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Piatti","The Grill at Torrey Pines","Hungry Hunter","Shogun" ]
a = []
x=len(list1)
y=len(list2)
for s in range(x) or range(y):
    for i in range(x) or range(y):
        if (i < x and (s - i) < y and list1[i] == list2[s - i]):
            a.append(list1[i])
            print(a)
    if (len(a) > 0):
        break
