word = list(input())
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
result = []

for i in range(0, len(alphabet)) :
    result.append(-1)

for j in range(0, len(alphabet)) :
    for k in range(0, len(word)) :
        if alphabet[j] == word[k] and result[j] == -1:
            result[j] = k
 
for x in result :
    print(x, end = " ")


# 문제 해석
# 예를 들어서 baekjoon이면
# a b c d e f g . . . . z
# 1 0 -1 -1 2 -1 -1 . . . . -1
# 알파벳 각각이 해당 단어의 몇 번째에 위치하는지를 결과로 출력하는 것임.
# 대신 첫번째를 1이라고 하지않고 0부터 시작함.

# end = " "를 사용해서 출력 방식을 변경할 수 있음.

# 첫번째 제출에서 틀린 이유 : 
# baekjoon처럼 o가 중복되는 경우 처음에 -1이 5로 바뀌고 뒤에 있는 o로 인해서 5가 6으로 바뀜.
# 해결 : 10번째 줄의 조건에 result[j] == -1을 추가해서 -1인 경우에만 바뀌도록 수정.
