def buscar_paciente():
    pacientes = []
    arch=open('F:/Facultad/Python/trabajo practico/pacientes2.txt', 'r')
    for i in arch:
        num_historia, paciente, prepaga = i.strip().split(',')
        pacientes.append((num_historia, paciente, prepaga))

    consultas = []
    try:
        arch=open('F:/Facultad/Python/trabajo practico/consultas2.txt', 'r')
        for i in arch:
            num_historia, diagnostico, fecha = i.strip().split(',')
            consultas.append((num_historia, diagnostico, fecha))
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    
    nombre_paciente = input("Ingrese el nombre del paciente (todo o parte): ")

    # Buscar pacientes que coincidan con la búsqueda
    pacientes_coincidentes = []
    for paciente in pacientes:
        if nombre_paciente.upper() in paciente[1].upper():
            pacientes_coincidentes.append(paciente)

    if len(pacientes_coincidentes) == 0:
        print("No se encontraron pacientes que coincidan con la búsqueda.")
        return

    # Mostrar listado de pacientes coincidentes
    print("Listado de pacientes coincidentes:")
    for paciente in pacientes_coincidentes:
        print("- Número de Historia Clínica:", paciente[0])
        print("- Nombre del paciente:", paciente[1])
        print("- Prepaga u Obra Social:", paciente[2])
        print()

    # Seleccionar paciente para mostrar historial médico
    num_historia_seleccionado = input("Ingrese el número de Historia Clínica del paciente seleccionado: ")

    historial_medico = []
    for consulta in consultas:
        if consulta[0] == num_historia_seleccionado:
            historial_medico.append((consulta[2], consulta[1]))

    if len(historial_medico) == 0:
        print("El paciente seleccionado no tiene consultas registradas.")
    else:
        historial_medico.sort(key=lambda x: x[0])  # Ordenar por fecha

        print("Historial médico del paciente:")
        print("- Número de Historia Clínica:", num_historia_seleccionado)
        for consulta in historial_medico:
            print("- Fecha:", consulta[0])
            print("- Diagnóstico:", consulta[1])
            print()


def agregar_paciente():
    num_historia = input("Ingrese el número de Historia Clínica: ")
    paciente = input("Ingrese el nombre y apellido del paciente: ")
    prepaga = input("Ingrese la prepaga u Obra Social: ")
    
    try:
        arch=open('F:/Facultad/Python/trabajo practico/pacientes2.txt', 'a')
        arch.write(f"{num_historia},{paciente},{prepaga}\n")
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    return num_historia


def agregar_consulta():
    num_historia = input("Ingrese el número de Historia Clínica: ")
    diagnostico = input("Ingrese el diagnóstico: ")
    fecha = input("Ingrese la fecha (formato AAAAMMDD): ")
    try:
        arch=open('F:/Facultad/Python/trabajo practico/consultas2.txt', 'a')
        arch.write(f"{num_historia},{diagnostico},{fecha}\n")
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

def menu():
    pacientes = []
    while True:
        opcion = input("1. Agregar paciente\n2. Agregar consulta\n3. Salir\nSeleccione una opción: ")
        if opcion == '1':
            agregar_paciente()
        elif opcion == '2':
            agregar_consulta()
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    
    return pacientes


# Programa principal
buscar_paciente()
menu()