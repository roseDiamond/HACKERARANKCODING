# return list with sam lengeth, first element is sum of all elem then revered elem of list except one

l = [1, 3, 4, 5]
n = len(l)-1


def nl(l):
    m = []
    f = 1
    for i in range(n, 0, -1):

        if i == n:
            for j in range(0, len(l)):
                f = f*l[j]
            m.append(f)
            f = 1

        f = l[i]*f
        print(f'i:{i} and v={l[i]} and f ={f}')
        m.append(f)
        f = 1
    return m


print(nl(l))
