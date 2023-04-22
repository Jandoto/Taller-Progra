class Matrix:
    def __init__(self, valores, y, z):
        self.y = y
        self.z = z
        self.matriz = []
        indice_valor = 0
        if len(valores) == y * z:
            for i in range(y):
                fila = []
                for j in range(z):
                    fila.append(valores[indice_valor])
                    indice_valor += 1
                self.matriz.append(fila)
        else:
            raise ValueError("El número de valores proporcionados no coincide con las dimensiones de la matriz.")
    
    def __str__(self):
        matrix_str = ''
        for fila in self.matriz:
            matrix_str += '| '
            for elemento in fila:
                matrix_str += f'{elemento} '
            matrix_str = matrix_str.rstrip()  
            matrix_str += ' |\n'
        return matrix_str.rstrip()  
    
    def __add__(self,b):
        if self.y != b.y or self.z != b.z:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarlas.")
        valores=[]
        for i in range(self.y):
            for j in range(self.z):
                valor=self.matriz[i][j]+b.matriz[i][j]
                valores.append(valor)
        return Matrix(valores,self.y,self.z)
    
    def __sub__(self,b):
        if self.y != b.y or self.z != b.z:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarlas.")
        valores=[]
        for i in range(self.y):
            for j in range(self.z):
                valor=self.matriz[i][j]-b.matriz[i][j]
                valores.append(valor)
        return Matrix(valores,self.y,self.z)
    
    def __mul__(self, b):
        if self.z != b.y:
            raise ValueError("El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
        valores = []
        for i in range(self.y):
            for j in range(b.z):
                valor = 0
                for k in range(self.z):
                    valor += self.matriz[i][k] * b.matriz[k][j]
                valores.append(valor)
        return Matrix(valores, self.y, b.z)

    def transpuesta(self):
        valores = []
        for j in range(self.z):
            for i in range(self.y):
                valores.append(self.matriz[i][j])
        return Matrix(valores, self.z, self.y)
    
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
matrices = []
for i in range(len(ABC)):
    matrices.append("NULL")
n=0

valores1 = [1, 2, 3, 4, 5, 6]
y1 = 2
z1 = 3
matrices[0] = Matrix(valores1, y1, z1)
a=Matrix.transpuesta(matrices[0])
print(matrices[0])
print(a)
valores2 = [1, 2, 3, 4, 5, 6]
y2 = 2
z2 = 3
matrices[1] = Matrix(valores2, y2, z2)

while n != "SALIR":
    n=input("Hola :")
    n=n.replace(" ","")
    if n[0] in ABC:
        print("entra")
        n=n.upper()
        if n[3]=="+":
            valor=ABC.index(n[0])
            valor1=ABC.index(n[2])
            valor2=ABC.index(n[4])
            print(valor)
        
            matrices[valor] = matrices[valor1] + matrices[valor2]
        
        if n[3]=="-":
            valor=ABC.index(n[0])
            valor1=ABC.index(n[2])
            valor2=ABC.index(n[4])
            print(valor)
        
            matrices[valor] = matrices[valor1] - matrices[valor2]

        if "**T" in n:
            valor=ABC.index(n[0])
            valor1=ABC.index(n[2])
            print(valor)
        
            matrices[valor] = Matrix.transpuesta(matrices[valor1]) 

        if "sort" in n:
            print("sort")


            
    elif n[0]=="s" and n[1]=="o":
        print("SSSSSSSSSSSSSS")
    print(matrices[2])

