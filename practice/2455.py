k = 0
M = 0
s = []

for i in range (4):
  a, b = input().split()
  m = int(b) - int(a)
  k += m
  if k > M:
    M=k


print(M)
