def ordenar_lista(lista:list[dict], valor:str, ascendente:bool):
    '''
    recibo la lista con los diccionarios un valor que sera el criterio a ordenar y el ascendente se recorrer la lista la cantidad de de elemntos de la lista recorre  con el primer for la cantidad de veces que lo hara el segundo  es para recorrer las posiciones lo siguinte es la parte que ordenadara mediante la psocion y la clave compara el elemento con el que esta despues de el si es ascendente intercambia los valores derecha  izq

    '''
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if ascendente :
                    if lista[j][valor] > lista[j+1][valor]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
                    if lista[j][valor] < lista[j+1][valor]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista
'''
# 1. Crear una función que permita leer cada línea del archivo csv y convertir cada lectura en una matriz de
3X3.
# 2. Crear una función que reciba la matriz anterior y la muestre.
# 3. Crear una función que analice el contenido de la matriz y determine si gano la X, la O o si hubo empate.
# (Tienen que hacer varias funciones para analizar las líneas verticales, horizontales o diagonales).
# Repetir el punto 2 y 3 por cada línea del archivo.
# 4. Antes de finwalizar el programa mostrar las estadísticas:
# Cuántas veces ganó la X
# Cuántas veces ganó la O
# Cuántas veces hubo empate
'''
import re
def leer_csv(path:str) -> list :

    matricez = []

    with open(path, "r","utf-8") as archivo

      for linea en archivo:
          matriz  = []


          registro = re.split(",|\n",linea)
          
          for i in range(0,9,3)
              pasaje =[registro[i:i+3]]
              matriz.append( pasaje)
              matricez.append(matriz)

          



    return matriz

# ejercicio integrador
def imprimir_matriz(matriz:list[list]):
    for fila in matriz:
        
        for columna in fila:
            
            print(f"{columna:14}|",end= " ")
        
        print("")
matriz = for [0]*3 in range(3)
imprimir  = imprimir_matriz ( matriz)

def determinar_operacion(matriz:list)

   contador_x = 0
   contador_o = 0
   lista_resultado =[]

   for filas in matriz:
       
       for columnas un filas:
            
            if matriz[fila][columnas] == x 
                
                contador_x += 1
            elif matriz[fila][columna] == o
                
                contador_o += 1
    
    lista_resultado = [contador_o, contador_x]
motrar_comptibilidad =34
def comprobacion( lista:list, elemento, elemento_2)
 
 contador = 0
 contador_2 = 0
 lista = []

 for i in lista:
     
     if i == elemento :
       
      contador = +=1
     elif i == elemento_2
      
      contador_2+=1
lista = [ contador,contador_2]

return lista

def lineas_verticales( matriz:list):
    
    
    lista_1 = []
    lista_2 = []
    lista_3 = []
    posicion = 0
    for  i in range(matriz:list):
        
        columas_1 = matriz[i][0] 
        lista_1.append( columnas_1)
        columnas_2 = matriz[i][1]
        columnas_3 = matriz[i][2]
        lista_2.append( columnas_2)
        lista_3.append( columnas_3)
    
    comprobar_1 = comprobacion (lista_1,)


print(2)
