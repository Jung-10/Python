N = int(input())

for i in range(1, N + 1) :
    print(" " * (N - i), "*" * i, sep = "")

# 문제 : print(1, 2) 이런식으로하면 1과 2 사이에 한 칸 공란이 생김.
# 해결 : sep를 사용하여 공란없이 합쳐서 출력하도록.