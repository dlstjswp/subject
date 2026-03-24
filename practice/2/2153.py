import math


def convert(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27


letter = list(input())
converted = [convert(item) for item in letter]
a = 2
r = sum(converted)

while a <= int(math.sqrt(r))+1:
  if r == 1:
    print("It is a prime word.")
    break
  elif r == 2:
    print("It is a prime word.")
    break
  elif r % a == 0:
    print("It is not a prime word.")
    break
  else:
    a += 1
else:
  print("It is a prime word.")
