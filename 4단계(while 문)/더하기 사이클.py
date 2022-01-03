num = int(input())
re_num = num
N = 0

while True :
    N += 1
    a = int((re_num - (re_num % 10)) / 10)
    b = int(re_num % 10)
    result = a + b
    re_num = b * 10 + (result % 10)

    if num == re_num :
        print(N)
        break

# 문제 풀이 방안 :
# 반복할 때마다 사이클의 길이 1씩 증가
# 처음에 받은 수의 십의자리 수와 일의 자리 수의 합을 구함
# 이전의 일의 자리 수와 이전의 결과 값의 합을 구함
# 처음에 받은 수와 이전의 일의 자리 수 * 10과 이전의 결과 더한 것이 같으면 종료.

# 문제1 : num 하나만 사용하여 while 안에서 if문 판별이 어려웠음.
# 해결1 : re_num이라는 변수에 num값을 대입하여 if문 판별을 가능하게함.

# 문제2 : 이전 결과가 한자리 수가 아닌 두자리 수가 나올 경우.
# 해결2 : 10번째 줄에 result 대신 result % 10으로 두자리 수는 result의 일의 자리 수만 사용.



# 이전 틀린 방법
# num = int(input())
# N = 0

# while True :
#     if num < 10 :
#         a = str(0)
#         b = str(num)
#         c = int(a) + int(b)
#         re_num = str(b) + str(c)

#         N += 1

#     elif num >= 10 :
#         a = int((num - (num % 10)) / 10)
#         b = int(num % 10)
#         c = a + b
#         re_num = str(b) + str(c)

#         N += 1
#     elif num == re_num:
#         break
    
# print(N)