n = int(input())
div = int(input())

def FindSumOfRemainders(n, div):
    sum=0
    i=1
    while i <=n:
        remainder=i%div
        sum+=remainder
        i+=1
        
    return sum



result = FindSumOfRemainders(n, div)
print(result)