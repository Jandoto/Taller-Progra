ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
matrices=[]
for i in range (len(ABC)):
    matrices.append("NULL")
print(matrices)

def crear_matriz(filas, columnas, valores):
    if len(valores) != filas * columnas:
        raise ValueError("La cantidad de valores no coincide con el tamaño de la matriz")

    matriz = []
    indice_valor = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(valores[indice_valor])
            indice_valor += 1
        matriz.append(fila)
    return matriz

def sumar_matrices(A,B):
    if len(A[0]) != len(B[0]):
        raise ValueError("Las matrices no son posibles de sumarse")
    C=[]
    for i in range(len(A)):
        aux1=[]
        for j in range(len(A[0])):
            aux2=A[i][j]+B[i][j]
            aux1.append(aux2)
        C.append(aux1)
    return C

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz_3x3 = crear_matriz(3, 3, valores)
matriz_3x32 = crear_matriz(3, 3, valores)
x=sumar_matrices(matriz_3x3,matriz_3x32)
print(F[0])
print("Matriz 3x3 con valores secuenciales:")
print(matriz_3x3[1][1])