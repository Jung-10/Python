all, N = map(int, input().split())
num = list(map(int, input().split()))
result = []

for i in range(all):
    if num[i] < N :
        result.append(str(num[i]))
print(" ".join(result))

# 결과가 [ ]를 포함하여 출력되어서 7번째 줄에 str을 적고
# 8번째 줄에 join으로 합쳐줌.

# join은 문자열로만 구성된 list에서만 사용가능하고 문자열을 합쳐줌.