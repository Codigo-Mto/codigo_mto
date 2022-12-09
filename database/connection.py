# libreria para realizar la conexion de la base de datos y python
from mysql import connector

# configuracion de los datos de la base de datos
config = {
    'user': 'root',
    'password': 'gabriel987',
    'host': 'localhost',
    'database': 'mantenimiento_db'
}
# funcion que realiza la conexion entre la base de datos y python
def create_connection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Error at create_connection function: {err.msg}" )
    return conn