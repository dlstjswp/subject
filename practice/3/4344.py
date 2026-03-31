Q_count = int(input())

def selecting(x):
    if x > sum(all_grade)/len(all_grade):
        return 1
    else:
        return 0

for i in range(Q_count):
    all_grade = list(map(int, input().split()))
    all_grade.remove(all_grade[0])
    pass_grade = list(map(selecting, all_grade))
    percentage = (sum(pass_grade)/len(pass_grade))*100
    percentage = round(percentage, 3)
    print(f'{percentage:.3f}%')
