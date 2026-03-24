num = int(input())
old_num = num
ten_th = num // 10
one_th = num % 10
new_num = ten_th + one_th
new_num_one_th = new_num % 10
num = new_num_one_th + 10*one_th
a = 1


while num != old_num:
  ten_th = num // 10
  one_th = num % 10
  new_num = ten_th + one_th
  new_num_one_th = new_num % 10
  num = new_num_one_th + 10*one_th
  a += 1

print(a)
