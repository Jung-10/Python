# 한수 테스트용
# i = 123

# print(i // 100) # 백의 자리수
# print((i % 100) // 10) # 십의 자리수
# print(i % 10) # 일의 자리수

# 한수 문제 함수 사용 안하고 내 방식대로 푼 것
num = int(input())
result = 0

for i in range(1, num + 1) :
    if i < 100 :
        result += 1
    elif i >= 100 and (((i % 100) // 10) - (i // 100)) == ((i % 10) - ((i % 100) // 10)):
        result += 1
    else :
        result += 0

print(result)