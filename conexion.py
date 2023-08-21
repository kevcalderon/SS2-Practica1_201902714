import pyodbc

def establecer_conexion():
    # Configura los detalles de la conexión
    try:
        server = 'DESKTOP-LBDH6DF\SQLEXPRESS'
        database = 'practica1semi2'
        username = ''
        password = ''
        driver = 'SQL Server'  # El driver puede variar según la versión de SQL Server

        # Crea la cadena de conexión
        connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

        # Establece la conexión
        return  pyodbc.connect(connection_string)
    except pyodbc.Error as err:
        print("error en la conexion", err)


# # Crea un cursor para ejecutar consultas
# cursor = connection.cursor()

# # Ejecuta una consulta
# query = "SELECT * FROM tu_tabla"
# cursor.execute(query)

# # Recupera los resultados
# results = cursor.fetchall()
# for row in results:
#     print(row)

# # Cierra la conexión
# cursor.close()
# connection.close()