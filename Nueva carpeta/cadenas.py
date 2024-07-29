def eleminar_vocales(cadena:str):
   
   vocales=["a","e","i","o","u"]
   cadena_sin_vocales=""
   for i in range (len(cadena)):
      hay_vocal = False
      for j in range(len(vocales)):
         if  cadena[i] == vocales[j]:
            hay_vocal = True
      if hay_vocal == False:
            cadena_sin_vocales+= cadena[i]
   return cadena_sin_vocales
         


# sd=eleminar_vocales("hola")
# print(sd)
def encontrar_subcadenas_en_cadenas(cadena:str,subcadena:str):
   contador=0
   for i in range (len(cadena)):
      if cadena [i:i+len(subcadena)] == subcadena:
         contador+=1
   print(contador)
pan="hola pan panadero"
encontrar_subcadenas_en_cadenas(pan,"pan")

def eliminar_caracteres_repetidos_1(cadena:str):
   cadena_eliminada=""
   for i in range(len(cadena)):
      if cadena[i] not in  cadena_eliminada:# busqueda  otro for  y un if una bandera
         cadena_eliminada+=cadena [i]
   print(cadena_eliminada)
hola="h0laaaaa"
def eliminar_caracteres_reptidas(cadena:str):
   cadena_eliminada = ""
   for i in range(len(cadena)):
      print(i)
