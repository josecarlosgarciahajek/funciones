from random import randint, uniform, random

num_random = randint(0, 10)

def calcula(rand, num):
    if num == rand:
        print("Número random: ", rand)
        print("Número usuario: ", num)
        print("Has acertado crack!")
    elif rand > num:
        print("Número random: ", rand)
        print("Número usuario: ", num)
        print("El número del programa es más alto.")
    else:
        print("Número random: ", rand)
        print("Número usuario: ", num)
        print("El número del programa es más bajo.")

numero = int(input("Adivina el número. Para ello dame un número: "))

calcula(num_random, numero)