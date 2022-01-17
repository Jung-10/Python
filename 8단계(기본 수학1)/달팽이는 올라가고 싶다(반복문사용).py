# A  낮
# B  밤
# V  높이

A, B, V = map(int, input().split())

result = 0
day = 1

while result <= V :
    result += A
    if result < V :
        result -= B
        day += 1
    

print(day)