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
    
    def separar_letras_numeros(self,l1):
        resultados = []
        for elemento in l1:
            numero = ""
            letra = ""

            ultimo_tipo = None
            for caracter in elemento:
                tipo_actual = None

                if caracter.isdigit():
                    tipo_actual = "numero"
                elif caracter.isalpha():
                    tipo_actual = "letra"

                if ultimo_tipo and ultimo_tipo != tipo_actual:
                    if tipo_actual == "numero":
                        numero = ""
                    elif tipo_actual == "letra":
                        letra = ""

                if tipo_actual == "numero":
                    numero += caracter
                elif tipo_actual == "letra":
                    letra += caracter

                ultimo_tipo = tipo_actual

            if letra and not numero:
                numero = "1"
            elif not letra and not numero:
                numero = "0"

            resultados.append((letra, numero))


        aux=[]
        CBA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for t in range(len(CBA)):
            aux.append(0)
        for x in range (len(resultados)):
            aux[CBA.index(resultados[x][0].upper())]=int(resultados[x][1])


        return aux

    
    def suma_alpha(self,b):
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        valores = []
        if self.y != b.y or self.z != b.z:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarlas.")
        
        for i in range(self.y):
            for j in range(self.z):
                valor=self.matriz[i][j]
                valor=valor.replace(" ","").split("+")
                valor2=b.matriz[i][j]
                valor2=valor2.replace(" ","")
                valor2=valor2.split("+")
                lista1 = self.separar_letras_numeros(valor)
                lista2 = self.separar_letras_numeros(valor2)
                val=""
                for t in range (len(lista1)):
                    if lista1[t]!=0 or lista2[t] != 0:
                        lista1[t]=lista1[t]+lista2[t]
                        val=val+str(lista1[t])+ABC[t]
                        val=val+"+"
                    else:
                        pass
                valores.append(val[:-1])

                
                

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
matrices_alpha=[]
for i in range(len(ABC)):
    matrices.append("NULL")
    matrices_alpha.append("NULL")
n=0


valores1 = [1, 2, 3, 4, 5, 6]
valores4 = ["2A+C", "d", "c", "d", "e", "f"]
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
        if n[3]=="+":

            valor=ABC.index(n[0])
            valor1=ABC.index(n[2])
            valor2=ABC.index(n[4])

        
            matrices[valor] = matrices[valor1] + matrices[valor2]
            matrices_alpha[valor] = matrices_alpha[valor1].suma_alpha(matrices_alpha[valor2])



        
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

