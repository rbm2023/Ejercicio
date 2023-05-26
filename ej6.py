#Ejercicio 6

'''Dispones de tres números enteros H, M, S correspondientes a hora,
minutos y segundos respectivamente, debes comprobar si se
trata de una hora válida.'''


entrada=False
contador=0

while entrada!=True:
    H = int(input('introduce la hora:'))
    M = int(input('introduce los minutos: '))
    S = int(input('Introduce los segundos: '))
    while contador<=5:

        if H<=24 and M<=60 and S<=60:
            print('la hora es correcta')
            entrada=True
        else:
            print('Vuelve a intentarlo')
            contador+=1
            #break