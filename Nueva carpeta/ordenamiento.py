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