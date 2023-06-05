def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

result = power(A, B)
print(f"{A} в степени {B} равно {result}")
