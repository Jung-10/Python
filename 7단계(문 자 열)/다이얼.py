word = list(input().lower())
time = 0

for i in word :
    if i == "a" or i == "b" or i == "c" :
        time += 3
    elif i == "d" or i == "e" or i == "f" :
        time += 4
    elif i == "g" or i == "h" or i == "i" :
        time += 5
    elif i == "j" or i == "k" or i == "l" :
        time += 6
    elif i == "m" or i == "n" or i == "o" :
        time += 7
    elif i == "p" or i == "q" or i == "r" or i == "s" :
        time += 8
    elif i == "t" or i == "u" or i == "v" :
        time += 9
    elif i == "w" or i == "x" or i == "y" or i == "z" :
        time += 10

print(time)


# 1이면 2초, 2부터는 +1초씩.