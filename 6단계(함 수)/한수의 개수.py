def hansu(n):
    sum = 0

    if n < 100 :
        return n
    else :
        for i in range(100, (n + 1)) :
            if (((i % 100) // 10) - (i // 100)) == ((i % 10) - ((i % 100) // 10)):
                sum += 1
        return(99 + sum)


num = int(input())
result = hansu(num)
print(result)


# 숫자가 한자리수이거나 두자리수이면 모두 한수.
# 100이후의 세자리수부터는 각 자리 수를 비교해 한수인지 아닌지 판단.
# 따라서 100 이후면 무조건 99까지는 한수니까 이후의 한수의 개수에 99를 더해줘야함.