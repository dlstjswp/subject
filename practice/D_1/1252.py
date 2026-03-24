a,b = input().split()
a = int(a)
b = int(b)
c = " " + str(a + b)


while c.find("1u") != -1 or c.find("2") != -1:
 c = c.replace('1u', '2')
 c = c.replace('2', 'u0')


c = c.replace('0u', '1')
c = c.replace(' u', '1')
c = c.replace(' ', '')


print(c)
