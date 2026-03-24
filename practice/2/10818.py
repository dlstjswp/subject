a = int(input())
number_list = input().split()
min_num = int(number_list[0])
max_num = int(number_list[0])
k = -1

for i in range(a):
  k += 1
  if min_num >= int(number_list[k]):
    min_num = int(number_list[k])
  if max_num <= int(number_list[k]):
    max_num = int(number_list[k])


print(min_num, max_num)
