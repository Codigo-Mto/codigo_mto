# librerias para realizar la coneccion con la bse de datos
from mysql import connector

from database.connection import create_connection

###################
# Insertar datos en la tabla maquinas del mysql
def insert(data):
    conn = create_connection()

    sql = """INSERT INTO maquina(NOMBRE_MAQUINA,SECCION, AREA,img_path,url_manual)


            VALUES(%s, %s, %s, %s, %s)
            """
    cur = conn.cursor()
    # conecta la sintaxis del sql y lo inserta en un vector data
    cur.execute(sql, data)
    conn.commit()
    
    cur.close()
    conn.close()

############################
# insertar datos en la tabla proveedor del mysql
def insert_proveedor(data):
    conn = create_connection()

    sql = """INSERT INTO proveedor(EMPRESA,PERSONA_DE_CONTACTO, DIRECCION,CORREO_ELECTRONICO,TELEFONO,PAGINA_WEB, TIPO_PROVEEDOR)


            VALUES(%s, %s, %s, %s, %s, %s, %s)
            """
    
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    
    cur.close()
    conn.close()
    
############################
# insertar datos en la tabla personal del mysql
def insert_personal(data):
    conn = create_connection()

    sql = """INSERT INTO personal(NOMBRE,TELEFONO,DIRECCION,CARGO,ESPECIALIDAD,FECHA_DE_NACIMIENTO,img_path)


            VALUES(%s, %s, %s, %s, %s, %s, %s)
            """
    
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    
    cur.close()
    conn.close()
############################
# insertar datos en la tabla repuestos

def insert_repuestos(data):
    conn = create_connection()

    sql = """INSERT INTO repuestos(NOMBRE_REPUESTO, CODIGO_REPUESTO, TIPO_REPUESTO, PRECIO, CANTIDAD, LEAD_TIME,img_path)


            VALUES(%s, %s, %s, %s, %s, %s, %s)
            """
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    
    cur.close()
    conn.close()


##############
# seleccionar datos de la base de datos, tabla maquinas
def select_all():
    conn = create_connection()
    sql = """SELECT ID,img_path,AREA,SECCION,NOMBRE_MAQUINA,url_manual FROM maquina """
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        maquina = cur.fetchall()
        return maquina
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

######################
# seleccionar datos de la base de datos, tabla proveedor
def select_all_proveedro():
    conn = create_connection()
    sql = """SELECT ID,EMPRESA,PERSONA_DE_CONTACTO,DIRECCION,CORREO_ELECTRONICO,TELEFONO,PAGINA_WEB FROM proveedor """
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        maquina = cur.fetchall()
        return maquina
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

######################
# seleccionar datos de la base de datos, tabla personal
def select_all_personal():
    conn = create_connection()
    sql = """SELECT ID,img_path,NOMBRE,TELEFONO,DIRECCION,CARGO,ESPECIALIDAD,FECHA_DE_NACIMIENTO FROM personal """
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        maquina = cur.fetchall()
        return maquina
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


######################
# seleccionar datos de la base de datos, tabla repuestos
def select_all_respuestos():
    conn = create_connection()
    sql = """SELECT ID,img_path,NOMBRE_REPUESTO,CODIGO_REPUESTO,TIPO_REPUESTO,PRECIO,CANTIDAD,LEAD_TIME FROM repuestos """
    
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        maquina = cur.fetchall()
        return maquina
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


