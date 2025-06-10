n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

t1 = (d1*18)/(v1*5)
t2 = (d2*18)/(v2*5)

if t1 < t2:
    print(n1)
else:
    print(n2)
