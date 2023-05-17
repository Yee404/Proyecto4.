def Read():
    with open("excel.csv","r", encoding = "ISO-8859-1") as info_m:
        Texto = info_m.read()
        info_m.close()
        registros = []
        lineas = Texto.split("\n")
        lineas.pop()
        for i in lineas:
            linea = i.split(",")
            registros.append(linea)
        return(registros)
    
def Guardar(c):
    registrof = ""
    for i in range(len(c)):
        registrof += ",".join(c[i])
        registrof += "\n"
    with open("datos.csv","w", encoding = "ISO-8859-1") as info_m:
        Texto = info_m.write(registrof)
    info_m.close()
    
def NuevoUsuario(x):
    new_line = ",".join(x)
    new_line += "\n"
    with open("datos.csv","a", encoding = "ISO-8859-1") as info_m:
        Texto = info_m.write(new_line)
    info_m.close()
    