A, B = map(int, input("").split())

if A > B :
    print(">")
elif A < B :
    print("<")
elif A == B:
    print("==")

# int를 사용하지 않아서 체점 결과 오류가 떴음.
# 해결 : map 사용.
# map은 리스트의 요소를 지정된 함수로 처리. 따라서 여기서는 int로 변환시켜줌.