a, b = input().split()
k1 = {}
k2 = {}

for i in range(int(b)):
    t = str(input())
    k1.update({t:i})
    k2.update({i:t})


k_list = list(k1)
k_val = []


for items in k_list:
    k_val.append(k1.get(items))

h = sorted(k_val)



for u in range(min(int(a), len(h))):
    print(k2[h[u]])
