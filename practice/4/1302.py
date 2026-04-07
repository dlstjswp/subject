a = int(input())
k = []
u = []


for i in range(a):
    k.append(input())

k_set = list(set(k))
k_set = sorted(k_set)

for items in k_set:
    u.append(k.count(items))


print(k_set[u.index(max(u))])
