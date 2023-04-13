import xml.etree.ElementTree as ET

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

info_personal = ET.Element("info_personal")

nombre_element = ET.SubElement(info_personal, "nombre")
nombre_element.text = nombre
apellido_element = ET.SubElement(info_personal, "apellido")
apellido_element.text = apellido

info_personal_xml = ET.tostring(info_personal, encoding="utf-8", xml_declaration=True)

info_personal_xml = info_personal_xml.decode()

print("Información en formato XML:")
print(info_personal_xml)
