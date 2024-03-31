

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

# Menú principal
while True:
    print("\n*** MENÚ ***")
    print("1. Mostrar un libro")
    print("2. Mostrar todos los libros")
    print("3. Añadir un libro")
    print("4. Eliminar un libro")
    print("5. Editar un libro")
    print("6. Salir")
    print("7. Seleccionar otra opción")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_libro()
    elif opcion == "2":
        mostrar_todos_los_libros()
    elif opcion == "3":
        agregar_libro()
    elif opcion == "4":
        eliminar_libro()
    elif opcion == "5":
        editar_libro()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    elif opcion == "7":
        continue
    else:
        print("Opción no válida. Inténtalo de nuevo.")