# 홀수번째 줄은 아래서 위로 올라감.
# 짝수번째 줄은 위에서 아래로 내려감.

num = int(input())

line = 0
line_max_num = 0

while line_max_num < num :
    line += 1
    line_max_num += line

order = line_max_num - num

if line % 2 == 0 :
    up = line - order
    down = order + 1
elif line % 2 == 1 :
    up = order + 1
    down = line - order

print("{}/{}".format(up, down))