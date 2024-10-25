#Tablas de Multiplicar

def tablasMultiplicar():
    for i in range (1,11):
        print(f"Tabla del {i}")
        for j in range (1,11):
            print(f"{i} X {j} = {i*j}")
tablasMultiplicar()