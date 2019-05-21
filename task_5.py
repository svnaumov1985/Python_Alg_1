# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if ((a > b) and (b > c)) or ((a < b) and (b < c)):
    print("Среднее число b")
elif ((b > a) and (a > c)) or ((b < a) and (a < c)):
    print("Среднее число a")
elif ((b > c) and (c > a)) or ((b < c) and (c < a)):
    print("Среднее число с")
else:
    print("Невозможно определить")