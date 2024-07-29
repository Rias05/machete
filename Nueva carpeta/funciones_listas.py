from ordenamiento import*
def validar_elementos_lista(lista:list,mensaje:str,mensaje_error): 

    dato = input(mensaje)
    retorno = ""
    bandera = True

    while bandera:
        for i in lista:

            if i == dato:
                retorno = i
                bandera = False

            else:
                dato = input(mensaje_error)

    return retorno 
# prueba = validar_elementos_lista(["hola"],"envia wey","error wey")
# print(prueba)
def elemento_mayor(lista:list):
    if type(lista) == list:
        maximo = 0
        for i in lista :
            if i > maximo:
                maximo = i
    else:
        print("se necesita una lista")
    return maximo
def sumar_elementos(lista):
    acumulador = 0
    if type(lista) == list:
    
        for i in lista:
            acumulador+=i
    return acumulador
def invertir_lista(lista:list):
    lista_invertida = []
    for i in range(len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])
    return lista_invertida
 

# lista_invertida = invertir_lista([1,2,3,4,5])
# print(lista_invertida)

def eliminar_duplicados(lista: list) -> list:
    sin_duplicado = []
    for i in range(len(lista)):
        duplicado = False
        for j in range(len(sin_duplicado)):
            if  sin_duplicado[j] != lista[i]:
                duplicado = False
            else:
                duplicado = True
    
        if duplicado == False :

            sin_duplicado.append(lista[i])
    return sin_duplicado
print(eliminar_duplicados([1,1,1,1,1,12,2]))

def indice_de_una_lista(lista:list,elemento):
    retorno = ""
    for i in range (len(lista)):
        if lista[i] == elemento:
            retorno = i
    return retorno

#
def rotar_lista(lista:list,n:int):
    lista_rotada=[None]* len(lista)

    for i in range(len(lista)):
        
        nueva_posicion = i+2 % len(lista)
        lista_rotada[nueva_posicion]== lista[i]
def segundo_elemento_mayor(lista:list):
    segundo_maximo = 0
    maximo = 0
        
    for i in lista:
        if i > maximo:
            lista.remove(i)
        
    for i in lista:
        if i > segundo_maximo:
            segundo_maximo = i
    return segundo_maximo

        
print(segundo_elemento_mayor([1,2,2,3]))

def calcular_promedio(lista:list[dict],clave:str):
    contador = 0
    acumulador = 0
    for i in lista:
        acumulador += i[clave]
        contador+=1
    promedio = int(acumulador/contador)
    return promedio
        

datos = [
    {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 25, "ciudad": "Barcelona"},
    {"nombre": "Carlos", "edad": 35, "ciudad": "Madrid"},
    {"nombre": "Laura", "edad": 28, "ciudad": "Barcelona"},
    {"nombre": "Pedro", "edad": 40, "ciudad": "Madrid"}
]

diccioanrio = {}
datos = ordenar_lista(datos,"edad",True)
contador=0
acumulador=0
for i in datos:
    registro = i
    esta = False
    ciudad = i["ciudad"]
    for j in diccioanrio:
        if j != ciudad:
            esta == False
        else:
            esta = True
    if esta == False and ciudad:
        diccioanrio[ciudad]= {"personas": [], "promedio":0}
    diccioanrio[ciudad]["personas"].append(registro)
    personas = i


for i in diccioanrio:
    acumulador = 0
    contador = 0
    personas = diccioanrio[i]["personas"]
    for j in personas:
        contador += 1
        acumulador += j["edad"]
# print(contador,acumulador)
    promedio =acumulador/ contador
    diccioanrio[i]["promedio"] = promedio
print(diccioanrio)
# print(promedio)
# for ciudad, info in diccioanrio.items():
#         print( info["personas"])
        



# for i in diccioanrio:
#     lista = diccioanrio[i]["personas"]
#     print(lista)
#     for i in lista:
#         # print(i)
#         pass







        
    
