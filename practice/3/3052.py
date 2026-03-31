remain = []

for i in range(10):
    num = int(input())
    remain.append(num%42)

remain = list(set(remain))

print(len(remain))
