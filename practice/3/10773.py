u = int(input())
k = []

for j in range(u):
    o = int(input())

    if o != 0:
        k.append(o)
    else:
        del k[len(k) - 1]

print(sum(k))
