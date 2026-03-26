a = int(input())
k = int(a/2)
k_1 = int((a+1)/2)
k_2 = int((a+1)/2 - 1)

for i in range(a):
    if a%2 == 0:
        print(("* " * k) .rstrip())
        print((" *" * k) .rstrip())
    elif a == 1:
        print("*")
    else:
        print(("* " * k_1) .rstrip())
        print((" *" * k_2) .rstrip())
