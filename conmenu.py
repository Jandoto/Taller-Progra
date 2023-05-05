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
        

    def inverse(self):
        if self.y != self.z:
            raise ValueError("La matriz debe ser cuadrada para calcular la inversa")

        matrix = [[self.matriz[i][j] for j in range(self.z)] for i in range(self.y)]

        n = len(matrix)
        identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

        for i in range(n):
            if matrix[i][i] == 0:
                for j in range(i+1, n):
                    if matrix[j][i] != 0:
                        matrix[i], matrix[j] = matrix[j], matrix[i]
                        identity_matrix[i], identity_matrix[j] = identity_matrix[j], identity_matrix[i]
                        break
                else:
                    raise ValueError("La matriz no tiene inversa")

            pivot = matrix[i][i]
            for j in range(i+1, n):
                factor = matrix[j][i] / pivot
                for k in range(i, n):
                    matrix[j][k] -= factor * matrix[i][k]
                for k in range(n):
                    identity_matrix[j][k] -= factor * identity_matrix[i][k]

        for i in range(n-1, -1, -1):
            pivot = matrix[i][i]
            for j in range(i):
                factor = matrix[j][i] / pivot
                for k in range(n):
                    identity_matrix[j][k] -= factor * identity_matrix[i][k]
                matrix[j][i] = 0
            identity_matrix[i] = [x / pivot for x in identity_matrix[i]]
        

        
        identity_matrix_of=[]
        for i in range (len(identity_matrix)):
            for j in range (len(identity_matrix[i])):
                identity_matrix_of.append(identity_matrix[i][j])

        return Matrix(identity_matrix_of, self.y, self.z)
    
    def determinant(self):
        matrix = [[self.matriz[i][j] for j in range(len(self.matriz[0]))] for i in range(len(self.matriz))]
        if len(matrix) != len(matrix[0]):
            raise ValueError("La matriz debe ser cuadrada para calcular el determinante")

        n = len(matrix)
        det = 1
        epsilon = 1e-15

        for i in range(n):
            max_element = abs(matrix[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(matrix[k][i]) > max_element:
                    max_element = abs(matrix[k][i])
                    max_row = k

            if abs(max_element) < epsilon:
                return 0

            if i != max_row:
                matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
                det = -det

            det *= matrix[i][i]

            for j in range(i + 1, n):
                matrix[i][j] /= matrix[i][i]

            for k in range(i + 1, n):
                for j in range(i + 1, n):
                    matrix[k][j] -= matrix[k][i] * matrix[i][j]

        return det

    def __str__(self, prefix="C"):
        output = []
        max_len = max(len(str(x)) for row in self.matriz for x in row)
        prefix = prefix + "="

        middle_row = (len(self.matriz) - 1) // 2
        prefix_length = len(prefix)

        for i, row in enumerate(self.matriz):
            formatted_row = [f'{x:<{max_len}}' for x in row]
            row_str = '| ' + ' '.join(formatted_row) + ' |'

            if i == middle_row:
                row_str = prefix + row_str
            else:
                row_str = ' ' * prefix_length + row_str

            output.append(row_str)

        return '\n'.join(output)



    
    def __add__(self,b):
        if self.y != b.y or self.z != b.z:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarlas.")
        valores=[]
        for i in range(self.y):
            for j in range(self.z):
                valor=int(self.matriz[i][j])+int(b.matriz[i][j])
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
        fusion=""
        if self.y != matriz_alpha.y or self.z != matriz_alpha.z:
            raise ValueError("Las matrices deben tener las mismas dimensiones para fusionarlas.")

        fusionada = []
        for i in range(self.y):
            for j in range(self.z):
                valor_numerico = str(self.matriz[i][j])
                valor_alfabetico = matriz_alpha.matriz[i][j]

                if valor_alfabetico:
                    if valor_numerico!="0":
                        fusion = valor_numerico + "+" + valor_alfabetico
                    else:
                        fusion=valor_alfabetico
                    
                else:

                    fusion = valor_numerico
                fusionada.append(fusion)
        
        return Matrix(fusionada, self.y, self.z)
    
    def sort(self, matriz_alpha):
        if self.y != matriz_alpha.y or self.z != matriz_alpha.z:
            raise ValueError("Las matrices deben tener las mismas dimensiones para fusionarlas.")

        tuplas = []
        for i in range(self.y):
            for j in range(self.z):
                fila=[]
                valor_numerico = str(self.matriz[i][j])
                valor_alfabetico = matriz_alpha.matriz[i][j]
                fila.append(valor_numerico)
                fila.append(valor_alfabetico)
                tuplas.append(fila)


        print(tuplas)
        c=sorted(tuplas, key=lambda num: num[0])
        x=len(c)
        print(x)
        auxiliar=[]
        eliminar=[]
        for i in range (x):

            print(c[i][0])
            if c[i][0]!="0":
                
                auxiliar.append(c[i])
                eliminar.append(i)
        print(eliminar,"aaaaa")
        for i in reversed(range(len(c))):
            
            if i in eliminar:
                print(c[i])
                c.pop(i)
        c=sorted(c, key=lambda al: al[1])
        
        print(c)
        print(auxiliar)

        auxiliar=auxiliar+c
        valores1=[]
        valores2=[]

        for i in range(len(auxiliar)):
            valo1=auxiliar[i][0]
            valo2=auxiliar[i][1]
            valores1.append(valo1)
            valores2.append(valo2)
        return Matrix(valores1,self.y,self.z),Matrix(valores2,self.y,self.z)
    

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
                            if lista1[t]==1:
                            
                                val=val+ABC[t]
                                val=val+"+"
                            else:

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
                if valor[0]=="0":
                    valor=valor[2:]
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

    
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ&"
matrices = []
matrices_alpha=[]
matrices_total=[]
for i in range(len(ABC)):
    matrices.append("NULL")
    matrices_alpha.append("NULL")
    matrices_total.append("NULL")
n=0



def menu():
    while True:
        print("Menú de opciones:")
        print("1. Leer matrices")
        print("2. Guardar matrices")
        print("3. Realizar operaciones con matrices")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            leer()
        elif opcion == "2":
            guardar()
        elif opcion == "3":
            operaciones(3)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida (1-4).")
    
def leer():
    fichero = open('entrada.txt')
    lineas = fichero.readlines()
    f=0
    for linea in lineas:
        valoresnum=[]
        valoresalpha=[]
        lin=linea.replace(" ","")
        lin=lin.replace("\n","")

        for i in range (len(lin)-2):
            
            if lin[i+2].isdigit():

                valoresnum.append(int(lin[i+2]))
                valoresalpha.append("")
            elif lin[i+2].isalpha():

                valoresalpha.append(lin[i+2])
                valoresnum.append(0)

        matrices[f] = Matrix(valoresnum, int(lin[0]), int(lin[1]))
        matrices_alpha[f] = Matrix(valoresalpha, int(lin[0]), int(lin[1]))
        matrices_total[f] = matrices[f].fusion_matrices(matrices_alpha[f])
        f=f+1
    fichero.close

#def guardar():




def operaciones(n):
    while n != "VOLVER":
        print("-----------------------------------------------------------------------------------------")
        print("VOLVER para volver al menu")
        n=input("Operación a realizar :")
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
                print(matrices[valor])
                print(matrices_alpha[valor])
                print(matrices_total[valor].__str__(prefix=ABC[valor]))



            
            elif n[3]=="-" and n[1]!="*":
                valor=ABC.index(n[0])
                valor1=ABC.index(n[2])
                valor2=ABC.index(n[4])

            
                matrices[valor] = matrices[valor1] - matrices[valor2]
                matrices_alpha[valor] = matrices_alpha[valor1].resta_alpha(matrices_alpha[valor2])
                matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor])

                print(matrices_total[valor].__str__(prefix=ABC[valor]))

            elif n[3]=="*" and n[2] not in ABC and n[4]!="*":
                print("adentro")
                valor=ABC.index(n[0])
                valor1=n[2]
                valor2=ABC.index(n[4])
                
                matrices[valor] = matrices[valor2] * int(valor1)  
                matrices_alpha[valor] = matrices_alpha[valor2].mul_alpha(valor1)
                print(matrices_alpha[valor])
                matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor])
                print(matrices_total[valor].__str__(prefix=ABC[valor]))

            elif n[3]=="*" and n[2] in ABC and n[4]in ABC:
                print("AAAAA")
                valor=ABC.index(n[0])
                valor1=ABC.index(n[2])
                valor2=ABC.index(n[4])

            
    
                matrices_total[valor] = matrices[valor1].mul2(matrices[valor2],matrices_alpha[valor1],matrices_alpha[valor2])
                print(matrices_total[valor].__str__(prefix=ABC[valor]))

            elif "**T" in n:
                valor=ABC.index(n[0])
                valor1=ABC.index(n[2])
                print(valor)
            
                matrices[valor] = Matrix.transpuesta(matrices[valor1])
                matrices_alpha[valor] = Matrix.transpuesta(matrices_alpha[valor1])
                matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor]) 
                print(matrices_total[valor].__str__(prefix=ABC[valor]))

            elif "SORT" in n and n[1]!="=":
                valor=ABC.index("&")
                valor1=ABC.index(n[4])

                
                matrices[valor],matrices_alpha[valor] = matrices[valor1].sort(matrices_alpha[valor1])
                matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor]) 
                print(matrices_total[valor].__str__(prefix=ABC[valor]))

            elif "SHOW" in n:
                for i in range (len(ABC)):
                    if matrices_total[i] != "NULL":
                        print(matrices_total[i].__str__(prefix=ABC[i]))
                    else:
                        pass



            elif "SHOW" in n and n[4]in ABC:
                valor=ABC.index(n[4])
                matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor]) 
                print(matrices_total[valor].__str__(prefix=ABC[valor]))

            elif "SORT" in n and n[1]=="=":
                valor=ABC.index(n[0])
                valor1=ABC.index(n[6])

                print(valor,valor1)
                
                matrices[valor],matrices_alpha[valor] = matrices[valor1].sort(matrices_alpha[valor1])
                matrices_total[valor] = matrices[valor].fusion_matrices(matrices_alpha[valor]) 
                print(matrices_total[valor].__str__(prefix=ABC[valor]))
            
            elif "DETERMINANT" in n:
                valor = ABC.index(n[0])
                det = matrices[valor].determinant()
                print(f"Determinante de la matriz {ABC[valor]}: {det}") 

            
            elif "**-1" in n:
                valor = ABC.index(n[0])
                inversa = matrices[valor].inverse()
                print(inversa)




                
        elif n[0]=="s" and n[1]=="o":
            print("SSSSSSSSSSSSSS")


Menu=menu()
Menu.run()