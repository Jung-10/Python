N = int(input())

kg_3 = 1
result = []

if N % 5 == 0 :
    print(N // 5)
else :
    while N >= 3 :
        N -= 3
        if N % 5 == 0 :
            result.append(kg_3 + N // 5)
        kg_3 += 1
    if len(result) == 0:
        print(-1)
    else :
        print(min(result))


# 다른 방법 시도했는데 반례 존재.
# N = int(input())

# result = []

# if N % 5 == 0 :
#     print(N // 5)
# else :
#     for i in range(1, N//5 + 1) :
#         if (N - 3 * i) % 5 == 0:
#             result.append(i + (N - 3 * i) // 5)
#             break
#         elif N % 3 == 0 :
#             result.append(i + (N // 3))
#     if len(result) == 0 :
#         print(-1)
#     else :
#         print(min(result))