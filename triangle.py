n = 4
for i in range(1, n+1):
    print(' '*(n-i)+'c '*i)

for j in range(n-1, 0, -1):
    print(' '*(n-j)+'c '*j)


for i in range(1, n+1):
    print(f"{' '*(n-i)}{i*'b '}")

    # def addDigits(self, num: int) -> int:
    #     while len(str(num)) != 1:
    #         num = str(num)
    #         num = sum([int(k) for k in num])
    #     return num

# n = 25930
# print(digSum(n))

#     def addDigits(self, num: int) -> int:
#         while len(str(num)) != 1:
#             num = str(num)
#             num = sum([int(k) for k in num])
#         return num

# # l=[25930,11345]
# x=[]
# for i in l:
#     y=digSum(i)
#     x.append(y)

# print(x)
