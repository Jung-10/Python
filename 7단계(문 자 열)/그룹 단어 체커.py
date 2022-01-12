N = int(input())

for i in range(N) :
    word = input()
    
    if list(word) != sorted(word, key = word.find):
        N -= 1

print(N)


# sorted(word, key = word.find)
# key 매개 변수는 각 리스트 요소에 대해 호출할 함수를 지정