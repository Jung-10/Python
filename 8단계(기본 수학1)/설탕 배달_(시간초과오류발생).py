kg_3 = 3
kg_5 = 5

result = 0
result_min = 0

N = int(input())

for kg_5_pcs in range(0, (N // 5) + 1) :
    for kg_3_pcs in range(0, (N // 5) + 1) :
        if (kg_3_pcs * kg_3 + kg_5_pcs * kg_5) == N :
            result_min = kg_3_pcs + kg_5_pcs
        if result == 0 :
            result = result_min
        elif result_min < result :
            result = result_min

if result == 0 :
    print(-1)
else :
    print(result)