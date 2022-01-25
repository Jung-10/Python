import math

N = int(input())

for i in range (0, N) :
    X, Y = map(int, input().split())
    distance = int(Y - X)
    max = int(round(math.sqrt(distance), 0))

    if (max * max == distance) :
        print(2 * max - 1)

    elif distance == 2 :
        print(2)
    
    elif distance == 3 :
        print(3)

    elif max * max < distance <= max * max + max :
        print(max * 2)

    else :
        print(max * 2 + 1)