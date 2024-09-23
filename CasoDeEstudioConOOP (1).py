import os
import time
import random

class OrdenarLista():
    def __init__(self, ListaNum):
        self.__ListaNum = ListaNum

    def Seleccion(self):
        ListaParaSortear = self.__ListaNum
        Tamaño = len(ListaParaSortear)
        for i in range(0, Tamaño):
            min = i
            for j in range(i + 1, Tamaño):
                if ListaParaSortear[min] > ListaParaSortear[j]:
                    min = j
            aux = ListaParaSortear[i]
            ListaParaSortear[i] = ListaParaSortear[min]
            ListaParaSortear[min] = aux
            OrdenarLista.Imprimir(ListaParaSortear)
        

    def Insercion(self):
        ListaParaSortear = self.__ListaNum
        for i in range(len(ListaParaSortear)):
            for j in range(i,0,-1):
                if(ListaParaSortear[j-1] > ListaParaSortear[j]):
                    aux=ListaParaSortear[j]
                    ListaParaSortear[j]=ListaParaSortear[j-1]
                    ListaParaSortear[j-1]=aux
                    OrdenarLista.Imprimir(ListaParaSortear)

    def Rapido(self):
        ListaParaSortear = self.__ListaNum
        Tamaño = len(ListaParaSortear)
        OrdenarLista.RapidoFinal(ListaParaSortear, 0, Tamaño-1)

    def ParticionRapido(ListaParaSortear, Bajo, Alto):
        Pivote = ListaParaSortear[Alto]
        i = Bajo - 1
        for j in range(Bajo, Alto):
            if ListaParaSortear[j] <= Pivote:
                i += 1
                (ListaParaSortear[i], ListaParaSortear[j]) = (ListaParaSortear[j], ListaParaSortear[i])
                OrdenarLista.Imprimir(ListaParaSortear)
        (ListaParaSortear[i + 1], ListaParaSortear[Alto]) = (ListaParaSortear[Alto], ListaParaSortear[i + 1])
        OrdenarLista.Imprimir(ListaParaSortear)  
        return i + 1
 
    def RapidoFinal(ListaParaSortear, Bajo, Alto):
        if Bajo < Alto:
            pi = OrdenarLista.ParticionRapido(ListaParaSortear, Bajo, Alto)
            OrdenarLista.RapidoFinal(ListaParaSortear, Bajo, pi - 1)
            OrdenarLista.RapidoFinal(ListaParaSortear, pi + 1, Alto) 

    def Mezcla(self):
        ListaParaSortear = self.__ListaNum
        OrdenarLista.MezclaFinal(ListaParaSortear)

    def MezclaFinal(ListaParaSortear):
        if len(ListaParaSortear) > 1:
            mitad = len(ListaParaSortear)//2
            primera_mitad = ListaParaSortear[:mitad]
            segunda_mitad = ListaParaSortear[mitad:]
        
            OrdenarLista.MezclaFinal(primera_mitad)
            OrdenarLista.MezclaFinal(segunda_mitad)
            i = 0
            j = 0
            k = 0
            
            
            while i < len(primera_mitad) and j < len(segunda_mitad):
                if primera_mitad[i] < segunda_mitad[j]:
                    ListaParaSortear[k] = primera_mitad[i]
                    i += 1
                else:
                    ListaParaSortear[k] = segunda_mitad[j]
                    j += 1
                k += 1
                OrdenarLista.Imprimir(ListaParaSortear) 
                
            while i < len ( primera_mitad):
                ListaParaSortear[k] = primera_mitad[i]
                i += 1
                k += 1 
                OrdenarLista.Imprimir(ListaParaSortear)
                
            while j < len (segunda_mitad):
                ListaParaSortear[k] = segunda_mitad[j]
                j += 1
                k += 1
                OrdenarLista.Imprimir(ListaParaSortear)

    def Stalin(self):
        ListaParaSortear = self.__ListaNum
        for i in range(len(ListaParaSortear)):
            try:
                while True:
                    if not ListaParaSortear[i]<ListaParaSortear[i+1]:
                        ListaParaSortear.pop(i+1)
                        OrdenarLista.Imprimir(ListaParaSortear)    
                    else:
                        break
            except:
                break
    
    def Imprimir(ListaParaSortear):
        if Impresion[0]:
            print (ListaParaSortear)
            time.sleep(0.07)
            os.system("cls")

def CasoEstudio():
    print(f"En este proyecto podras interactuar con varios metodos de ordenamiento con listas de 15 numeros con un rango de 1 a 30\nAqui estan las opciones y configuraciones")
    print(f"1. Menu lista de numeros\n2. Metodos de ordenamiento\n3. Habilitar impresion de proceso\n4. Salir")
    print("Elige cualquiera de las 4 opciones")
    while True:
        OpcionConfig = IntroducirInt()
        os.system("cls")
        if OpcionConfig == 4:
            return
        OpcionDiccionario(Config, OpcionConfig, "5")
        MostrarOpciones("5")

def ListaMenu():
    print("Maneja tu lista de numeros actual")
    print(f"1. Ver la lista de numeros actual\n2. Llenar lista manualmente (15 numeros)\n3. Llenar lista con numeros aleatorios (15 numeros)\n4. Vaciar lista\n5. Volver al menu principal")
    print("Elige una de estas opciones")
    while True:
        OpcionLista = IntroducirInt()
        os.system("cls")
        if OpcionLista == 5:
            return
        OpcionDiccionario(ListaConfig, OpcionLista, "6")
        MostrarOpciones("6")

