# 1, 2, 8, 20, 38,
#  1  6  12   18  24
# A + B = c
# A = 2
# B = 6i = 6 * 1 = 6
# A + B = 2 + 6 = 8 = c

num = int(input())

A = 1
result = 1

for i in range(1, num + 1) :
    B = 6 * i
    C = A + B
    A = C

    if num == 1 :
        print(int(1))
    
    elif num >= A :
        result += 1
    
    elif num < A :
        result += 1
        print(result)
        break
