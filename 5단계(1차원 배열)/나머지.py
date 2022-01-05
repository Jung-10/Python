result = []

for i in range(0, 10):
    num = int(input())
    num = num % 42
    result.append(num)
    
result = set(result)

print(len(result))

# set : set 함수를 사용하여 집합 타입으로 변환시킬 수 있음.
# 집합은 중복된 원소가 없기 때문에 사용.

# len을 사용해서 원소의 개수를 세는데 사용가능.