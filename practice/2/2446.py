num = int(input())
a = num
k = 2*a - 1
m = k

for i in range(num):
  print(('*' * k).center(m).rstrip())
  a -= 1
  k = 2*a - 1

a = 1

for p in range(num-1):
  a += 1
  k = 2*a - 1 
  print(('*' * k).center(m).rstrip())