def VerListaNumeros():
    print(f"Aqui esta la lista actual\n{ListaGenerada}")
    
def Manual():
    ListaTamaño=len(ListaGenerada)
    if ListaTamaño == 15:
        os.system("cls")
        print("Parece que ya hay una lista existente, por favor vacia la lista")
        return
    print("Introduce 15 numeros enteros entre 1 y 30")
    while ListaTamaño < 15:
        Valor = IntroducirInt()
        if Valor >= 1 and Valor <= 30:
            ListaGenerada.append(Valor)
            ListaTamaño=len(ListaGenerada)
        else:
            print("Introduce un numero entre 1 y 30")
    os.system("cls")
    print("La lista ha sido llenada")
        
def Random():
    ListaTamaño=len(ListaGenerada)
    if ListaTamaño == 15:
        os.system("cls")
        print("Parece que ya hay una lista existente, por favor vacia la lista")
        return
    print("Llenando lista...")
    for e in range(15):
        Valor = random.randint(1, 30)
        print(Valor)
        time.sleep(0.05)
        ListaGenerada.append(Valor)
    os.system("cls")
    print("La lista ha sido llenada")

def Vaciar():
    ListaGenerada.clear()
    print("La lista ha sido vaciada")

def VerListaMenu():
    print(f"Aqui estan las opciones disponibles:\n1. Ver la lista de numeros actual\n2. Llenar lista manualmente (15 numeros)\n3. Llenar lista con numeros aleatorios (15 numeros)\n4. Vaciar lista\n5. Volver al menu principal")

def MetodosSorteo():
    ListaCheck = len(ListaGenerada)
    if ListaCheck == 0:
        print("Es necesario crear una lista para continuar")
        return
    print(f"Aqui estan los sorteos actuales\n1. Por seleccion\n2. Por insercion\n3. Ordenamiento Rapido\n4. Por mezcla\n5. Ordenamiento Stalin\n6. Volver al menu principal")
    print("Elige uno de estos sorteos")
    while True:
        ListaParaSortear = ListaGenerada[:]
        PreparacionLista = OrdenarLista(ListaParaSortear)
        OpcionSorteo = IntroducirInt()
        os.system("cls")
        if OpcionSorteo == 1:
            PreparacionLista.Seleccion()
            ImprimirLista(ListaParaSortear)
        elif OpcionSorteo == 2:
            PreparacionLista.Insercion()
            ImprimirLista(ListaParaSortear)
        elif OpcionSorteo == 3:
            PreparacionLista.Rapido()
            ImprimirLista(ListaParaSortear)
        elif OpcionSorteo == 4:
            PreparacionLista.Mezcla()
            ImprimirLista(ListaParaSortear)
        elif OpcionSorteo == 5:
            PreparacionLista.Stalin()
            ImprimirLista(ListaParaSortear)
        elif OpcionSorteo == 6:
            return
        elif OpcionSorteo == 7:
            VerSorteos()
        else:
            print("Parece que esa opcion no existe, intenta nuevamente (Presiona 7 para ver las opciones)")
        MostrarOpciones("7")

def VerSorteos():
    print(f"Aqui estan los sorteos disponibles:\n1. Por seleccion\n2. Por insercion\n3. Ordenamiento Rapido\n4. Por mezcla\n5. Ordenamiento Stalin\n6. Volver al menu principal")
    

def HabilitarImpresion():
    print(f"Al habilitar esta opcion, podras ver como el sorteo de la lista con 15 numeros ocurre en tiempo real\nHabilitar la impresion de proceso?\nHabilitar/Deshabilitar")
    while True:
        ImpresionCheck = str(input()).lower()
        os.system("cls")
        if ImpresionCheck == "habilitar" or ImpresionCheck == "deshabilitar":
            break
        else:
            print("(Solo escribe entre las palabras ""habilitar"" o ""deshabilitar"")")
            
    if ImpresionCheck == "habilitar":
        print("La impresion de proceso ha sido habilitada")
        Impresion[0] = True
    else:
        print("La impresion de proceso ha sido deshabilitada")
        Impresion[0] = False


def VerOpciones():
    print(f"Aqui estan las opciones disponibles:\n1. Menu lista de numeros\n2. Metodos de sorteo\n3. Habilitar impresion de proceso\n4. Salir")

Config = {1:ListaMenu, 2:MetodosSorteo, 3:HabilitarImpresion, 5:VerOpciones}

ListaConfig = {1:VerListaNumeros, 2:Manual, 3:Random, 4:Vaciar, 6:VerListaMenu}

ListaGenerada = []

Impresion = [False]


def IntroducirInt():
    try:
        NumInt = int(input())
    except:
        print("Introduce correctamente un numero")
    return NumInt

def OpcionDiccionario(OpcionDiccionario, OpcionUsuario, ListaOpciones):
    try:
        Opcion=OpcionDiccionario.get(OpcionUsuario)
        Opcion()
    except:
        print(f"Parece que esa opcion no existe, intenta nuevamente (Presiona {ListaOpciones} para ver las opciones)")

def MostrarOpciones(ListaOpciones):
    print(f"Ahora, elige cualquier opcion (Presiona {ListaOpciones} para ver la lista de opciones)")

def ImprimirLista(ListaParaSortear):
    print("La lista ha sido organizada")
    print(ListaParaSortear)

CasoEstudio()