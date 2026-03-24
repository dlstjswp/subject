a = int(input())
n = 0

for i in range(a):
  a, b = input().split()
  n += 1
  print(f'Case #{n}: {int(a)+int(b)}')
