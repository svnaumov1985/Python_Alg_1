# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input("введите x: "))

x1 = x // 100
x = x - x1 * 100
x2 = x // 10
x = x - x2 * 10
x = x * x1* x2

print("произведение: ", x)