lista_nombres = []
lista_edades = []
lista_obras_sociales = []

lista_de_obras_sociales_disponibles = ["Osde", "Swiss Medical", "Medicus", "Pami", "Dosuba", "Particular"]


def mostrar_datos_cargados():
    for i in range(len(lista_nombres)):
        print("Nombre:", lista_nombres[i])
        print("Edad:", lista_edades[i])
        print("Obra social:", lista_obras_sociales[i])
        print("-------------------------")

def main():

    nombre = input("Ingrese su nombre: ")
    nombre = nombre.capitalize()

    while nombre in lista_nombres:
        print("Nombre ya registrado")
        nombre = input("Ingrese su nombre: ")
    
    lista_nombres.append(nombre)

    edad = int(input("Ingrese su edad: "))

    while edad < 18 or edad > 100:
        print("Edad no válida")
        edad = int(input("Ingrese su edad: "))

    lista_edades.append(edad)
    
    obra_social = input("Ingrese su obra social (Si no tiene, ingrese 'particular'): ")
    obra_social = obra_social.capitalize()

    while obra_social not in lista_de_obras_sociales_disponibles:
        print("Obra social no disponible.")
        obra_social = input("Ingrese su obra social (Si no tiene, ingrese 'particular'): ")

    lista_obras_sociales.append(obra_social.capitalize())

    registrar_otro_paciente = input("¿Quiere registrar otro paciente? Ingrese sí o no")
    
    if registrar_otro_paciente.capitalize() == "Si" or registrar_otro_paciente.capitalize() == "Sí":
        main()
    else:
        mostrar_datos_cargados()
        quit()

main()