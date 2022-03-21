import random

numero_aleatorio = random.randrange(101)
boolean_gane = False
print("Tenés 5 intentos para adivinar un entre 0 y 100")
numero_intento = 1
while numero_intento < 6 and not boolean_gane:
    numero_ingresado = int(input('Ingresa tu número: '))
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(numero_intento))
        boolean_gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        numero_intento += 1
if not boolean_gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))