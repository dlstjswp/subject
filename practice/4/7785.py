a = int(input())
name = []

for o in range(a):
    g, h = input().split()
    if h == 'enter':
        name.append(g)

    if h == 'leave':
        name.remove(g)

name = sorted(name, reverse = True)

for i in range(len(name)):
    print(name[i])
