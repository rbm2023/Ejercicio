#Ej4 - Permite validar a un usuario con 3
#intentos y los datos de validación correctos almacenados en dos constantes predefinidas.

usuario='ricardo'
contrasena='12345'
contador=0
loguin=True

#or loguin!=False
while contador <= 3:

        user = input('introduce tu usuario: ')
        password = input('introduce tu pass: ')

        if usuario == user and contrasena == password:
            print('usuario y pass correctos')
            loguin=True
            break

        else:
            print('Intentalo de nuevo')
            contador+=1


print('Te has logueado correctamente')