lista_nombres = []
lista_edades = []
lista_obras_sociales = []
lista_tipo_de_consulta = []
lista_valores_de_consulta = []

lista_de_tipos_de_consulta_disponibles = ["Consulta médica general", "Consulta psicológica", "Consulta de prevención"]
valor_consulta_medica_general = 15000
valor_consulta_psicologica = 20000
valor_consulta_de_prevencion = 25000

costo_adicional_por_no_tener_obra_social = 10000

lista_de_obras_sociales_disponibles = ["Osde", "Swiss Medical", "Medicus", "Pami", "Dosuba", "Particular"]


def ordenar_por_valor_de_consulta(lista_datos_de_pacientes):

    for i in range(len(lista_datos_de_pacientes)):
        for j in range(0, len(lista_datos_de_pacientes) - i - 1):
            if lista_datos_de_pacientes[j][4] > lista_datos_de_pacientes[j + 1][4]:
                lista_datos_de_pacientes[j], lista_datos_de_pacientes[j + 1] = lista_datos_de_pacientes[j + 1], lista_datos_de_pacientes[j]

def mostrar_datos_cargados():
    lista_datos_de_pacientes = []

    for i in range(len(lista_nombres)):
        lista_datos_de_pacientes.append((lista_nombres[i], lista_edades[i], lista_obras_sociales[i], lista_tipo_de_consulta[i], lista_valores_de_consulta[i]))


    ordenar_por_valor_de_consulta(lista_datos_de_pacientes)

    # Se imprime la lista de todos los pacientes ordenados por valor de consulta (de menor a mayor)
    print("Lista de pacientes ordenada por orden de consulta: ")
    for i in range(len(lista_nombres)):
        print("-------------------------")
        print("Nombre:", lista_datos_de_pacientes[i][0])
        print("Edad:", lista_datos_de_pacientes[i][1])
        print("Obra social:", lista_datos_de_pacientes[i][2])
        print("Tipo de consulta realizada:", lista_datos_de_pacientes[i][3])
        print("Costo de la consulta: $", lista_datos_de_pacientes[i][4])
    
    print("------------------------------------------------------------------------------------")
    print()

    # Corroboración de que las listas siguen siendo paralelas
    print("Corroboración de que las listas siguen siendo paralelas (no ordenadas): ")
    for i in range(len(lista_nombres)):
        print("-------------------------")
        print("Nombre:", lista_nombres[i])
        print("Edad:", lista_edades[i])
        print("Obra social:", lista_obras_sociales[i])
        print("Tipo de consulta realizada:", lista_tipo_de_consulta[i])
        print("Costo de la consulta: $", lista_valores_de_consulta[i])
    
    print()
        

def registrar_paciente():
    registrar_otro_paciente = input("¿Quiere registrar otro paciente? Ingrese sí o no: ")

    if registrar_otro_paciente.capitalize() == "Si" or registrar_otro_paciente.capitalize() == "Sí":
        main()
    else:
        mostrar_datos_cargados()
        quit()


def calcular_costo_de_consulta(obra_social, valor_de_tipo_de_consulta):

    if obra_social == "Particular":
        valor_de_la_consulta = valor_de_tipo_de_consulta + costo_adicional_por_no_tener_obra_social
        return valor_de_la_consulta
    else:
        valor_de_la_consulta = valor_de_tipo_de_consulta
        return valor_de_la_consulta


def buscar_y_asociar_tipo_de_consulta(tipo_de_consulta, obra_social):
    match tipo_de_consulta:
        case 1:
            lista_tipo_de_consulta.append("Consulta médica general")
            valor_de_la_consulta = calcular_costo_de_consulta(obra_social, valor_consulta_medica_general)
            lista_valores_de_consulta.append(valor_de_la_consulta)
        case 2:
            lista_tipo_de_consulta.append("Consulta psicológica")
            valor_de_la_consulta = calcular_costo_de_consulta(obra_social, valor_consulta_psicologica)
            lista_valores_de_consulta.append(valor_de_la_consulta)
        case 3:
            lista_tipo_de_consulta.append("Consulta de prevención")
            valor_de_la_consulta = calcular_costo_de_consulta(obra_social, valor_consulta_de_prevencion)
            lista_valores_de_consulta.append(valor_de_la_consulta)


def actualizar_nombre(posicion_de_paciente):
    nombre_actualizado = input("Ingrese un nombre para reemplazar al nombre existente: ")

    while nombre_actualizado.isdigit():
        print("El nombre ingresado no es válido. Intente de nuevo.")
        nombre_actualizado = input("Ingrese un nombre para reemplazar al nombre existente: ")

    nombre_ya_registrado = False

    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_actualizado:
            nombre_ya_registrado = True
            break
                    
    while nombre_ya_registrado == True:
        nombre_ya_registrado = False
        print("Nombre ya registrado")
        nombre_actualizado = input("Ingrese un nombre para reemplazar al nombre existente: ")
        for i in range(len(lista_nombres)):
            if lista_nombres[i] == nombre_actualizado:
                nombre_ya_registrado = True
                break
                        
    lista_nombres[posicion_de_paciente] = nombre_actualizado
    registrar_paciente()


def actualizar_edad(posicion_de_paciente):

    edad_valida = False

    while edad_valida == False:
        try:
            edad_actualizada = int(input("Ingrese una edad para reemplazar a la edad existente: "))

            while edad_actualizada < 18 or edad_actualizada > 100:
                print("Edad no válida")
                edad_actualizada = int(input("Ingrese una edad para reemplazar a la edad existente: "))

            edad_valida = True
            
        except ValueError:
            print("El valor ingresado no es válido. Intente de nuevo.")

    lista_edades[posicion_de_paciente] = edad_actualizada
    registrar_paciente()


