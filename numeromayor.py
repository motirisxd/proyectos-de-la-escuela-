#Escribir una funcion que reciba 2 numeros y que regrese el numero mayor
def comparar_numeros(num1, num2):
    if num1 > num2:
        return f"El número mayor es: {num1}"
    elif num2 > num1:
        return f"El número mayor es: {num2}"
    else:
        return "Ambos números son iguales."
# Ejemplo de uso
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resultado = comparar_numeros(num1, num2)
print(resultado)