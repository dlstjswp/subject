o = int(input())


for e in range(o):
    j = input()
    k = True
    while k:
        j = j.replace('()', '')
        k = "()" in j


    if j == '':
        print("YES")
    else:
        print("NO")

