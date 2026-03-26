a, b = input().split()
a = int(a)
b = int(b)
max_num = 0
u = 0

for i in range(1, b+1):
    k_1 = ''
    k = str(a * i)
    for c in k:
      k_1 = c + k_1
    u = int(k_1)
    if u >= max_num:
        max_num = u
    else:
        max_num = max_num

print(max_num)
