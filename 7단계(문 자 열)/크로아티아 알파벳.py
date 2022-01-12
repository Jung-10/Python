word = input()
alphbet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alphbet :
    word = word.replace(i, "!")

print(len(word))

# replace 함수는 문자열 내 원하는 문자 변경이 가능