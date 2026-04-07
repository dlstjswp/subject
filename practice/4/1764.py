a, b = input().split()
k1 = []
k2 = []

for i in range(int(a)):
    k1.append(input())


for o in range(int(b)):
    k2.append(input())


f = list(set(k1) & set(k2))
f = sorted(f)

print(len(f))
for items in f:
    print(items)
