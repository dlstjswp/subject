def num(a):
    a_list = list(map(int, str(a)))
    for items in a_list:
        a += items
    return a

self_num = True

for i in range(1, 10000):
    for j in range(i//2, i):
        if num(j) == i:
            self_num = False
    if self_num == True:
        print(i)
    self_num = True
