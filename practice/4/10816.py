a = int(input())
s1 = list(map(int,input().split()))

count={}
for i in s1:
    try: count[i] += 1
    except: count[i]=1

b = int(input())
s2 = list(map(int,input().split()))


for items in s2:
    if items in count:
        print(count[items], end = " ")
    else:
        print(0, end = " ")