###############
# seleccionar datos segun el ID de la base de datos, tabla maquinas
def select_by_id(_id):

    conn = create_connection()
    sql = f"""SELECT *FROM maquina WHERE id = {_id} """
    print("asdsad",_id)
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        maquina = cur.fetchone()
        return maquina
    except connector.Error as err:
        print(f"Error at select_by_id function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
##############
# seleccionar datos segun el ID de la base de datos, tabla proveedor
def select_by_id_proveedor(_id):

    conn = create_connection()
    sql = f"""SELECT *FROM proveedor WHERE id = {_id} """
    print("asdsad",_id)
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        maquina = cur.fetchone()
        return maquina
    except connector.Error as err:
        print(f"Error at select_by_id function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

##############
# seleccionar datos segun el ID de la base de datos, tabla personal
def select_by_id_personal(_id):

    conn = create_connection()
    sql = f"""SELECT *FROM personal WHERE id = {_id} """
    print("asdsad",_id)
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        maquina = cur.fetchone()
        return maquina
    except connector.Error as err:
        print(f"Error at select_by_id function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
###########################
# seleccionar datos segun el ID de la base de datos, tabla repuestos
def select_by_id_repuestos(_id):

    conn = create_connection()
    sql = f"""SELECT *FROM repuestos WHERE id = {_id} """
    print("asdsad",_id)
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        maquina = cur.fetchone()
        return maquina
    except connector.Error as err:
        print(f"Error at select_by_id function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

###########################        
# actualizar datos de la tabla maquina
def update(_id, data):
    conn = create_connection()
    sql = f"""UPDATE maquina SET 
                                
                                NOMBRE_MAQUINA =%s,
                                SECCION =%s, 
                                AREA =%s,
                                url_manual =%s 
                                img_path =%s,
                                
                WHERE ID = {_id}
                """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

###########################   
# actualizar datos de la tabla personal
def update_personal(_id, data):
    conn = create_connection()
    sql = f"""UPDATE personal SET 
                                
                                NOMBRE =%s,
                                TELEFONO =%s, 
                                DIRECCION =%s,
                                CARGO =%s ,
                                ESPECIALIDAD =%s,
                                FECHA_DE_NACIMIENTO =%s,
                                img_path =%s
                                
                WHERE ID = {_id}
                """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

###########################   
# actualizar datos de la tabla proveedor
def update_proveedor(_id, data):
    conn = create_connection()
    sql = f"""UPDATE proveedor SET 
                                
                                EMPRESA =%s,
                                PERSONA_DE_CONTACTO =%s, 
                                DIRECCION =%s,
                                CORREO_ELECTRONICO =%s,
                                TELEFONO =%s,
                                PAGINA_WEB =%s,
                                TIPO_PROVEEDOR =%s
                                
                WHERE ID = {_id}
                """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

###########################   
# actualizar datos de la tabla repuestos
def update_repuesto(_id, data):
    conn = create_connection()
    sql = f"""UPDATE repuestos SET 
                                
                                NOMBRE_REPUESTO =%s,
                                CODIGO_REPUESTO =%s, 
                                TIPO_REPUESTO =%s,
                                PRECIO =%s,
                                CANTIDAD =%s,
                                LEAD_TIME =%s,
                                img_path =%s
                                  
                WHERE ID = {_id}
                """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at select_all function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

# seleccionar datos segun el parametro de la tabla maquina
def select_by_parameter(param):
    
    conn = create_connection()
    param = f"%{param}%"
    print("el parametro es",param)
    sql = """SELECT ID,img_path,AREA,SECCION,NOMBRE_MAQUINA,url_manual FROM maquina
            WHERE NOMBRE_MAQUINA LIKE %s OR AREA LIKE %s
    
           """
    try:
        cur = conn.cursor()
        cur.execute(sql,(param,param))
        maquina = cur.fetchall()
        return maquina
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

################
# seleccionar datos segun el parametro de la tabla proveedor
def select_by_parameter_proveedor(param):
    
    conn = create_connection()
    param = f"%{param}%"
    print("el parametro es",param)
    sql = """SELECT ID,EMPRESA,PERSONA_DE_CONTACTO,DIRECCION,CORREO_ELECTRONICO,TELEFONO,PAGINA_WEB,TIPO_PROVEEDOR FROM proveedor
            WHERE EMPRESA LIKE %s OR PERSONA_DE_CONTACTO LIKE %s
    
           """
    try:
        cur = conn.cursor()
        cur.execute(sql,(param,param))
        maquina = cur.fetchall()
        return maquina
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
#############
################
# seleccionar datos segun el parametro de la tabla personal
def select_by_parameter_personal(param):
    
    conn = create_connection()
    param = f"%{param}%"
    print("el parametro es",param)
    sql = """SELECT ID,img_path,NOMBRE,TELEFONO,DIRECCION,CARGO,ESPECIALIDAD,FECHA_DE_NACIMIENTO FROM personal
            WHERE NOMBRE LIKE %s OR ESPECIALIDAD LIKE %s
    
           """
    try:
        cur = conn.cursor()
        cur.execute(sql,(param,param))
        maquina = cur.fetchall()
        return maquina
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
######
# seleccionar datos segun el parametro de la tabla repuestos
def select_by_parameter_repuestos(param):
    
    conn = create_connection()
    param = f"%{param}%"
    print("el parametro es",param)
    sql = """SELECT ID,img_path,NOMBRE_REPUESTO,CODIGO_REPUESTO,TIPO_REPUESTO,PRECIO,CANTIDAD,LEAD_TIME FROM repuestos
            WHERE NOMBRE_REPUESTO LIKE %s OR CODIGO_REPUESTO LIKE %s
    
           """
    try:
        cur = conn.cursor()
        cur.execute(sql,(param,param))
        maquina = cur.fetchall()
        return maquina
    except connector.Error as err:
        print(f"Error at select_by_param function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


##############
# Eliminar datos de la tabla maquina
def delete(_id):

    conn = create_connection()
    sql = f""" DELETE FROM maquina
                WHERE ID = {_id}
                """
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

###################
# Eliminar datos de la tabla proveedor
def delete_proveedor(_id):

    conn = create_connection()
    sql = f""" DELETE FROM proveedor
                WHERE ID = {_id}
                """
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

###################
# Eliminar datos de la tabla personal
def delete_personal(_id):

    conn = create_connection()
    sql = f""" DELETE FROM personal
                WHERE ID = {_id}
                """
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

###################
# Eliminar datos de la tabla repuestos
def delete_repuestos(_id):

    conn = create_connection()
    sql = f""" DELETE FROM repuestos
                WHERE ID = {_id}
                """
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()