# -*- coding: utf-8 -*-
"""

@author: lara Sanchez

"""

#Importar las librerias necesarias
import pandas as pd
#Clasificador a utilizar: NB
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
#Función que crea los conjuntos de Pruebas y de Entrenamiento
from sklearn.model_selection import train_test_split
#Función que nos devolverá las diferentes métricas del clasificador 
from sklearn import metrics 
from sklearn.metrics import accuracy_score

#Leer los datos tratados
datasetCSVMean = pd.read_csv("DataPorSesion/Model4FeaturesMean.csv") #80.24691358024691 %
datasetCSVMedian = pd.read_csv("DataPorSesion/Model4FeaturesMedian.csv") #79.01234567901234 %
datasetCSV = pd.read_csv("DataPorSesion/Model8Features.csv") #82.71604938271605 %

#Convertirlos con Numpy
dataMean = datasetCSVMean.to_numpy()
dataMedian = datasetCSVMedian.to_numpy()
data = datasetCSV.to_numpy()

#El target es el mismo para los tres (Los usuarios)
target = []
#Las features seran distintas
dataProcMean = []
dataProcMedian = []
dataProc = []

for i in range(len(dataMean)):
    target.append(data[i][8])
    dataProcMean.append([data[i][0], 
                     data[i][1],
                     data[i][2],
                     data[i][3]
            ])

for i in range(len(dataMedian)):    
    dataProcMedian.append([data[i][0], 
                     data[i][1],
                     data[i][2],
                     data[i][3]
            ])
    
for i in range(len(data)):    
    dataProc.append([data[i][0], 
                     data[i][1],
                     data[i][2],
                     data[i][3],
                     data[i][4], 
                     data[i][5],
                     data[i][6],
                     data[i][7]
            ])


#Crear los array de target y feature
XMean = dataProcMean
XMedian = dataProcMedian
X = dataProc
y = target

#Dividir el conjunto en training data y test data
#80% Training 20% Test 
X_trainMean, X_testMean, y_trainMean, y_testMean = train_test_split(
             XMean, y, test_size = 0.2, random_state=44)

X_trainMedian, X_testMedian, y_trainMedian, y_testMedian = train_test_split(
             XMedian, y, test_size = 0.2, random_state=44)

X_train, X_test, y_train, y_test = train_test_split(
             X, y, test_size = 0.2, random_state=12)


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
clf = GaussianNB()
clf.fit(X_train, y_train)
y_pred  =  clf.predict(X_test)
ac = accuracy_score(y_test,y_pred)
print(round(ac*100,2),"%")

scMean = StandardScaler()
X_trainMean = scMean.fit_transform(X_trainMean)
X_testMean = scMean.transform(X_testMean)
clfMean = GaussianNB()
clfMean.fit(X_trainMean, y_trainMean)
y_predMean  =  clfMean.predict(X_testMean)
acMean = accuracy_score(y_testMean,y_predMean)
print(round(acMean*100,2),"%")

scMedian = StandardScaler()
X_trainMedian = scMedian.fit_transform(X_trainMedian)
X_testMedian = scMedian.transform(X_testMedian)
clfMedian = GaussianNB()
clfMedian.fit(X_trainMedian, y_trainMedian)
y_predMedian  =  clfMedian.predict(X_testMedian)
acMedian = accuracy_score(y_testMedian,y_predMedian)
print(round(acMedian*100,2),"%")

from sklearn import metrics
labels = []
for label in y_test:
    if not label in labels:
        labels.append(int(label))
labels.sort()
metrics.plot_confusion_matrix(clf, X_test, y_test, display_labels=labels).ax_.set(xlabel='Valores Predichos', ylabel='Valores Verdaderos', title="8 Características")


labelsMean = []
for label in y_testMean:
    if not label in labelsMean:
        labelsMean.append(int(label))
labelsMean.sort()
metrics.plot_confusion_matrix(clfMean, X_testMean, y_testMean, display_labels=labelsMean).ax_.set(xlabel='Valores Predichos', ylabel='Valores Verdaderos', title="4 Medias")


labelsMedian = []
for label in y_testMedian:
    if not label in labelsMedian:
        labelsMedian.append(int(label))
labelsMedian.sort()
metrics.plot_confusion_matrix(clfMedian, X_testMedian, y_testMedian, display_labels=labelsMedian).ax_.set(xlabel='Valores Predichos', ylabel='Valores Verdaderos', title="4 Medianas")


y_pred = clf.predict(X_test)
y_predMean = clfMean.predict(X_testMean)
y_predMedian = clfMedian.predict(X_testMedian)
print("8 Características")
print(metrics.classification_report(y_test, y_pred, digits=3, labels = labels, zero_division = 0))
print("4 Medias")
print(metrics.classification_report(y_testMean, y_predMean, digits=3, labels = labelsMean, zero_division = 0))
print("4 Medianas")
print(metrics.classification_report(y_testMedian, y_predMedian, digits=3, labels = labelsMedian, zero_division = 0))



