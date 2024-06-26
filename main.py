
def iniciar_sesion():
  nombre_usuario = input("Ingrese su nombre de usuario: ")
  contraseña = input("Ingrese su contraseña: ")
  list = []
  with open("Usuaris.txt", "r") as file:
  
    
    for line in file:
      list = line.strip().split(',')
      if list[0] == nombre_usuario and list[1] == contraseña:
        print("Inicio de sesión exitoso")
        break
      else: 
        print("Nombre de usuario o contraseña incorrectos.")


iniciar_sesion()

def menu():
    print("Bienvenido al menú principal")
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
    def mostrar_libro():
        titulo = input("Introduce el título del libro que deseas mostrar: ")
        with open("Llibrest.txt", "r") as file:
            for line in file:
                guardado = line.strip().split(',')
                if guardado[0] == titulo: 
                  print("Título:", guardado[0])
                  print("Autores:", guardado[1])
                  print("Año de Publicación:", guardado[2])
                  print("Genero:", guardado[3])
                  print("ISBN:", guardado[4])
                  break
            else:
                print("El libro no está en la lista.")
    mostrar_libro()
  elif opcion == "2":
    def mostrar_todos_los_libros():
        print("Mostrando todos los libros:")
        with open("Llibrest.txt", "r") as file:
            for line in file:
                print(line)

    mostrar_todos_los_libros()

  elif opcion == "3":
    def agregar_libro():
        titulo = input("Introduce el título del libro que deseas agregar: ")
        autores = input("Introduce los autores del libro: ")
        año_publicacion = input("Introduce el año de publicación del libro: ")
        genero = input("Introduce el género del libro: ")
        isbn = input("Introduce el ISBN del libro: ")
        with open("Llibrest.txt", "a") as file:
            file.write(f"{titulo},{autores},{año_publicacion},{genero},{isbn}\n")

    agregar_libro()
  elif opcion == "4":
    def eliminar_libro():
        titulo = input("Introduce el título del libro que deseas eliminar: ")  
        with open("Llibrest.txt", "r") as file:
            lines = file.readlines()
        with open("Llibrest.txt", "w") as file:
            for line in lines:
                guardado = line.strip().split(',')
                if guardado[0] != titulo:
                    file.write(line)
    eliminar_libro()
  elif opcion == "5":
    def editar_libro():
        titulo = input("Introduce el título del libro que deseas editar: ")
        with open("Llibrest.txt", "r") as file:
            lines = file.readlines()

        with open("Llibrest.txt", "w") as file:
            for line in lines:
                guardado = line.strip().split(',')
                if guardado[0] == titulo:
                    print("Libro encontrado:")
                    print("Título:", guardado[0])
                    print("Autores:", guardado[1])
                    print("Año de Publicación:", guardado[2])
                    print("Género:", guardado[3])
                    print("ISBN:", guardado[4])

                    nuevo_titulo = input("Introduce el nuevo título del libro: ")
                    nuevos_autores = input("Introduce los nuevos autores del libro: ")
                    nuevo_año_publicacion = input("Introduce el nuevo año de publicación del libro: ")
                    nuevo_genero = input("Introduce el nuevo género del libro: ")
                    nuevo_isbn = input("Introduce el nuevo ISBN del libro: ")

                    
                    line = f"{nuevo_titulo},{nuevos_autores},{nuevo_año_publicacion},{nuevo_genero},{nuevo_isbn}\n"
                file.write(line)

    editar_libro()

          
  elif opcion == "6":
    print("¡Hasta luego!")
    break
  elif opcion == "7":
    continue
  else:
    print("Opción no válida. Inténtalo de nuevo.")


menu()

