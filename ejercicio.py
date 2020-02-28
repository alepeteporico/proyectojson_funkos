from funciones import *
import json
with open ("products.json") as fichero:
    datos=json.load(fichero)

while True:
    print("=============================================MENÚ=============================================")
    print("1. Listar las licencias que hay y al listarlas te pide si quieres listar las figuras que tiene alguna de ellas.")
    print("2. Pide por teclado una licencia y te dice las figuras que tiene.")
    print("3. Mostrar las figuras que sean de una categoría especfica.")
    print("4. Pide por teclado una figura y te dice de que licencia es y si hay alguna relacionada (Del mismo personaje).")
    print("5. Pide una figura y muestra en el navegador una imagen de la misma, después te pregunta si quieres ver las tiendas donde está disponible y te pregunta si quieres ir a alguna de ellas.")
    print("6. Salir")
    print("==============================================================================================")
    opc=int(input("Elige una opción: "))
    print("")

    if opc==1:
        print("-------LICENCIAS-------")
        for licencia in ej1(datos):
            print("-",licencia)
        print("")

        opcion=input("¿Quieres listar las figuras de alguna licencia? (s/n): ")

        while opcion=="s":
            licencia=input("Dime la licencia de la que quieres listar las figuras: ")
            print("-------FIGURAS-------")
            for figura in ej1_2(datos,licencia):
                print("-",figura)
            print("--------------------")
            opcion=input("¿Quieres listar las figura de alguna otra licencia? (s/n): ")
        print("------------------------------------------------------------------")
        print("")

    elif opc==2:
        licencia=input("Dime la licencia de la que quieres contar las figuras: ")
        print(licencia,"tiene",ej2(datos,licencia),"figuras")
        print("------------------------------------------------------------------")
        print("")

    elif opc==3:
        categoria=input("Dime una categoria: ")
        for figura in ej3(datos,categoria):
            print("-",figura)
        print("------------------------------------------------------------------")
        print("")
    
    elif opc==4:
        figura=input("Dime una figura: ")
        print(figura,"pertenece a",ej4(datos,figura))
        print("")
        
        if len(ej4_2(datos,figura))!=0:
            print("-------RELACIONADAS-------")
            for figuras in ej4_2(datos,figura):
                print("-",figuras)
        
        else:
            print("No hay figuras relacionadas.")
        print("------------------------------------------------------------------")
        print("")
    
    elif opc==6:
        break

    else:
        print("ERROR, ESTA OPCION NO EXISTE")