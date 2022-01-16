num = input()
num_split = list(num.split('/'))

up = num_split[0]
down = num_split[1]

plus = int(up) + int(down)

result = []

for i in range(1, int(up) + int(down)) :
    result.append("{}/{}".format(i, plus - i))

# 홀수번째 줄은 아래서 위로 올라감.
# 짝수번째 줄은 위에서 아래로 내려감.

if plus == 2 :
    print(1)

elif plus % 2 == 0 : #짝수
    result.reverse()
    for x in range(0, len(result)) :
        if result[x] == num :
            final = (((plus-2)^2 + (plus-2)) / 2) + (x + 1)
            print(int(final))
            break
elif plus % 2 == 1 : #홀수
    for x in range(0, len(result)) :
        if result[x] == num :
            final = (((plus-2)^2 + (plus-2)) / 2) + (x + 1)
            print(int(final))
            break


# 1, 3, 6, 10, 15, 21
# (n^2 + n) / 2

# (n^2 + n) / 2 이전 줄의 개수는 이걸로하고 몇번째인지 더해서 최종 몇번째인지 계산.