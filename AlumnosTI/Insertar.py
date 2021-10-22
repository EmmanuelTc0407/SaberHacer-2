import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file= parse('edificio.xml')
root = et.Element("Edificio_2")
xmlRoot = xml_file.getroot()

se = et.SubElement(root,"Alumno_Unknown")
et.SubElement(se, "Matricula").text = "10000000"
et.SubElement(se, "Carrera").text = "Hacker White Hat"
et.SubElement(se, "Nombre").text = "LEMILLION"

xmlRoot.append(se)
xml_file.write("edificio.xml",xml_declaration=True)
