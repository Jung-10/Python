N = int(input())

score = list(map(int, input().split()))
result = []

big = score[0]

for i in range(0, N) :

    if score[i] < big:
        big = big
        
    elif score[i] > big:
        big = score[i]


for j in score :
    re_score = j / big * 100
    result.append(re_score)

print(sum(result)/N)


# max를 사용해서 최댓값을 구하는 방법도 있음.
# for문 사용할 때 범위에 리스트 변수를 넣으면 리스트 안에 있는 값이 for문에서 사용됨.