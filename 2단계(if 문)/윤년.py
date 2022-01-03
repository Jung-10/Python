year = int(input())

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) :
    print(1)
else :
    print(0)

# 파이썬은 &&, ||이 아니라 and, or로 사용