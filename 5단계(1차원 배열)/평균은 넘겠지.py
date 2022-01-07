student_N = int(input())

student_score = []

result = 0

for k in range(0, student_N) :
    student_all = list(map(int, input().split()))
    
    for j in range(1, len(student_all)) :
        student_score.append(student_all[j])

    for i in student_score :
        if (sum(student_score)/student_all[0]) < i :
            result += 1
    
    print("{:.3f}%".format(result/student_all[0] * 100))
    result = 0
    student_score = []

# 소수점을 나타내려면 format 사용하여 {}안에 :.f 사용.