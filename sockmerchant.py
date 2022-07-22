# def sockMerchant(n,ar):
#     x=1
#     while x<=n:
#         ar.append(int(input("enter number for the pairs")))
#         x+=1
#     # ar.sort()
#     print(ar)
#     if len(ar)>2:
#         result = 0
#         i = 0
#         j = 1
#         while i <len(ar):
#             if(ar[i] == ar[j-1]):
#                 result=result+1
#             i=i+1
#             j=j+1
#             i=i+1
#             j=j+1
#             if(j == len(ar)):
#                 break
#         return result
#     else:
#         return "1 pair or no pair"
# print(sockMerchant(int(input("enter the number")),[]))




# def sockMerchant(n, ar):
#     if len(ar)>2:
#         ar.sort()
#         result=0
#         i=1
#         j=0
#         while i<len(ar):
#             if ar[i]==ar[j]:
#                 result+=1
#             i+=1
#             j+=1
#             i+=1
#             j+=1
#             if j==len(ar):
#                 break
#         return result
#     else:
#         return "1 pair or not pair"
# print(sockMerchant(int(input()),[10, 20, 20, 10, 10, 30, 50, 10, 20]))#[4,5,5,5,6,6,4,1,4,4,3,6,6,3,6,1,4,5,5,5]))



print(0.9*27500*9.5)