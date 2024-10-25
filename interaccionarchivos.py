# with open("archivoprueba.txt", "r") as archivo:
#     contenido= archivo.read()
#     print(contenido)

#FUNCION PARA ESCRIBIR UN ARCHIVO

# def escrbirArchivo(nombre_archivo,contenido):
#     with open(nombre_archivo, "r") as archivo:
#         for linea in archivo:
#             print(linea.strip())

#FUNCION PARA ESCRIBIR UN ARCHIVO
# def escrbirArchivo(nombre_archivo,contenido):
#     with open(nombre_archivo, "w") as archivo:
#         archivo.write(contenido)
# escrbirArchivo("mi_archivo.txt","Hola a todos, estoy escribiendo desde el archivo")      

#contar lineas del archivo
def contarLineas(nombre_archivo):
    with open(nombre_archivo,"r") as archivo:
        lineas=archivo.readlines()
    return len(lineas)
num_lineas=contarLineas("archivoprueba.txt")
#print(f"El archivo tiene {num_lineas} lineas")

def copiarArchivos(archivo_origen,archivo_destino):
    with open(archivo_origen,"r") as original:
         contenido= original.read()
         print("Texto copiado")   
    with open(archivo_destino,"w") as copia:
        copia.write(contenido)
        print("Archivo copiado correctamente")
#copiarArchivos("archivoprueba.txt","mi_archivo.txt")

#buscar palabra
def buscaPalabra(nombre_archivo,palabra):
    contador=0
    with open(nombre_archivo,"r") as archivo:
        for linea in archivo:
            palabras_en_linea=linea.split()
            contador+= palabras_en_linea.count(palabra)
    return contador 
cantidad= buscaPalabra("archivoprueba.txt",("HOLA"))
print(f"la palabra hola aparece {cantidad} veces")