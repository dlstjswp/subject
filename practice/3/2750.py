u = int(input())
r = []

for i in range(u):
    y = int(input())
    r.append(y)
    r.sort()

for g in range(u):
    print(r[g])
