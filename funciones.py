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

def ej2(datos,licencia):
    num=len(datos[licencia])
    return num

def ej3(datos,categoria):
    figuras=[]
    for licencias in datos:
        for figura in datos[licencias]:
            if figura.get("category")==categoria:
                figuras.append(figura["name"])
    return figuras

def ej4(datos,figura):
    for licencias in datos:
        for figuras in datos[licencias]:
            if figuras.get("name")==figura:
                return licencias

def ej4_2(datos,figura):
    relacionadas=[]

    for licencias in datos:
        for figuras in datos[licencias]:
            if figuras.get("name")!=figura and figura in figuras.get("name"):
                relacionadas.append(figuras["name"])
    return relacionadas