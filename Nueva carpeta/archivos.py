def generar_csv_pacientes(path:str, lista:list):

    ''' 


    '''
    try:
        with open(path, "w", encoding ="utf8") as archivo:
        # Escribir datos de los pacientes
            encabezado = "nombre,apellido,edad,altura,dni,peso,grupo sanguineo,id\n"

            archivo.write(encabezado)
            for paciente in lista:
                linea = f"{paciente['nombre']},{paciente['apellido']},{paciente['edad']},{paciente['altura']},{paciente['dni']},{paciente['peso']},{paciente['grupo sanguineo']},{paciente['id']}\n"
                archivo.write(linea)
    except:
        print("error en agregar datos en el archivo")
import re
def parser_csv_pacientes(path:str)-> list:
    '''
    
    '''
    lista = []
    with open(path, "r", encoding="utf8") as archivo:
        lista=[]
        listas_registro= []
        for linea in archivo:
            registro = re.split(",|\n",linea)  # Dividir la línea en los datos del paciente
            listas_registro.append(registro)
        listas_registro.remove(listas_registro[0])
        for registro in listas_registro:
            diccionario={}
            diccionario["nombre"]=registro[0]
            diccionario["apellido"]= registro[1]
            diccionario["edad"]= int(registro[2])
            diccionario["altura"]=int(registro[3])
            diccionario["dni"]= int(registro[4])
            diccionario["peso"]=float (registro[5])
            diccionario["grupo sanguineo"] = (registro[6])
            diccionario["id"] = int(registro[7])
            lista.append(diccionario)
    return lista