def actualizar_obra_social(posicion_de_paciente):
    obra_social_actualizada = input("Ingrese una obra social para reemplazar a la obra social existente (" + lista_obras_sociales[posicion_de_paciente] + "): ")

    while obra_social_actualizada.capitalize() not in lista_de_obras_sociales_disponibles or obra_social_actualizada.capitalize() == lista_obras_sociales[posicion_de_paciente]:
        print("La obra social no es válida o es la misma que ya está registrada.")
        obra_social_actualizada = input("Ingrese una obra social para reemplazar a la obra social existente (" + lista_obras_sociales[posicion_de_paciente] + "): ")
            
    lista_obras_sociales[posicion_de_paciente] = obra_social_actualizada.capitalize()
    registrar_paciente()


def actualizar_tipo_de_consulta(posicion_de_paciente):

    es_el_tipo_de_consulta_valido = False

    while es_el_tipo_de_consulta_valido == False:
        try:
            print("1. Consulta médica general")
            print("2. Consulta psicológica")
            print("3. Consulta de prevención")
            numero_de_tipo_de_consulta_actualizada = int(input("Ingrese un tipo de consulta para reemplazar al tipo de consulta ya existente (" + lista_tipo_de_consulta[posicion_de_paciente] + "): "))

            while numero_de_tipo_de_consulta_actualizada < 1 or numero_de_tipo_de_consulta_actualizada > len(lista_de_tipos_de_consulta_disponibles):
                print("El valor ingresado no es válido.")
                print("1. Consulta médica general")
                print("2. Consulta psicológica")
                print("3. Consulta de prevención")
                numero_de_tipo_de_consulta_actualizada = int(input("Ingrese un tipo de consulta para reemplazar al tipo de consulta ya existente (" + lista_tipo_de_consulta[posicion_de_paciente] + "): "))
            
            es_el_tipo_de_consulta_valido = True
            
        except ValueError:
            print("El valor ingresado no es un un número")

    tipo_de_consulta_actualizada = lista_de_tipos_de_consulta_disponibles[numero_de_tipo_de_consulta_actualizada - 1]
                
    lista_tipo_de_consulta[posicion_de_paciente] = tipo_de_consulta_actualizada

    valor_de_consulta_actualizada = 0

    buscar_y_asociar_tipo_de_consulta(numero_de_tipo_de_consulta_actualizada, lista_obras_sociales[posicion_de_paciente])

    lista_valores_de_consulta[posicion_de_paciente] = valor_de_consulta_actualizada
    registrar_paciente()


def actualizar_datos_del_paciente(nombre, tipo_de_dato_a_actualizar):
    posicion_de_paciente = lista_nombres.index(nombre)
                
    match tipo_de_dato_a_actualizar:
        case 1:
            actualizar_nombre(posicion_de_paciente)

        case 2:
            actualizar_edad(posicion_de_paciente)
        
        case 3:
            actualizar_obra_social(posicion_de_paciente)
        
        case 4:
            actualizar_tipo_de_consulta(posicion_de_paciente)


def main():

    nombre = input("Ingrese su nombre: ")

    while nombre.isdigit():
        print("El nombre ingresado no es válido. Intente de nuevo")
        nombre = input("Ingrese su nombre: ")

    if nombre in lista_nombres:
        print("Nombre ya registrado")
        actualizar_registro = input("Desea actualizar el registro de este nombre? Indique 'Sí' o 'No': ")

        if actualizar_registro.capitalize() == "Si" or actualizar_registro.capitalize() == "Sí":
        
            print("1. Nombre")
            print("2. Edad")
            print("3. Obra social")
            print("4. Tipo de consulta")
            tipo_de_dato_a_actualizar = int(input("Ingrese el número que coincida con el dato que desea actualizar: "))

            actualizar_datos_del_paciente(nombre, tipo_de_dato_a_actualizar)

        else:
            quit()
    
    lista_nombres.append(nombre)

    edad_valida = False

    while edad_valida == False:
        try:
            edad = int(input("Ingrese su edad: "))

            while edad < 18 or edad > 100:
                print("Edad no válida")
                edad = int(input("Ingrese su edad: "))

            edad_valida = True
            
        except ValueError:
            print("El valor ingresado no es válido. Intente de nuevo.")

    lista_edades.append(edad)
    
    obra_social = input("Ingrese su obra social (Si no tiene, ingrese 'particular'): ")
    obra_social = obra_social.capitalize()

    while obra_social.capitalize() not in lista_de_obras_sociales_disponibles:
        print("Obra social no disponible.")
        obra_social = input("Ingrese su obra social (Si no tiene, ingrese 'particular'): ")

    lista_obras_sociales.append(obra_social.capitalize())


    valor_de_la_consulta = 0

    es_el_tipo_de_consulta_valido = False

    while es_el_tipo_de_consulta_valido == False:
        try:
            print("1. Consulta médica general")
            print("2. Consulta psicológica")
            print("3. Consulta de prevención")
            tipo_de_consulta = int(input("Ingrese el número de algún tipo de consulta mencionada previamente: "))

            while tipo_de_consulta < 1 or tipo_de_consulta > len(lista_de_tipos_de_consulta_disponibles):
                print("El valor ingresado no es válido.")
                print("1. Consulta médica general")
                print("2. Consulta psicológica")
                print("3. Consulta de prevención")
                tipo_de_consulta = int(input("Ingrese el número de algún tipo de consulta mencionada previamente: "))
            
            es_el_tipo_de_consulta_valido = True

        except ValueError:
            print("El valor ingresado no es un un número.")

    buscar_y_asociar_tipo_de_consulta(tipo_de_consulta, obra_social)

    mostrar_datos_cargados()
    registrar_paciente()


main()