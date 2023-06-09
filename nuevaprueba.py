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
        output = []
        max_len = max(len(str(x)) for row in self.matriz for x in row)

        for row in self.matriz:
            formatted_row = [f'{x:<{max_len}}' for x in row]
            row_str = '| ' + ' '.join(formatted_row) + ' |'
            output.append(row_str)

        return '\n'.join(output)
    
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
    
    def fusion_matrices(self, matriz_alpha):
        if self.y != matriz_alpha.y or self.z != matriz_alpha.z:
            raise ValueError("Las matrices deben tener las mismas dimensiones para fusionarlas.")

        fusionada = []
        for i in range(self.y):
            for j in range(self.z):
                valor_numerico = str(self.matriz[i][j])
                valor_alfabetico = matriz_alpha.matriz[i][j]
                if valor_alfabetico:
                    fusion = valor_numerico + "+" + valor_alfabetico
                    print(fusion)
                else:
                    fusion = valor_numerico
                fusionada.append(fusion)
        
        return Matrix(fusionada, self.y, self.z)
    

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
                elif caracter=="-":
                    tipo_actual = "numero"

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
                        if lista1[t]!=0:
                            val=val+str(lista1[t])+ABC[t]
                            val=val+"+"
                    else:
                        pass
                valores.append(val[:-1])

        return Matrix(valores,self.y,self.z)

    def resta_alpha(self,b):
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
                        lista1[t]=lista1[t]-lista2[t]
                        if lista1[t]!=0:
                            val=val+str(lista1[t])+ABC[t]
                            val=val+"+"
                        else:
                            pass
                    else:
                        pass
                valores.append(val[:-1])

                
                

        return Matrix(valores,self.y,self.z)
    
    def __mul__(self, b):
        valores = []
        for i in range(self.y):
            for j in range(self.z):
                valor = self.matriz[i][j] * b
                print(valor)
                valores.append(valor)
        return Matrix(valores, self.y, self.z)
    
    def mul2(self, a,b,c):
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.z != a.y:
            raise ValueError("El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
        valores = []
        for i in range(self.y):
            for j in range(a.z):
                valor = 0
                val_alpha=""
                for k in range(self.z):
                    #MULTIPLICACION PARTE NÚMERICA CON NÚMERICA
                    valor += self.matriz[i][k] * a.matriz[k][j] 

                    
                    #MULTIPLICACION PARTE NÚMERICA CON ALFABETICA
                    valor1=c.matriz[k][j]
                    valor1=valor1.replace(" ","").split("+")
                    lista1 = self.separar_letras_numeros(valor1)

                    val=""
                    for t in range (len(lista1)):
                        if lista1[t]!=0:

                            lista1[t]=lista1[t]*int(self.matriz[i][k])

                            if lista1[t]!=0:
                                if lista1[t]==1:

                                    val=val+str(ABC[t])
                                    val=val+"+"
                                else:
                                    val=val+str(lista1[t])+str(ABC[t])
                                    val=val+"+"

                        else:
                            pass
                    val_alpha=val_alpha+val
                    

                    #MULTIPLICACION PARTE ALFABETICA CON ALFABETICA
                    valor1=b.matriz[i][k]
                    valor1=valor1.replace(" ","").split("+")
                    lista1 = self.separar_letras_numeros(valor1)

                    valor2=c.matriz[k][j]
                    valor2=valor2.replace(" ","").split("+")
                    lista2 = self.separar_letras_numeros(valor2)

                    val=""
                    auxiliar=[]
                    for t in range (len(lista1)):
                        if lista1[t]!=0:
                            
                            for g in range (len(lista2)):
                                if lista2[g]!=0:

                                    lista1[t]=lista1[t]*lista2[g]
                                    if lista1[t]==1:
                                        val=val+str(ABC[t])+str(ABC[g])
                                        val=val+"+"
                                    else:
                                        val=val+str(lista1[t])+str(ABC[t])+str(ABC[g])
                                        val=val+"+"


                            #if lista1[t]!=0:
                                #val=val+str(lista1[t])+str(ABC[t])+str(ABC[g])

                                #val=val+"+"
                        else:
                            pass
                    val_alpha=val_alpha+val


                    #MULTIPLICACION PARTE ALFABETICA CON NÚMERICA
                    valor1=b.matriz[i][k]
                    valor1=valor1.replace(" ","").split("+")
                    lista1 = self.separar_letras_numeros(valor1)

                    val=""
                    for h in range (len(lista1)):
                        if lista1[h]!=0:

                            lista1[h]=lista1[h]*int(a.matriz[k][j])

                            if lista1[h]!=0:
                                if lista1[h]==1:

                                    val=val+str(ABC[h])
                                    val=val+"+"
                                else:
                                    val=val+str(lista1[h])+str(ABC[h])
                                    val=val+"+"
                        else:
                            pass
                    val_alpha=val_alpha+val
                    ########################################################
                

                if val_alpha.endswith('+'):
                    val_alpha=val_alpha[:-1]
                else:
                    pass

                
                if val_alpha != "":         
                    valor=str(valor)+"+"+val_alpha
                else:
                    valor=str(valor)
                valores.append(valor)

        return Matrix(valores, self.y, a.z)
    
    def mul_alpha(self,b):
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        valores = []

        for i in range(self.y):
            for j in range(self.z):
                valor=self.matriz[i][j]
                valor=valor.replace(" ","").split("+")
                lista1 = self.separar_letras_numeros(valor)

                val=""
                for t in range (len(lista1)):
                    if lista1[t]!=0:

                        lista1[t]=lista1[t]*int(b)

                        if lista1[t]!=0:
                            val=val+str(lista1[t])+ABC[t]

                            val=val+"+"
                    else:
                        pass
                valores.append(val[:-1])


        return Matrix(valores,self.y,self.z)

    def transpuesta(self):
        valores = []
        for j in range(self.z):
            for i in range(self.y):
                valores.append(self.matriz[i][j])
        return Matrix(valores, self.z, self.y)

    
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
matrices = []
matrices_alpha=[]
matrices_total=[]
for i in range(len(ABC)):
    matrices.append("NULL")
    matrices_alpha.append("NULL")
    matrices_total.append("NULL")
n=0


valores1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valores4 = ["", "", "", "", "", "","","",""]
valores5 = ["a", "b", "c", "d", "e", "f","g","h","i"]
y1 = 3
z1 = 3
matrices[0] = Matrix(valores1, y1, z1)
matrices_alpha[0] = Matrix(valores4, y1, z1)

a=Matrix.transpuesta(matrices[0])
valores2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
y2 = 3
z2 = 3
matrices[1] = Matrix(valores2, y2, z2)
matrices_alpha[1] = Matrix(valores5, y2, z2)

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
            matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor])



        
        if n[3]=="-":
            valor=ABC.index(n[0])
            valor1=ABC.index(n[2])
            valor2=ABC.index(n[4])
            print(valor)
        
            matrices[valor] = matrices[valor1] - matrices[valor2]
            matrices_alpha[valor] = matrices_alpha[valor1].resta_alpha(matrices_alpha[valor2])

        if n[3]=="*" and n[2] not in ABC :
            valor=ABC.index(n[0])
            valor1=n[2]
            valor2=ABC.index(n[4])
            
            matrices[valor] = matrices[valor2] * int(valor1)  
            matrices_alpha[valor] = matrices_alpha[valor2].mul_alpha(valor1)
            matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor])

        if n[3]=="*" and n[2] in ABC and n[4]in ABC:
            print("AAAAA")
            valor=ABC.index(n[0])
            valor1=ABC.index(n[2])
            valor2=ABC.index(n[4])

        
   
            matrices_total[valor] = matrices[valor1].mul2(matrices[valor2],matrices_alpha[valor1],matrices_alpha[valor2])

        if "**T" in n:
            valor=ABC.index(n[0])
            valor1=ABC.index(n[2])
            print(valor)
        
            matrices[valor] = Matrix.transpuesta(matrices[valor1])
            matrices_alpha[valor] = Matrix.transpuesta(matrices_alpha[valor1])
            matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor]) 

        if "sort" in n:
            print("sort")


            
    elif n[0]=="s" and n[1]=="o":
        print("SSSSSSSSSSSSSS")

    print(matrices[2])
    print(matrices_total[2])

