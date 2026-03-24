a = input()
b = input()
c = input()

a = a.replace('0', '')
a = a.replace(' ', '') + "2"
b = b.replace('0', '')
b = b.replace(' ', '') + "2"
c = c.replace('0', '')
c = c.replace(' ', '') + "2"

a = int(a)
b = int(b)
c = int(c)

if a == 1112:
  print("A")
elif a == 112:
  print("B")
elif a == 12:
  print("C")
elif a == 2:
  print("D")
else:
  print("E")


if b == 1112:
  print("A")
elif b == 112:
  print("B")
elif b == 12:
  print("C")
elif b == 2:
  print("D")
else:
  print("E")


if c == 1112:
  print("A")
elif c == 112:
  print("B")
elif c == 12:
  print("C")
elif c == 2:
  print("D")
else:
  print("E")
