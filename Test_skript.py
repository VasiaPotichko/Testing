from random import randint

while True:
    username = input("Пожалуйста введите свое имя -  ")
    randigit = randint(1, 101) # случайное число

    print(f"Привет {username}! твое случайное число: {randigit}")

    if username == "пожалуйста хватит":
        break 
