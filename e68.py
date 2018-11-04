from sets import Set

s = Set(['1', '2', '3', '4', '5'])

e0 = 6
e1 = 10
e2 = 9
e3 = 8
e4 = 7

def is_ok(val):
    l = str(val)
    if len(l) != 5:
        return False
    tmp = Set()
    for d in l:
        if d not in s:
            return False
        if d in tmp:
            return False
        tmp.add(d)

    return True

def test(c):
    c = map(int, str(c))

    a = e0 + c[0] + c[1]
    b = e1 + c[1] + c[2]
    q = e2 + c[2] + c[3]
    d = e3 + c[3] + c[4]
    e = e4 + c[4] + c[0]

    return a == b and q == d and e == a

val = 54321
final = 0

for i in range(0, 54321):
    if is_ok(val - i) and test(val - i):
        c = val - i
        break

c = str(c)

final = str(e0) + c[0] + c[1] + str(e1) + c[1] + c[2] + str(e2) + c[2] + c[3] + str(e3) + c[3] + c[4] + str(e4) + c[4] + c[0]

print(final)
