# -*- coding: utf-8 -*-
"""
@author: Lara Sánchez

"""

#Librerias

import pandas as pd
import numpy as np


#==============================================================================
#Leer el CSV con los datos
def leerDataSet(ruta):
    
    datasetCSV = pd.read_csv(ruta)
    datasetNP = datasetCSV.to_numpy()
    
    return datasetNP
#==============================================================================
#Tiempo de Permanencia
#KeyDown 1 - KeyUp 1
#Input: Matriz con los datos de una sola sesión. 
#[[Registro1],[Registro2],[...],[RegistroN]]
#Output: Tiempo que pasa entre la pulsación de una tecla y al soltarla 
#[T1, T2, T3... TN]
def Down_Up(DataSet):
    
    rango = (len(DataSet))
    #Variable que se usa para buscar dentro de la sesion
    indexSplit = 0
    #Resultado a devolver
    TDown_Up = []
    
    #Por cada registro de la sesion
    for i in range(rango):
        
        #Si la acción es "Pulsar"
        if(DataSet[i][0] == 'keydown'):
            
            #Buscamos la siguiente acción "Soltar" de la misma tecla
            #Guardamos la telca que se pulsó
            keyAnterior = DataSet[i][2]
            #Guardamos el tiempo en el que se pulsó
            tiempoAnterior = DataSet[i][1]
            #Desde el momento que se pulsa la tecla y con la variable indexSplit
            #Buscamos en el resto de la sesión cuándo se suelta la tecla
            busqueda = DataSet[indexSplit:]
            #Variable que permitirá cortar el bucle cuando se encuentre la tecla
            Bandera = False 
            #Iteramos en el segundo bucle 
            for n_busqueda in range(len(busqueda)):
                #Si la acción es Soltar y además la tecla coincide con la tecla pulsada
                if(busqueda[n_busqueda][0] == 'keyup' and busqueda[n_busqueda][2] == keyAnterior and not Bandera):
                    
                    #Guardamos el tiempo donde se soltó la tecla
                    tiempoKeySiguiente = busqueda[n_busqueda][1]                    
                    #Verificamos que el tiempo de silencio sea menor o igual a 300ms
                    if(tiempoKeySiguiente-tiempoAnterior <= TiempoSilencio):
                        #Guardamos el tiempo que ha transcurrido entre las dos acciones
                        TDown_Up.append(tiempoKeySiguiente-tiempoAnterior)
                    
                    Bandera = True
            
        #Aumentamos la variable que divide la sesion   
        indexSplit = indexSplit + 1
    #Devolvemos todos los tiempos que transcurren
    return TDown_Up
#==============================================================================
#Tiempo entre Retenciones
#KeyDown 1 - KeyDown 2
#Input: Matriz con los datos de una sola sesión. 
#[[Registro1],[Registro2],[...],[RegistroN]]
#Output: Tiempo que pasa entre la pulsación de una tecla y pulsación de otra
#[T1, T2, T3... TN]
def Down_Down(DataSet):
    
    rango = (len(DataSet))
    #Variable que se usa para buscar dentro de la sesion
    indexSplit = 0
    #Resultado a devolver
    TDown_Down = []
    #Por cada registro de la sesion
    for row in range(rango):
        
        indexSplit = indexSplit + 1  
        #Si la accion de la tecla es "pulsar"
        if(DataSet[row][0] == 'keydown'):
            #Se guarda el tiempo en el que se pulsó
            tiempoInicial = DataSet[row][1]
            #Se divide la sesion para buscar la siguiente pulsación
            busqueda = DataSet[indexSplit:]
            
            for n_busqueda in range(len(busqueda)):
                #Si la accion de la siguiente tecla es "pulsar"
                if(busqueda[n_busqueda][0] == 'keydown'):
                    
                    #Se guarda el momento en el que se pulsó 
                    tiempoKeySiguiente = busqueda[n_busqueda][1]
                    #Verificamos que el tiempo de silencio sea menor o igual a 300ms
                    if(tiempoKeySiguiente-tiempoInicial <= TiempoSilencio):
                        #Guardamos el tiempo que ha transcurrido entre las dos acciones
                        TDown_Down.append(tiempoKeySiguiente-tiempoInicial)
                    #Salimos del bucle
                    break
    #Devolvemos los tiempos que transcurren
    return TDown_Down
