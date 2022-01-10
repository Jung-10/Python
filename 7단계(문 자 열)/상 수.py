num = list(map(int, input().split()))

num0_100 = num[0] // 100

num0_10 = (num[0] % 100) // 10

num0_1 = num[0] % 10

num1_100 = num[1] // 100

num1_10 = (num[1] % 100) // 10

num1_1 = num[1] % 10

re_num0 = int(str(num0_1) + str(num0_10) + str(num0_100))

re_num1 = int(str(num1_1) + str(num1_10) + str(num1_100))

if re_num0 > re_num1 :
    print(re_num0)
else :
    print(re_num1)