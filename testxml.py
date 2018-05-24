import lxml.etree as ET
import MySQLdb

c = "banco.xslt"

# BD
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'root'
DB_NAME = 'banco'

# Funciones

def transform_xml (a, b):
    dom = ET.parse(a)
    xslt = ET.parse(c)
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    text_file = open(b, "wb")
    text_file.write(ET.tostring(newdom, pretty_print=True))
    text_file.close()


def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    cursor.execute(query)  # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()  # Traer los resultados de un select
    else:
        conn.commit()  # Hacer efectiva la escritura de datos
        data = None

    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexion

    return data

def conectar (db):
    # Conecto con base de datos
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="banco")
    cursor = db.cursor()
    return cursor

def insert_xml_to_bd(f_clientes):
    c = 0
    while (c < 3):
        # Datos del cliente

        id_cli = f_clientes[c].getchildren()[0].text
        nombre = f_clientes[c].getchildren()[1].text
        direccion = f_clientes[c].getchildren()[2].text
        dni = (f_clientes[c].getchildren()[3].text)

        # Datos de los cuentas de los clientes
        cuentas = f_clientes[c].getchildren()[4].getchildren()

        for cuenta_cli in cuentas:
            cta_id = cuenta_cli.getchildren()[0].text
            cta_tipo = cuenta_cli.getchildren()[1].text
            balance = (cuenta_cli.getchildren()[2].text)

        # Inserto datos de xml a base de datos
        id_cli_bd = "'" + id_cli + "'"
        nombre_bd = "'" + nombre + "'"
        cta_tipo_bd = "'" + cta_tipo + "'"

        dato = "(" + id_cli_bd + "," + nombre_bd + "," + dni + "," + cta_tipo_bd + "," + balance + ");"
        consulta = "INSERT INTO clientes VALUES"
        query = consulta + dato
        print query

        run_query(query)
        c = c + 1

def consultar_ctas():
    print ("Ingrese DNI de cliente:")
    dni = raw_input()
    consulta = "SELECT nombre,tipo_cta, balance FROM clientes WHERE dni ="
    query = consulta + dni
    print run_query(query)