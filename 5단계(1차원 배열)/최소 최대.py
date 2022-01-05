N = int(input())

num = list(map(int, input().split()))
small = num[0]
big = num[0]

for i in range(0, N):
    if num[i] < small and num[i] < big:
        small = num[i]
        big = big
        
    elif num[i] < small and num[i] > big:
        small = num[i]
        big = num[i]
        
    elif num[i] > small and num[i] < big:
        small = small
        big = big
        
    elif num[i] > small and num[i] > big:
        small = small
        big = num[i]

print(small, big)


# 이전 답안
# N = int(input())

# num = list(map(int, input().split()))

# for i in range(N):
#     if num[i] < num[i+1] :
#         small = num[i]
#         big = num[i+1]
#     elif num[i] > num[i+1]:
#         small = num[i+1]
#         big = num[i]

# print(small, big)