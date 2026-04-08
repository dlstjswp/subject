num = 0


def hansu(a):
    global num
    if a <= 99:
        num += 1
    else:
        a_list = list(str(a))
        k = []
        for i in range(len(a_list) - 1):
            k.append(int(a_list[i]) - int(a_list[i+1]))
        if len(set(k)) == 1:
            num += 1


o = int(input())

for i in range(1, o+1):
    hansu(i)


print(num)
