import random

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player_choice = input("Ваш выбор (камень, ножницы, бумага): ").strip().lower()
    if player_choice not in ["камень", "ножницы", "бумага"]:
        print("Неверный выбор, попробуйте снова.")
        continue

    computer_choice = random.choice(["камень", "ножницы", "бумага"])
    print(f"Компьютер выбрал: {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
         (player_choice == "ножницы" and computer_choice == "бумага") or \
         (player_choice == "бумага" and computer_choice == "камень"):
        player_score += 1
        print("Вы выиграли раунд!")
    else:
        computer_score += 1
        print("Компьютер выиграл раунд!")

    print(f"Счёт: Игрок {player_score} - {computer_score} Компьютер\n")

if player_score == 3:
    print("Вы победили!")
else:
    print("Компьютер победил!")
