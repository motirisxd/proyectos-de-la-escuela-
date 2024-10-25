#Crear una funcion que reciba una cadena de texto 
#y que regrese esa cadea de texto arrevez

# invertir("python") #nohtyp

# def palabraInvertida(palabra):
#     return palabra[::-1]
# palabra= input("ingrese la palabra")
# palabraInvertida=palabraInvertida(palabra)
# print("Palabra Invertida:",palabraInvertida)

def invertir (cadena):
    cadena_inverida = ""
    for letra in cadena:
        cadena_inverida = letra + cadena_inverida
    return cadena_inverida
print(invertir("python"))