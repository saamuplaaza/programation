# import random


# Baraja de 20 números, acertar número aleatorio.

# numAleatorio = random.randint(1, 20)
# while True:
#     try:
#         numUsuario = int(input("Intena adivinar el número escondido (1-20): "))
#     except ValueError:
#         print("Formato no válido.")
#     else:
#         if numUsuario>20 or numUsuario<1:
#             print("Número fuera del rango.")
#         elif numUsuario == numAleatorio:
#             print("ENHORABUENA, ¡¡¡HAS ACERTADO!!!")
#             break
#         else:
#             print("Número incorrecto, inténtalo otra vez.")


# Factorial de un número.
num=int(input("Indica el número para hacer factorial: "))
factorial=1
for x in range(num, 0, -1):
    factorial*=x
print("%s! = %s" %(num, factorial))
