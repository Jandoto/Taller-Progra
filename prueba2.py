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
    
    def oper_alpha(self,b):
        print("aaaaa")
        if self.y != b.y or self.z != b.z:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarlas.")
        
        for i in range(self.y):
            for j in range(self.z):
                print("AAAA")
                auxa=[]
                auxb=[]
                CBA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                for t in range(len(CBA)):
                    auxa.append(0)
                    auxb.append(0)
                valor=self.matriz[i][j]
                valor=valor.replace(" ","")
                valor=valor.split("+")
                for c in range (len(valor)):
                    resultado = ""
                    ultimo_tipo = None
                    for caracter in valor[c]:
                        tipo_actual = None
                        if caracter.isdigit():
                            tipo_actual = "numero"
                        elif caracter.isalpha():
                            tipo_actual = "letra"
                        if ultimo_tipo and ultimo_tipo != tipo_actual:
                            if tipo_actual == "numero":
                                print(resultado,"PRIMERO")
                                almacenado=resultado
                                resultado = ""
                            elif tipo_actual == "letra":
                                almacenado=resultado
                                resultado = ""
                            else:
                                pass

                        resultado += caracter
                        ultimo_tipo = tipo_actual
                    print(almacenado,"almacenado")
                    print(resultado,"resultado")
                    resultado=resultado.upper()
                    if resultado.isdigit():
                        auxa[CBA.index(almacenado)]=resultado
                        
                    else:
                        auxa[CBA.index(resultado)]=almacenado
                    print(auxa,"aaaaaaaaaa")
                
        return 12
        

        
    
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
matrices_alpha=[]
for i in range(len(ABC)):
    matrices.append("NULL")
    matrices_alpha.append("NULL")
n=0
print("aaaaaaa")

valores1 = [1, 2, 3, 4, 5, 6]
valores4 = ["2A+C+D", "b", "c", "d", "e", "f"]
y1 = 2
z1 = 3
matrices[0] = Matrix(valores1, y1, z1)
matrices_alpha[0] = Matrix(valores4, y1, z1)

a=Matrix.transpuesta(matrices[0])
valores2 = [1, 2, 3, 4, 5, 6]
y2 = 2
z2 = 3
matrices[1] = Matrix(valores2, y2, z2)
matrices_alpha[1] = Matrix(valores4, y1, z1)

while n != "SALIR":
    n=input("Hola :")
    n=n.replace(" ","")
    n=n.upper()
    if n[0] in ABC:
        print("entra")
        if n[3]=="+":
            valor=ABC.index(n[0])
            valor1=ABC.index(n[2])
            valor2=ABC.index(n[4])
            print("hols")
        
            matrices[valor] = matrices[valor1] + matrices[valor2]
            matrices_alpha[valor] = matrices_alpha[valor1].oper_alpha(matrices_alpha[valor2])



        
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
    print(matrices_alpha[2])