#==============================================================================    
#Tiempo de Cambio
#KeyUp 1 - KeyDown 1
#Input: Matriz con los datos de una sola sesión. 
#[[Registro1],[Registro2],[...],[RegistroN]]
#Output: Tiempo que pasa entre soltar una tecla y pulsación de otra
#[T1, T2, T3... TN]
def Up_Down(DataSet):
        
    rango = (len(DataSet))
    #Variable que se usa para buscar dentro de la sesion
    indexSplit = 0
    #Resultado a devolver
    TUp_Down = []
    
    #Por cada registro de la sesion
    for row in range(rango):
        
        indexSplit = indexSplit + 1
        #Si la accion de la tecla es "soltar"
        if(DataSet[row][0] == 'keyup'):
            #Se guarda el tiempo en el que se soltó
            tiempoInicial = DataSet[row][1]
            #Se divide la sesion para buscar la siguiente "soltura"
            busqueda = DataSet[indexSplit:]
            
            for n_busqueda in range(len(busqueda)):
                 #Si la accion de la siguiente tecla es "pulsar"
                if(busqueda[n_busqueda][0] == 'keydown'):
                    
                    #Se guarda el momento en el que se pulsó 
                    tiempoKeySiguiente = busqueda[n_busqueda][1]
                    #Verificamos que el tiempo de silencio sea menor o igual a 300ms
                    if(tiempoKeySiguiente-tiempoInicial <= TiempoSilencio):
                        #Guardamos el tiempo que ha transcurrido entre las dos acciones
                        TUp_Down.append(tiempoKeySiguiente-tiempoInicial)
                    #Salimos del bucle
                    break
    #Devolvemos los tiempos que transcurren
    return TUp_Down
#==============================================================================    
#Tiempo entre Liberaciones
#KeyUp 1 - KeyUp 1
#Input: Matriz con los datos de una sola sesión. 
#[[Registro1],[Registro2],[...],[RegistroN]]
#Output: Tiempo que pasa entre soltar una tecla y pulsación de otra
#[T1, T2, T3... TN]
def Up_Up(DataSet):
        
    rango = (len(DataSet))
    #Variable que se usa para buscar dentro de la sesion
    indexSplit = 0
    #Resultado a devolver
    TUp_Up = []
    
    #Por cada registro de la sesion
    for row in range(rango):
        indexSplit = indexSplit + 1  
        #Si la accion de la tecla es "soltar"
        if(DataSet[row][0] == 'keyup'):
            #Se guarda el tiempo en el que se soltó
            tiempoInicial = DataSet[row][1]
            #Se divide la sesion para buscar la siguiente "soltura"
            busqueda = DataSet[indexSplit:]
            
            for n_busqueda in range(len(busqueda)):
                #Si la accion de la siguiente tecla es "soltar"
                if(busqueda[n_busqueda][0] == 'keyup'):
                    
                    #Se guarda el momento en el que se pulsó 
                    tiempoKeySiguiente = busqueda[n_busqueda][1]
                    #Verificamos que el tiempo de silencio sea menor o igual a 300ms
                    if(tiempoKeySiguiente-tiempoInicial <= TiempoSilencio):
                        #Guardamos el tiempo que ha transcurrido entre las dos acciones
                        TUp_Up.append(tiempoKeySiguiente-tiempoInicial)
                    #Salimos del bucle
                    break
    #Devolvemos los tiempos que transcurren
    return TUp_Up
#==============================================================================
#Input: Sesion 
#[[Registro1],[Registro2],[...],[RegistroN]]
#Outpu: Sesion divida cada 1 min
#[[Division1],[Division2],[...],[Division3]]
def SplitEvery6000ms(lista):
    
    rango = (len(lista))
    indexSplit = 0
    #Guardamos el primer tiempo
    tiempoInicial = lista[0][1]
    Split = []
    #Por cada registro de la sesion
    for row in range(rango):
        indexSplit = indexSplit + 1  
        #Vemos si la diferencia entre el tiempo inicial + 60000 ms es menor al siguiente tiempo
        if(tiempoInicial+60000 < lista[row][1]):
            #Si se cumple, dividmos la sesion 
            Split.append(lista[indexSplit:])
            #Asignamos un nuevo tiempo inicial 
            tiempoInicial = lista[row][1]
    #Devolvemos la sesion dividida
    return Split   
