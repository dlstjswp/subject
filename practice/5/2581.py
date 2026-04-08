def prime_num(x):
    for i in range(2, round(x**(1/2)) + 2):
        if x%i == 0:
            return 0
    return x



m = int(input())
n = int(input())
p = []

for j in range(m, n+1):
     p.append(prime_num(j))


p = list(set(p))
p.remove(0)

if len(p) != 0:
    print(sum(p))
    print(p[0])
else:
    print(-1)
