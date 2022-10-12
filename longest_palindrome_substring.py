s = 'forgeeksskeegfor'
L = []
for i in range(0, len(s)):
    # print('i:',i,s[i])
    r = ''
    for j in range(i, len(s)):

        r = r+s[j]
        # print('j',j,'r+s[j]',r)

        if len(r) > 1 and (r == r[::-1]):
            L.append(r)
            # print('list',L)
    # print('**********************************************************************')
print(L, max(L, key=len))
X = 'mond', 'aaaaa'
lon = ''
for i in X:
    if len(i) > len(lon):
        lon = i
