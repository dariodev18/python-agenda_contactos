def mostrar_menu():
    print("\nAgenda de Contactos:" )
    print("1. Agregar Nuevo Contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")
    
def agregar_contacto(agenda):
    nombre = input("Por favor Ingrese el nombre completo del contacto: ")
    telefono = input("Por favor Ingrese el telefono del contacto: ")
    email = input("Por favor Ingrese el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"Se ha agregado el contacto {nombre} exitosamente!")
    
def eliminar_contacto(agenda):
    nombre = input("Por favor Ingrese el nombre de la agenda que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Se ha eliminado el contacto {nombre} exitosamente!")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que esta buscando: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")    
        print(f"Telefono: {agenda[nombre]['telefono']}")    
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")
        
def listar_contactos(agenda):
    if agenda:
        print("\nLista de Contactos: ")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info['telefono']}")
            print(f"Email: {info['email']}")
            print("-" *20)
    else:
        print("La agenda aun esta vacia!")
    
def agenda_contactos():
    agenda = {}
    
    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opcion: ")
        print("\n")
        
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Gracias por usar la agenda de contactos")
            break
        else:
            print("Opcion invalida, por favor elija una opcion valida")

agenda_contactos()        