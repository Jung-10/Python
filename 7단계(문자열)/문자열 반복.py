N = int(input())
re_str = []
result = []

for i in range(N) :
    all_input = list(input().split(" "))
    re_str = list(all_input[1])

    repeat = int(all_input[0])

    for j in range(0, len(re_str)) :
        result.append(repeat * re_str[j])

    print(''.join(result))
    re_str = []
    result = []


