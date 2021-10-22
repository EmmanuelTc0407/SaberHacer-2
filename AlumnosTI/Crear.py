import xml.etree.cElementTree as et

root = et.Element("Edificio_2")

se = et.SubElement(root,"Alumno_1")
et.SubElement(se, "Matricula").text = "18040103"
et.SubElement(se, "Carrera").text = "Redes inteligentes y ciberseguridad"
et.SubElement(se, "Nombre").text = "Emmanuel Tovar Castañón"

se = et.SubElement(root,"Alumno_2")
et.SubElement(se, "Matricula").text = "18040106"
et.SubElement(se, "Carrera").text = "Redes inteligentes y ciberseguridad"
et.SubElement(se, "Nombre").text = "Valeria Vazquez Enriquez"

se = et.SubElement(root,"Alumno_3")
et.SubElement(se, "Matricula").text = "18040108"
et.SubElement(se, "Carrera").text = "Redes inteligentes y ciberseguridad"
et.SubElement(se, "Nombre").text = "Rosa Rodriguez Uribe"

se = et.SubElement(root,"Alumno_4")
et.SubElement(se, "Matricula").text = "18040109"
et.SubElement(se, "Carrera").text = "Redes inteligentes y ciberseguridad"
et.SubElement(se, "Nombre").text = "Alonso Reyes Segura"

se = et.SubElement(root,"Alumno_5")
et.SubElement(se, "Matricula").text = "18040101"
et.SubElement(se, "Carrera").text = "Redes inteligentes y ciberseguridad"
et.SubElement(se, "Nombre").text = "Luis Nuncio Rodriguez"

se = et.SubElement(root,"Alumno_1")
et.SubElement(se, "Matricula").text = "18040204"
et.SubElement(se, "Carrera").text = "Entornos virtuales y negocios digitales"
et.SubElement(se, "Nombre").text = "Mariana Elizalde Lara"

se = et.SubElement(root,"Alumno_2")
et.SubElement(se, "Matricula").text = "18040206"
et.SubElement(se, "Carrera").text = "Entornos virtuales y negocios digitales"
et.SubElement(se, "Nombre").text = "Jose Gallardo Monroy"

se = et.SubElement(root,"Alumno_3")
et.SubElement(se, "Matricula").text = "18040208"
et.SubElement(se, "Carrera").text = "Entornos virtuales y negocios digitales"
et.SubElement(se, "Nombre").text = "Victor Sanchez Martinez"

se = et.SubElement(root,"Alumno_4")
et.SubElement(se, "Matricula").text = "18040210"
et.SubElement(se, "Carrera").text = "Entornos virtuales y negocios digitales"
et.SubElement(se, "Nombre").text = "Erik Vallejo Ramirez"

se = et.SubElement(root,"Alumno_5")
et.SubElement(se, "Matricula").text = "18040212"
et.SubElement(se, "Carrera").text = "Entornos virtuales y negocios digitales"
et.SubElement(se, "Nombre").text = "Kevin Guerrero Martinez"

se = et.SubElement(root,"Alumno_1")
et.SubElement(se, "Matricula").text = "18040301"
et.SubElement(se, "Carrera").text = "Desarrollo y gestion de software"
et.SubElement(se, "Nombre").text = "Priscila Castro Garay"

se = et.SubElement(root,"Alumno_2")
et.SubElement(se, "Matricula").text = "18040304"
et.SubElement(se, "Carrera").text = "Desarrollo y gestion de software"
et.SubElement(se, "Nombre").text = "Ernesto Alvarez Martinez"

se = et.SubElement(root,"Alumno_3")
et.SubElement(se, "Matricula").text = "18040307"
et.SubElement(se, "Carrera").text = "Desarrollo y gestion de software"
et.SubElement(se, "Nombre").text = "Felipe Alvarez Sanchez"

se = et.SubElement(root,"Alumno_4")
et.SubElement(se, "Matricula").text = "18040311"
et.SubElement(se, "Carrera").text = "Desarrollo y gestion de software"
et.SubElement(se, "Nombre").text = "Guillermo Herrera Solis"

se = et.SubElement(root,"Alumno_5")
et.SubElement(se, "Matricula").text = "18040313"
et.SubElement(se, "Carrera").text = "Desarrollo y gestion de software"
et.SubElement(se, "Nombre").text = "Daniel Juarez Zavala"

tree = et.ElementTree(root)
tree.write("edificio.xml", xml_declaration=True)




















