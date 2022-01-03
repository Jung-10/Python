H, M = map(int, input("").split())

if H != 0 and 0 <= M < 45 :
    H = H - 1
    M = 60 + (M - 45)
    print(H, M)
elif H != 0 and M >= 45 :
    M = M - 45
    print(H, M)
elif H == 0 and 0 <= M < 45 :
    H = 23
    M = 60 + (M - 45)
    print(H, M)
elif H == 0 and M >= 45 :
    M = M - 45
    print(H, M)

# 분끼리 빼고 음수면 시간을 1을 빼고 양수면 그냥 출력.
# 시간 0이면 23으로