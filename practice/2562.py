num_list = []
for i in range(9):
  num_list.append(input())



max_num = int(num_list[0])


for k in range(9):
  if max_num <= int(num_list[k]):
    max_num = int(num_list[k])



print(max_num)
print(num_list.index(str(max_num)) + 1)
