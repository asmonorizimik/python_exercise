# numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL",
#              50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
# num = int(input("enter digit:"))  # LVIII
# roman = ''
# for k, v in sorted(numerals.items(), reverse=True):
#     while num >= k:
#         roman += v
#         num -= k
# print(roman)







# n = int(input("Enter the number: "))
# num = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
# rom = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
# result = ''
# for i in range(len(num)) :
#     count = int(n / num[i])
#     result += str(rom[i] * count)
#     n -= num[i] * count
# print(result)



# values =	{
#   "I": 1,
#   "V": 5,
#   "X": 10,
#   "L": 50,
#   "C": 100,
#   "D": 500,
#   "M": 1000,
# }

# def romanToInt(str): 
#   total = 0
#   i = 0
#   while (i < len(str)): 
#     s1 = values[str[i]]
#     if (i+1 < len(str)): 
#         s2 = values[str[i+1]]
#         if (s1 >= s2): 
#           total = total + s1 
#           i = i + 1
#         else: 
#           total = total - s1 
#           i = i + 1
#     else: 
#       total = total + s1 
#       i = i + 1
#   return total
  
# # Driver code 
# print(romanToInt("MCMXCIV")) 




# def romanTointeger(num,value,symbol):
#   roman=""
#   i=0
#   while num>0:
#     div=num//value[i]
#     num=num%value[i]
#     while div>0:
#       roman=roman + symbol[i]
#       div-=1
#     i+=1
#   return roman
# num=int(input("enter integer number: "))
# value = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
# symbol = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
# print(romanTointeger(num,value,symbol))