
numbers = []
for i in range(3):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)

min_number = numbers[0]

for number in numbers:
    if number < min_number:
        min_number = number

print("Наименьшее число:", min_number)














