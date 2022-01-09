all_num = set(range(1, 10001))
generated_num = set()

for i in all_num :
    for j in str(i) :
        i += int(j)
    generated_num.add(i)

self_num = sorted(all_num - generated_num)

for x in self_num :
    print(x)






