# def singlDigit(n):
#     s = 0
#     num = str(n)
#     print(num)
#     for i in num:
#         s = s+int(i)

#     if s > 9:
#         singlDigit(s)
#     print('else part')
#     return s


# n = 25660

# print('input:', n)
# print(singlDigit(n))
def singlDigit(n):
    num = str(n)
    s = 0
    for i in num:
        s = s+int(i)

    if s > 9:
        return singlDigit(str(s))
    return str(s)


n = [25660, 12345]

L = []
for i in n:
    L.append(int(str(i)+singlDigit(i)))
print(L)
