def comprueba(range):
    if range > 0 & range <= 20:
        print("Dentro del rango")
        return True
    else:
        print("Fuera del rango")
        return False

def busqueda(num, num_list):
    if num in num_list:
        print("Número encontrado.")
        return True
    else:
        print("Número no encontrado.")
        return False

lista_numeros = [6, 14, 11, 3, 2, 1, 15, 19]

numero = int(input("Dame un número válido del 1 al 20 y te diré si ese número está en mi lista: "))

comprueba(numero)
busqueda(numero, lista_numeros)
