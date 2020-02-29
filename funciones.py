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
    descartados=["The","the","a","in","King"]
    cadenas=figura.split(" ")

    for figuras in datos[ej4(datos,figura)]:
        for cadena in cadenas:
            if cadena not in descartados:
                if figuras.get("name")!=figura and cadena in figuras.get("name") and figuras.get("name") not in relacionadas:
                    relacionadas.append(figuras["name"])
    return relacionadas

def ej5(datos,figura):
    for licencias in datos:
        for figuras in datos[licencias]:
            if figuras["name"]==figura:
                imagen=figuras.get("img")
    return imagen

def ej5_2(datos,figura):
    tiendas=[]
    for licencias in datos:
        for figuras in datos[licencias]:
            if figuras["name"]==figura:
                for elemento in figuras.get("tiendas"):
                    for tienda in elemento.keys():
                        tiendas.append(tienda)                 
    return tiendas