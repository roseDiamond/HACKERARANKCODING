# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

s = 'ABCDEFGHIJ'
w = 4


def wrap(s, w):
    c = 0
    l = []
    for i in s:
        l.append(i)
        c = c+1

        if c == w:
            l.append("\n")
            c = 0
    return l, "".join(l)


l, s = wrap(s, w)
print(f'list:{l}\n\n{s}')
