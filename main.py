from conexion import establecer_conexion
import csv

def menuPrincipal():
    con = establecer_conexion()
    
    with open('EntregasUSAC-Delivery.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for index, row in enumerate(csv_reader):
            if index == 0:
                continue
            print("ID:", row[0])
            print("DIA:", row[1])
            print("MES:", row[2])
            print("ANIO", row[3])
            print("---------")
            
    
            

    # print(con)

    # pass   
    # while True:
       
    #     print("")
    #     print("******************************")
    #     print("      PRACTICA 1 - SEMI2      ")
    #     print("******************************")
        
    #     print("1. Borrar modelo")
    #     print("2. Crear modelo")
    #     print("3. Extraer información")
    #     print("4. Cargar información")
    #     print("5. Realizar consultas.")
    #     print("6. Salir")
    #     print(" ")
    #     opcion = input("> Ingrese el numero de la opción: ")

    #     if opcion == "1":

    #         pass
    #     elif opcion == "2":
    #         pass
    #     elif opcion == "3":
    #         pass
    #     elif opcion == "4":
    #         pass
    #     elif opcion == "5":
    #         pass
    #     elif opcion == "6":
            
    #         break
    #     else:
    #         print("")
    #         print("Opción inválida. Por favor, seleccione una opción válida.")
        



if __name__ == "__main__":
    menuPrincipal()