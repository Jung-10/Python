while True:
    try :
        A, B = map(int, input().split())
        print(A + B)
    except :
        break
# try except문은 try를 하다가 오류가 발생하면 except문 쪽으로 넘어감.
# 어떤 오류인지 정하지 않았기 때문에 except 기능 뒷쪽에 따로 오류문을 추가하지않아도 됨.