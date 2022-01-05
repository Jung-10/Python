result = []
big = 0
line = 0

for i in range(0, 9):
    num = int(input())
    result.append(num)
    
    if result[i] < big:
        big = big
        
    elif result[i] > big:
        big = result[i]
        line = i + 1
    
print(big)
print(line)