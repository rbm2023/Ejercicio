#Ejercicio 3

print("Ejercicio 3 sumar /restar reales solicitados")

x1 = float(input(' introduce un numero: '))
x2 = float(input('introduce otro numero: '))

op1= 'suma'
op2= 'resta'

opx = input('suma o resta?: ')

if opx==op1:
    print(x1 + x2)

if opx==op2:
    print(x1 - x2)
