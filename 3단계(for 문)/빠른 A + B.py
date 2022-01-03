import sys

input = sys.stdin.readline
N = int(input())

for i in range(N) :
    A, B = map(int, input().split())
    print(A + B)

# sys.stdin.readline를 사용하려면 import sys해주기