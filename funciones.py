def ej1(datos):
    licencias=[]
    for licencia in datos:
        licencias.append(licencia)
    return licencias

def ej1_2(datos,licencia):
    figuras=[]
    for figura in datos[licencia]:
        figuras.append(figura["name"])
    return figuras