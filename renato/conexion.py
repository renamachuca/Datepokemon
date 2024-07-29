import psycopg2
from psycopg2 import OperationalError

#realizar la conexion a la base de datos
def get_conexion():
    try:
        conn = psycopg2.connect(
            dbname = 'Pokemon',
            user = "postgres",
            password = "penguin",
            host= "localhost",
            port = "5432"
        )
        print("La conexion fue exitosa")
        return conn
    except OperationalError as e:
        print(f"Error de conexion: {e}")
        return None

    # #para liberar recursos y cerrar la conexion
    # finally:
    #     # Cerrar la conexión solo si se ha establecido
    #    if conn is not None and not conn.closed:
    #         conn.close()
    #         print("Conexión cerrada")