word = list(input().lower())

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

result = []

sum = 0

for i in alphabet :
    result.append(word.count(i))
    
for j in alphabet :
    if max(result) == word.count(j) :
        sum += 1

if sum == 1 :
    for x in alphabet :
        if max(result) == word.count(x) :
            print(x.upper())
else :
    print("?")

# 대문자로 변환하는 함수가 upper()임.

# 첫번째 제출에서 틀린 이유 : 
# input을 받은 것에서 대소문자 구분을 못하게해서
# 해결 : 1번째 줄에서 input으로 받은 것을 모두 lower() 함수를 사용해서 소문자로 바꿈.