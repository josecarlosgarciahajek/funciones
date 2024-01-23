def esPrimer(numero):
    for num in range(2, numero):
        if numero % num == 0:
            print("No es primo")
            return False
        else:
            print("Es primo")
            return True
numero_input = int(input("Dame un número y te diré si es primo o no: "))
esPrimer(numero_input)