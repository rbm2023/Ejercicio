#Ej1
n1 = int(input('Introduce el primer numero:'))
n2 = int(input('Introduce el segundo:'))
n3 = int(input('Introduce el tercero:'))

if n1 > n2 and n1 > n3:
    print(str(n1) + ' Es el mayor')

if n2 > n1 and n2 > n3:
    print(str(n2) + ' Es el mayor')

if n3 > n1 and n3 > n2:
    print(str(n3) + ' Es el mayor')