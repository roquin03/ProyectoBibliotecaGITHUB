

usuarios = {}

def registrar_usuario():
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    contraseña = input("Ingrese una contraseña: ")

   
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya existe. Por favor, elija otro.")
        return

 
    usuarios[nombre_usuario] = contraseña
    print("Usuario registrado exitosamente.")


registrar_usuario()



def iniciar_sesion():

    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

   
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso. ¡Bienvenido,", nombre_usuario, "!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")


iniciar_sesion()