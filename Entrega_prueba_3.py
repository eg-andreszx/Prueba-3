

print("=====Bienvenido al cine Duoc Uc======")
nombre = (input("  Ingrese su nombre y apellido:  "))


#soy feliz con un 4 :)

#SORRY PROFE, NO ME ACORDABA BIEN DE COMO HACER LA MATRIZ :(

peliculas = ["Super Mario Bros 2D"]
asientos = [
    ['A1', 'A2', 'A3', 'A4', 'A5',"A6","A7","A8","A9","A10","A11","A12","A13","A14","A15"],
    ['B1', 'B2', 'B3', 'B4', 'B5',"B6","B7","B8","B9","B10","B11","B12","B13","B14","B15"],
    ['C1', 'C2', 'C3', 'C4', 'C5',"C6","C7","C8","C9","C10","C11","C12","C13","C14","C15"],
    ['D1', 'D2', 'D3', 'D4', 'D5',"D6","D7","D8","D9","D10","D11","D12","D13","D14","D15"],
    ['E1', 'E2', 'E3', 'E4', 'E5',"E6","E7","E8","E9","E10","E11","E12","E13","E14","E15"],
    ['F1', 'F2', 'F3', 'F4', 'F5',"F6","F7","F8","F9","F10","F11","F12","F13","F14","F15"],
    ['G1', 'G2', 'G3', 'G4', 'G5',"G6","G7","G8","G9","G10","G11","G12","G13","G14","G15"],
    ['H1', 'H2', 'H3', 'H4', 'H5',"H6","H7","H8","H9","H10","H11","H12","H13","H14","H15"],
    ['I1', 'I2', 'I3', 'I4', 'I5',"I6","I7","I8","I9","I10","I11","I12","I13","I14","I15"]]
    


def mostrar_menu():
    print("^============================^")
    print("|   Bienvenido al cine Duoc  |")
    print("|[1] Ver lista de películas  |")
    print("|[2] Seleccionar película    |")
    print("|[3] Seleccionar asiento     |")
    print("|[4] Ver asientos disponibles|")
    print("|[5] Salir                   |")
    print("^============================^")


def asientos_disponibles ():    #los asientos que estan disponibles, que los recorra y que si se tiene uno tomado se le cambie por una x
    print("=== Asientos Disponibles ===")
    for fila in asientos:
        for asiento in fila:
            print(asiento, end=' ')
        print()
    print("==========================")


def generar_boleta(pelicula, asiento, valor_entrada):
    print("^==========================================^")
    print("|         Cine Duoc                        |")
    print("|   ¡Disfruta tu película!                 |")
    print("^==========================================^")
    print("|cliente:", nombre,                       "|")
    print("|Película:", pelicula,    "                |")
    print("|Asiento:", asiento ,                     "|")
    print("|Valor de la entrada:", valor_entrada,    "|")
    print("|Descuento por Alumno duoc(Opcional): 60%""|")
    print("^==========================================^")

def seleccionar_opcion():
    opcion = 0
    pelicula_seleccionada = ""
 #aca llamo al menu para poder seleccionar una de las opciones que estan en el menu
    while opcion != 5:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            #opciones que me da el menu
            if opcion == 1:
                print("=== Lista de Películas ===")
                
                for i, pelicula in enumerate(peliculas):
                    print(f"{i+1}. {pelicula}")
                print("==========================")

            elif opcion == 2:
                pelicula_seleccionada = int(input("Selecciona el número de película: "))

                if pelicula_seleccionada >= 1 and pelicula_seleccionada <= len(peliculas):

                    pelicula = peliculas[pelicula_seleccionada-1]
                    print(f"Seleccionaste la película: {pelicula}")

                else:
                    print("Opción inválida. Por favor, selecciona nuevamente.")

            elif opcion == 3:
                                     #aca hice un if para que se puedan almacenar los asientos
                if pelicula_seleccionada == "":
                    print("Por favor, selecciona una película antes de elegir un asiento.")

                else:
                    fila = input("Ingresa la fila del asiento: ").upper()
                    columna = input("Ingresa la columna del asiento: ")
                    if fila in ["A", "B", "C", "D", "E","F","G","H","I"] and columna.isdigit() and int(columna) >= 1 and int(columna) <= 15:  
                        asiento = asientos[ord(fila) - ord("A")][int(columna) - 1]
                        print(f"Seleccionaste el asiento: {asiento}")
                        generar_boleta(peliculas[pelicula_seleccionada-1], asiento, 2500)
                    else:
                        print("Asiento inválido. Por favor, selecciona nuevamente.")
            elif opcion == 4:      #no se me ocurrio nada para poder dejar con x el asiento, sorry 
                asientos_disponibles()

            elif opcion == 5:
                print(f"Gracias,{nombre}, vuelva pronto")
            else:
                print("Opción inválida. Por favor, selecciona nuevamente.")
        except ValueError:
            print("Opción inválida. Por favor, selecciona nuevamente.")

seleccionar_opcion()


