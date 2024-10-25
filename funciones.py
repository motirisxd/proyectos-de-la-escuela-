# def funcionSaludar(nombre):
#     return f"!HOLAAAAAA, {nombre}!"
# mensaje=funcionSaludar("Angel ELias")
# print(mensaje)

# #sumar numeros pares en un rango establecido
# def sumaPares(inicio,fin):
#     suma=0
#     for num in range (inicio,fin+1):
#         if num%2==0:
#             suma+=num
#             print(num)
#     return suma

# print(sumaPares(1,20))

# def contarVocales(texto):
#     contador=0
#     vocales= 'aeiouAEIOU'
#     for letra in texto:
#         if letra in vocales:
#             contador+=1
#     return contador
# print(contarVocales("Murcielago"))




#Adivina el Numero
import random
def adivinaUnNumero():
    numero_secreto = random.randint(1,100)
    adivinado=False #variable bandera
    
    while not adivinado:
        intento= int(input("adivina un numero entre 1,100: "))
    
        if intento>0:
            if intento<numero_secreto :
                print("El numero es mayor")
            elif intento>numero_secreto:
                print("El numero es menor")
            else:
                print("Felicidades adivinaster el numero")
                adivinado=True
        else:
            print("Ingresa Numeros Positivos")
adivinaUnNumero()