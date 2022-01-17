T = int(input())

for i in range(0, T) :
    H, W, N = map(int, input().split())

    if N % H == 0 :
        room_number_last = (N // H)
        floor_number = H

    else :
        room_number_last = (N // H) + 1
        floor_number = N % H

    if room_number_last < 10 :
        result = int(str(floor_number) + str(0) +str(room_number_last))
        print(result)
    else :
        result = int(str(floor_number) + str(room_number_last))
        print(result)

