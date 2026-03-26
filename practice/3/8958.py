b = input()


for m in range(int(b)):
    a = input()
    a = a.replace('X', ' ')
    a = a.replace('  ', ' ')
    a = a.replace('O', '1')
    k = 0

    list = a.split()

    for i in range(int(len(list))):
        list[i] = (int(len(list[i]))**2 + int(len(list[i])))/2

    print(int(sum(list)))
