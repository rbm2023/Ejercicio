# ej5

''' Crea una variable que sea una letra, si es una a muestra el número 7,
si es una b, el 9, si es una c el 101
y si no es ninguno de los tres, indica que se han equivocado de letra'''

letra = input(' introduce una letra: ')

if letra == 'a':
    print('7')

else:
    if letra == 'b':
        print('9')

    else:
        if letra == 'c':
            print('101')

        else:
            print('Te has equivocado de letra')

