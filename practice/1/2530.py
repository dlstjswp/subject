import math
h, m, s = input() .split()
t = input()
h = int(h)
m = int(m)
s = int(s)
t = int(t)



s = s + t
while s >= 60:
  s = s - 60
  m = m + 1

while m >= 60:
  m = m - 60
  h = h + 1

while h >= 24:
  h = h - 24


h = str(h)
m = str(m)
s = str(s)
print(f'{h} {m} {s}')
