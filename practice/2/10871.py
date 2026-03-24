a, b = input().split()
a = int(a)
b = int(b)
k = 0
c = input().split()


for i in range(a):
  if int(c[k]) < b:
    print(c[k], end=" ")
  k += 1
