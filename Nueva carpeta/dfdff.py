#Deberán crear una matriz que indique en la primera columna cada uno de los tipos
#sanguíneos, en la segunda a cuántas personas pueden donar y en la tercera de cuántas
#personas pueden recibir ese tipo, asegurarse que el desarrollo cuente con funciones
#minificadas y reutilizables. Realizar una función que reciba la matriz y la muestre.

    
compatibilidad = {
    "O-": [["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], ["O-"]],
    "O+": [["A+", "B+", "AB+", "O+"], ["O+", "O-"]],
    "A-": [["A+", "A-", "AB+", "AB-"], ["A-", "O-"]],
    "A+": [["A+", "AB+"], ["A+", "A-", "O+", "O-"]],
    "B-": [["B+", "B-", "AB+", "AB-"], ["B-", "O-"]],
    "B+": [["B+", "AB+"], ["B+", "B-", "O+", "O-"]],
    "AB-": [["AB+", "AB-"], ["AB-", "A-", "B-", "O-"]],
    "AB+": [["AB+"], ["AB+", "AB-", "A+", "A-", "B+", "B-", "O+", "O-"]]
}
pueden_donar = ["A+", "B+", "AB+", "O+"]
pacientes = [
    {'nombre': 'justin', 'apellido': 'prado', 'edad': 45, 'altura': 180, 'dni': 94996106, 'peso': 45.6, 'grupo sanguineo': 'A+', 'id': 1},
    {'nombre': 'sad', 'apellido': 'sad', 'edad': 94, 'altura': 23, 'dni': 94996108, 'peso': 34.0, 'grupo sanguineo': 'A+', 'id': 3},
    {'nombre': 'seiya', 'apellido': 'pegaso', 'edad': 100, 'altura': 180, 'dni': 94996105, 'peso': 45.0, 'grupo sanguineo': 'A+', 'id': 4}
]
def validar_dato(lista:list,dato:str):
    retorno = False
    for i in lista:
        if dato == i:
            retorno = True
        pass
    return retorno


    

tipos_de_sangre = ["A+", "A-", "B+", "B-","AB+", "AB-", "O+", "O-"] 
# filas = len(tipos_de_sangre)
# columnas = 3
# matriz = [[0]* columnas for _ in range (filas)] # hace una matriz de puros 0
# for fila in range(len(matriz)):
#     matriz[fila][0] = tipos_de_sangre[fila]
#     matriz[fila][1] = 4

# print(matriz)

def contar_repeticiones(lista_general:list,lista_secundaria:list):
    lista_de_contadores = []
    # lista_de_contadores = [0]* len(lista_general)
    for i in range(len(lista_general)):
        contador = 0
        for j in lista_secundaria:
            if j == lista_general[i]:
                contador += 1
                # lista_de_contadores[i] = contador
        lista_de_contadores.append(contador)

    return lista_de_contadores

def traspasar_datos(lista:list,almacenar:list):
    
    for i in lista:
        almacenar.append(i)
    return almacenar

def repeticiones(lista:list,lista2:dict,clave:str,):

    total_cantidad_doanantes = []
    total_cantidad_receptores = []

    for i in lista:
        grupo_sanguineo = i[clave]

        for j in tipos_de_sangre:
                
                extracion = lista2[j][0]
                extracion_2 = lista2[j][1]
                for donante in extracion:
                    contador = 0
                    
                    if donante == grupo_sanguineo:
                        contador +=1
                        cantidad = [j]*(contador)
                        traspasar_datos(cantidad,total_cantidad_doanantes)
                # total_cantidad_doanantes.append(cantidad)
                
                for receptor in extracion_2:
                    contador_2 = 0
                    if receptor == grupo_sanguineo:
                        contador_2+=1
                        cantidad_2 = [j]*contador_2
                # total_cantidad_receptores.append(cantidad_2)
                        traspasar_datos(cantidad_2,total_cantidad_receptores)

    guardar = [total_cantidad_doanantes,total_cantidad_receptores]    

    return guardar
            
shi = repeticiones(pacientes,compatibilidad,"grupo sanguineo")
def matriz_compatibilidad(lista:list,lista_2:list):
    tipos_de_sangre = ["A+", "A-", "B+", "B-","AB+", "AB-", "O+", "O-"] 
    filas = len(tipos_de_sangre)
    columnas = 3
    matriz = [[0]* columnas for _ in range (filas)] # hace una matriz de puros 0
    for fila in range(len(matriz)):
        matriz[fila][0] = tipos_de_sangre[fila]
        matriz[fila][1] = lista[fila]
        matriz [fila][2] = lista_2[fila]
    return matriz
lista_donantes = contar_repeticiones(tipos_de_sangre,shi[0])
print(lista_donantes)
lista_receptoes = contar_repeticiones(tipos_de_sangre,shi[1])
matriz_compa = matriz_compatibilidad(lista_donantes,lista_receptoes)


def imprimir_matriz(matriz:list[list]):
    for fila in matriz:
        for columna in fila:
            print(f"{columna:14}|",end= " ")
        print("")
imprimir_matriz(matriz_compa)
