a=int(input())
b=int(input())


k = b%10
f1 = int(a*k)

k = (b%100 - b%10)/10
f2 = int(a*k)

k = (b - b%100)/100
f3 = int(a*k)

print(f1)
print(f2)
print(f3)
print(a*b)
