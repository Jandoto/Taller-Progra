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

    
class MatrixManager:
    def __init__(self):
        self.ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.matrices = []
        self.matrices_alpha = []
        self.matrices_total = []
        self.n = 0
        for i in range(len(self.ABC)):
            self.matrices.append("NULL")
            self.matrices_alpha.append("NULL")
            self.matrices_total.append("NULL")

        self.valores1 = [1, 2, 2, 1, 1, 2]
        self.valores4 = ["2A", "", "", "", "", ""]
        self.valores5 = ["B", "", "", "", "", ""]
        self.y1 = 2
        self.z1 = 3
        self.matrices[0] = Matrix(self.valores1, self.y1, self.z1)
        self.matrices_alpha[0] = Matrix(self.valores4, self.y1, self.z1)

        self.a = Matrix.transpuesta(self.matrices[0])
        self.valores2 = [1, 2, 0, 1, 1, 2]
        self.y2 = 2
        self.z2 = 3
        self.matrices[1] = Matrix(self.valores2, self.y2, self.z2)
        self.matrices_alpha[1] = Matrix(self.valores5, self.y2, self.z2)

    def leer(self):
        # Implementar la función de leer más tarde
        pass

    def guardar(self):
        # Implementar la función de guardar más tarde
        pass

    def operaciones(self):
        while self.n != "SALIR":
            self.n = input("OPERACION :")
            self.n = self.n.replace(" ", "")
            self.n = self.n.upper()
            if self.n[0] in self.ABC:
                if self.n[3] == "+":

                    valor = self.ABC.index(self.n[0])
                    valor1 = self.ABC.index(self.n[2])
                    valor2 = self.ABC.index(self.n[4])

                    self.matrices[valor] = self.matrices[valor1] + self.matrices[valor2]
                    self.matrices_alpha[valor] = self.matrices_alpha[valor1].suma_alpha(self.matrices_alpha[valor2])
                    self.matrices_total[valor] = self.matrices[valor].fusion_matrices(self.matrices_alpha[valor])
                    
                    print(self.matrices_total[valor])
                    return str(self.matrices_total[valor])
                if self.n[3] == "-":
                    valor = self.ABC.index(self.n[0])
                    valor1 = self.ABC.index(self.n[2])
                    valor2 = self.ABC.index(self.n[4])

                    self.matrices[valor] = self.matrices[valor1] - self.matrices[valor2]
                    self.matrices_alpha[valor] = self.matrices_alpha[valor1].resta_alpha(self.matrices_alpha[valor2])

                if self.n[3] == "*" and self.n[2] not in self.ABC:
                    valor = self.ABC.index(self.n[0])
                    valor1 = self.n[2]
                    valor2 = self.ABC.index(self.n[4])

                    self.matrices[valor] = self.matrices[valor2] * int(valor1)
                    self.matrices_alpha[valor] = self.matrices_alpha[valor2].mul_alpha(valor1)
                    self.matrices_total[valor] = self.matrices[valor].fusion_matrices(self.matrices_alpha[valor])

                if self.n[3] == "*" and self.n[2] in self.ABC and self.n[4] in self.ABC:
                    valor = self.ABC.index(self.n[0])
                    valor1 = self.ABC.index(self.n[2])
                    valor2 = self.ABC.index(self.n[4])

                    self.matrices_total[valor] = self.matrices[valor1].mul2(self.matrices[valor2], self.matrices_alpha[valor1], self.matrices_alpha[valor2])

                if "**T" in self.n:
                    valor = self.ABC.index(self.n[0])
                    valor1 = self.ABC.index(self.n[2])

                    self.matrices[valor] = Matrix.transpuesta(self.matrices[valor1])
                    self.matrices_alpha[valor] = Matrix.transpuesta(self.matrices_alpha[valor1])
                    self.matrices_total[valor] = self.matrices[valor].fusion_matrices(self.matrices_alpha[valor])

                if "sort" in self.n:
                    print("sort")

                elif self.n[0] == "s" and self.n[1] == "o":
                    print("SSSSSSSSSSSSSS")


    def menu(self):
        while True:
            print("Menú de opciones:")
            print("1. Leer matrices")
            print("2. Guardar matrices")
            print("3. Realizar operaciones con matrices")
            print("4. Salir")

            opcion = input("Ingrese el número de la opción que desea realizar: ")

            if opcion == "1":
                self.leer()
            elif opcion == "2":
                self.guardar()
            elif opcion == "3":
                self.operaciones()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida (1-4).")

gestor_matrices = MatrixManager()

# Ejecutar el menú
ab=gestor_matrices.menu()
print(ab)