#==============================================================================
#Tratamiento de datos
def TratamientoGeneral():
    #Por cada sesion realizada
    for user in ["1A", "1B", "1C","1D","1E","1F","1G","1H","1I","1J","1K","1L",
                 "2A", "2B",
                 "3A", "3B", "3C","3D","3E","3F","3G",
                 "4A", "4B", "4C","4D","4E",
                 "5A", "5B", "5C","5D","5E",
                 "6A", "6B", "6C","6D","6E","6F","6G","6H","6I","6J",
                 "7A", "7B", "7C","7D","7E",
                 "8A", "8B", "8C","8D","8E",
                 "9A", "9B", "9C","9D",
                 "10A",
                 "11A", "11B", "11C"]:
        #Obtenemos el usuario que ha realizado la sesion por el nombre del archivo
        #Si el nombre del archivo tiene menos de 3 digitos es un usuario del 1 al 9
        if len(user) >= 3:
            word = [user[i:i+2] for i in range(0, len(user), 2)]
        #Si el nombre del archivo tiene mas de 3 digitos es el usuario 10 u 11
        else:
            word = [user[i:i+1] for i in range(0, len(user), 1)]
        
        #Accedemos a la ruta donde se encuentra la sesion
        ruta = "DataPorSesion/data"+str(user)+".csv"
        #Utilizamos el método que lee la sesión 
        DataSet = leerDataSet(ruta)
        #Dividimos la sesion cada 1 min
        Splited = SplitEvery6000ms([DataSet][0])
        index = 1
        #Por cada división de la sesión
        for array in Splited:
            #Usamos el método para calcular el tiempo de Permanencia
            TDU = Down_Up(list(array))
            
            #Usamos el método para calcular el tiempo entre Liberaciones
            TUU = Up_Up(list(array))
            
            #Usamos el método para calcular el tiempo de entre Retenciones
            TDD = Down_Down(list(array))
            
            #Usamos el método para calcular el tiempo de Cambios
            TUD = Up_Down(list(array))
            
            #Verificamos los conjuntos con pocos datos
            if(len (TDU) > 10 and len (TUU) > 5 and 
               len (TDD) > 5 and len (TUD) > 5  ):
                
                #Calcuamos la media, la desviacion típica y mediana del tiempo de permanencia            
                TDUMean = float(round(np.mean(np.array(TDU), dtype=np.float64),10))
                TDUStd  = float(round(np.std(np.array(TDU)),10))
                TDUMedian = float(round(np.median(np.array(TDU)),10))
                
                #Calcuamos la media y la desviacion típica del tiempo entre Liberaciones
                TUUMean = float(round(np.mean(np.array(TUU), dtype=np.float64),10))
                TUUStd  = float(round(np.std(np.array(TUU)),10))
                TUUMedian = float(round(np.median(np.array(TUU)),10))
                
                #Calcuamos la media y la desviacion típica del tiempo de cambio
                TUDMean = float(round(np.mean(np.array(TUD), dtype=np.float64),10))
                TUDStd  = float(round(np.std(np.array(TUD)),10))
                TUDMedian = float(round(np.median(np.array(TUD)),10))
                
                #Calcuamos la media y la desviacion típica del tiempo de entre Retenciones
                TDDMean = float(round(np.mean(np.array(TDD), dtype=np.float64),10))
                TDDStd  = float(round(np.std(np.array(TDD)),10))
                TDDMedian = float(round(np.median(np.array(TDD)),10))
                
                #Ver si la desviacion tipica es menor o igual a 37ms
                #Quitar los outliers
                if(int(round(np.std(np.array(TDU)),0)) <= 37):
                    
                #Guardamos los tiempos junto al usuario que lo realiza 
                    Model8Features.append([
                                     TDUMean,
                                     TDUStd,
                                     TUUMean,
                                     TUUStd,
                                     TDDMean,
                                     TDDStd,
                                     TUDMean,
                                     TUDStd,
                                     word[0]
                                    ])

                    Model4FeaturesMean.append([
                                     TDUMean,
                                     TUUMean,
                                     TDDMean,
                                     TUDMean,
                                     word[0]
                                    ])

                    Model4FeaturesMedian.append([
                                     TDUMedian,
                                     TUUMedian,
                                     TDDMedian,
                                     TUDMedian,
                                     word[0]
                                    ])
            index = index + 1   
            #np.mean(np.array(list(array)), dtype=np.float64), np.std(np.array(list(array))) 
            

#==============================================================================
# Main
#==============================================================================   
if __name__ == '__main__':
    #Tiempo de Silencio Max 300 ms
    TiempoSilencio = 300
    #Modelo 8 Caracterisictas
    #TP Media
    #TP Varianza
    #TC Media
    #TC Varianza
    #TER Media
    #TER Varianza
    #TEL Media
    #TEL Varianza
    #Usuario
    Model8Features = []
    
    #Modelo 4 Caracterisictas Medias
    #TP Media
    #TC Media
    #TER Media
    #TEL Media
    #Usuario
    Model4FeaturesMean = []
    
    #Modelo 4 Caracterisictas Medianas
    #TP Mediana
    #TC Mediana
    #TER Mediana
    #TEL Mediana
    #Usuario
    Model4FeaturesMedian = []
    
    #Llamada al método principal
    TratamientoGeneral()
    
    #Guardar los modelos
    np.savetxt("DataPorSesion/Model8Features.csv", Model8Features, delimiter=",", fmt='%s')
    np.savetxt("DataPorSesion/Model4FeaturesMean.csv", Model4FeaturesMean, delimiter=",", fmt='%s')
    np.savetxt("DataPorSesion/Model4FeaturesMedian.csv", Model4FeaturesMedian, delimiter=",", fmt='%s')
