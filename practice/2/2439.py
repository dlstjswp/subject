num = int(input())
a = 0

for i in range(num):
  a += 1
  print(('*' * a).rjust(num))
