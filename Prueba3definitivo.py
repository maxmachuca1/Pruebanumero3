import csv

prestamos = []
docente = "Pablo Saldaña"
codigo_curso = "FDP1101"
numero_seccion = "008D"

def validar_entrada(rut, nombre, documento, numero_notebook):
    if not (rut and nombre and documento and numero_notebook):
        print("Todos los campos son obligatorios.")
        return False
    if not rut.isalnum():
        print("El RUT debe contener solo caracteres alfanuméricos.")
        return False
    return True

def prestar_notebook(rut, nombre, documento, numero_notebook):
    if validar_entrada(rut, nombre, documento, numero_notebook):
        prestamos.append({
            'rut': rut,
            'nombre': nombre,
            'documento': documento,
            'numero_notebook': numero_notebook
        })
        print(f"Notebook {numero_notebook} prestado a {nombre} ({rut}).")
    else:
        print("Error en el préstamo del notebook.")

def devolver_notebook(rut):
    for prestamo in prestamos:
        if prestamo['rut'] == rut:
            prestamos.remove(prestamo)
            print(f"Notebook devuelto por {prestamo['nombre']} ({rut}).")
            return
    print(f"No se encontró un préstamo para el RUT {rut}.")

def modificar_prestamo(rut, nuevo_numero_notebook):
    for prestamo in prestamos:
        if prestamo['rut'] == rut:
            prestamo['numero_notebook'] = nuevo_numero_notebook
            print(f"Préstamo modificado para {rut}, nuevo notebook {nuevo_numero_notebook}.")
            return
    print(f"No se encontró un préstamo para el RUT {rut}.")

def imprimir_prestamos():
    archivo = f"{docente.replace(' ', '_')}_{codigo_curso}_{numero_seccion}.csv"
    with open(archivo, mode='w', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow(['RUT', 'Nombre', 'Documento', 'Número de Notebook'])
        for prestamo in prestamos:
            escritor.writerow([prestamo['rut'], prestamo['nombre'], prestamo['documento'], prestamo['numero_notebook']])
    print(f"La lista de préstamos se ha guardado en {archivo}.")

def finalizar_clase():
    if not prestamos:
        print("Clase terminada. Todos los notebooks han sido devueltos.")
    else:
        print("No se puede terminar la clase, aún hay notebooks sin devolver:")
        for prestamo in prestamos:
            print(f"Notebook {prestamo['numero_notebook']} no ha sido devuelto por {prestamo['nombre']} ({prestamo['rut']}).")

def menu_prestamos():
    global prestamos, docente, codigo_curso, numero_seccion
    prestamos = []

    opciones = {
        '1': "Prestar notebook",
        '2': "Devolver notebook",
        '3': "Modificar préstamo",
        '4': "Imprimir lista de préstamos",
        '5': "Finalizar clase",
        '6': "Salir"
    }

    while True:
        print("\nMenú de préstamos:")
        for key, value in opciones.items():
            print(f"{key}. {value}")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            rut = input("Ingrese el RUT (solo caracteres alfanuméricos): ")
            nombre = input("Ingrese el nombre: ")
            documento = input("Ingrese el documento: ")
            numero_notebook = input("Ingrese el número del notebook: ")
            prestar_notebook(rut, nombre, documento, numero_notebook)

        elif opcion == '2':
            rut = input("Ingrese el RUT: ")
            devolver_notebook(rut)

        elif opcion == '3':
            rut = input("Ingrese el RUT: ")
            nuevo_numero_notebook = input("Ingrese el nuevo número del notebook: ")
            modificar_prestamo(rut, nuevo_numero_notebook)

        elif opcion == '4':
            imprimir_prestamos()

        elif opcion == '5':
            finalizar_clase()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")

menu_prestamos()
