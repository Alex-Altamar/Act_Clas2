#********************************
#*        MANEJO DE LISTAS      *
#********************************

def listas():
    lista1 = []
    lista2 = list()

    ListaConElementos = [30, 2000000, "Alexander Altamar", "Estudiante", "Universidad de la guajira", True, ["Ing.Sistemas","10mo Semestre",25]]

    ListaConElementos.remove("Estudiante") # elimina elemntro especifico de la lista
    print(ListaConElementos)
    #del ListaConElementos[2]#remueve elemento por posicion
    #ListaConElementos.insert(2,["sede riohacha", "Miguel Soto"]) # inserta elemento en posicion determinada
    #ListaConElementos.append(["Sede Riohacha", "Miguel soto"]) #Inserta arreglo dentro del arreglo
    #ListaConElementos.append("Sede Riohacha") #inserta elemento en el arreglo
    #ListaConElementos[1] = ListaConElementos[1]+200000 #adiciona cantidad a valor dentro del arreglo
    """"
    j=0 #inicializar la variable a usar en el ciclo
    while j < len(ListaConElementos):
        print(ListaConElementos[j])
        j+=1
    
    """

    #print(ListaConElementos[0:8:2]) #muestra elementos en posiciones pares de la lista [0:6:2] elementos impares de la lista
    #print(ListaConElementos[0:3]) #muestra un rango de elementos de una lista
    #print(ListaConElementos) #muestra todos los elementos
    #print(ListaConElementos[2]) #muesra elemento en la posicion indicada 
    #print(ListaConElementos[5][3])#[][] para mostar ellemento de la lista dentro de otra lista
    #print(ListaConElementos[-1][3]) #muestra el elemento final de la lista el otro [] es para mostar elemento de una lista dentro de otra lista

   
    """
    for i in range(len(ListaConElementos)):""" 
    """
        usa len para leer la lista completa y () un rango para un elemento especifico dentro de la lista
        """
    """ print(ListaConElementos[i])"""
    
def main():
    listas()


if __name__ == "__main__":
    main()