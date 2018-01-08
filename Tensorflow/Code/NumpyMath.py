'''
Created on 20.12.2017

@author: Maggi
'''
import numpy as np

def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y +a

print(add(1,2))
print(addFixedValue(1))
print("test")

#Liste ist gut um Sachen aufzulisten
L = [1,2,3]

for e in L:
    print(e)

#Array ist gut, wenn man Vektor operationen durchführen möchte
A = np.array([1,2,3])

for e in A:
    print(e)
    
print(2*A)
print(2*L)
print(A**2)
print(np.sqrt(A))
print(np.log(A))
print(np.exp(A))

#Marix
M = np.array([[1,2],[3,4]])
print(M[0][0] , "," , M[1,1])

a= np.array([[1,1],[1.5,4]])
b= np.array([2200,5050])

x= np.linalg.solve(a,b)
print(x)

#read csv
import pandas as pd
X = pd.read_csv("../Data/titanic.csv",header=5)
print("Zeilen und Spalten", X.shape , type(X),"\n")
print(X.info())
#ersten 5 Zeilen
print(X.head())
#In NP Array umwandeln
M = X.as_matrix()
print(type(M))