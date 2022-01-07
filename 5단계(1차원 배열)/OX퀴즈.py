sum = 0
plus_score = 0

N = int(input())

for j in range(0, N) :
    answer = list(input())
    for i in range(0, len(answer)) :
        
        if i != 0 and answer[i-1] == "O" and answer[i] == "O" :
            plus_score += 1
            sum += plus_score

        elif answer[i] == "O" :
            sum += 1
            plus_score += 1
        
        elif answer[i] == "X" :
            sum += 0
            plus_score = 0
    print(sum)
    sum = 0
    plus_score = 0


# 값을 list로 받으면 문자가 하나씩 따로따로 리스트에 저장됨.

# plus_score를 사용해서 O가 반복되는 경우의 추가 점수를 계산함.