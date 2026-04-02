k = int(input())
a = list(map(int,input().split()))
s = 0


for n in range(k):
    for m in range(k):
        s += abs(a[n] - a[m])

print(s)
