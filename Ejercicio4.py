from api.library import *

def main ():
   #Aplicacion de los diccionarios estos tienen propiedades y valores

   """
   #crea un diccionario en este caso persona
   persona = {
      "Nombre": "Alexander",
      "Apellidos": "Altamar Vanegas",
      "edad": 25
   
   """
   
   #crea un diccionario con 2 diccionarios dentro
   persona = {
      "Datos Personales": {
      "Nombre": "Alexander",
      "Apellidos": "Altamar Vanegas",
      "edad": 25
      },
      "Salarial":{
         "Salario": 1000000,
         "SubTransporte": 50000,
         "SubAlimentacion": 60000 
      }
   }
   

   #print(persona)
   print(f"Nombre: {persona['Datos Personales']['Nombre']} {persona['Datos Personales']['Apellidos']}")
   print(f"Salario: {persona['Salarial']['Salario']}")
   #print(persona["Salarial"])# muestra diccionario especifico desntro de otro diccionario
   #persona["Nombre"] = "Enrique" #cambio nombre del atributo en el diccionario
   #print(f"{persona['Nombre']}  {persona['Apellidos']}")#{} y espacio para separar los resultados en pantalla #muestra elementos especificos del diccionario



if __name__ == "__main__":
    main()