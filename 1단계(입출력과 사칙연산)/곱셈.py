A = int(input(""))
B = int(input(""))

sum1 = A * (B % 10)
sum2 = A * ((B % 100) // 10)
sum3 = int((A * (B - (B % 100))) / 100)

sum2_2 = A * ((B % 100) - (B % 10))
sum3_2 = A * (B - (B % 100))

print(sum1)
print(sum2)
print(sum3)
print(sum1 + sum2_2 + sum3_2)
