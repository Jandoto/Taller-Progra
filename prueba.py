def separar_letras_numeros(texto):
    resultados = []

    for elemento in texto:
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

        resultados.append((letra, numero))

    return resultados


texto = ["A1", "12B", "C"]
resultados = separar_letras_numeros(texto)
print(resultados[1][0])
print(len(resultados))
