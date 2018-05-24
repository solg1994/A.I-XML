import lxml.etree as node
import testxml

# DOM
testxml.transform_xml("banco.xml", "Output_1.xml")
testxml.transform_xml("banco_2.xml", "Output_2.xml")

# NOTA: Sigue estando mal el XSLT, solo hice el ejercicio con el parseo del Banco 1.-
banco = node.parse("Output_1.xml")
raiz = banco.getroot()

'''
# Pruebas
print "La raiz es: ", raiz
print "Raiz Sub-elementos: ", raiz.getchildren()
print "Hijos de clientes", raiz.getchildren()[0].getchildren()
'''

# Todos los clientes
f_clientes = raiz.getchildren()[0].getchildren()

#Tomo los xml finales y los ingreso en la BD

testxml.insert_xml_to_bd(f_clientes)

#Consultar cuentas de Clientes por DNI en la BD.-
testxml.consultar_ctas()
