# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


list1 = [1,2,4]
list2 = [1,3,4]
list3=[]
i=0
j=0
while i <len(list1) or j<len(list2):
    if len(list1)>0 or len(list2)>0:
        list3.append(list1[i])
        list3.append(list2[j])
    else:
        list3.append()
    i+=1
    j+=1
list3.sort()
print(list3)