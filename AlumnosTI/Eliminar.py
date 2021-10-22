from xml.etree.ElementTree import parse, Element

file_name = 'edificio.xml'
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find('Alumno_1'))

new_file = 'edificio2.xml'
doc_xml.write(new_file, xml_declaration=True)
