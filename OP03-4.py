num1 = int(input("Введите начальное число: "))
num2 = int(input("Введите конечное число: "))

print("Чётные числа в данном диапазоне:")
for number in range(num1, num2 + 1):
    if number % 2 == 0:
        print(number)
