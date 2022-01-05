a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
mul_str = list(str(mul))

for i in range(0, 10) :
    print(mul_str.count(str(i)))


# count 메소드 : count는 문자열의 갯수가 몇 개인지 확인하기 쉽게 사용 가능.
# 비교할 숫자와 리스트 안의 숫자 모드 문자열로 바꿔줌.
# 리스트 안의 수와 비교하여 갯수를 셈.