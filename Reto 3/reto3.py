# -*- coding: utf-8 -*-
"""reto3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VIxhXYotxDcM7-lgFo0g7QIK-smepVkJ
"""

"""Reto3"""
"""=======================================INICIALIZACIONES========================="""

bandera = True
n=[]#lista vacia de cantidad de sucursales
m=[]#lista vacia de cantidad de pacientes



"""=======================================FUNCIONES========================="""

def cambiar_tipo_int(lista):#Funcion que cambia los str de una lista a tipo  int
  for i in range(len(lista)):
    lista[i] = int(lista[i])
  return lista

def sucursal_min(lista_de_sucursales):#Funcion para sacar la sucursal minima y su respectiva posicion
  minimo = min(lista_de_sucursales)
  for i in range(len(lista_de_sucursales)):
    if lista_de_sucursales[i] == minimo:
      posicion = i+1
    else:
      continue  
    posicion = str(posicion)
    minimo = str(minimo)
    resultado = [posicion, minimo]
    return (" ".join(resultado))#La funcion join convierte la lista en un str

def sucursal_max(lista_de_sucursales):#Funcion para sacar la sucursal minima y su respectiva posicion 
  maximo = max(lista_de_sucursales)
  for i in range(len(lista_de_sucursales)):
    if lista_de_sucursales[i] == maximo:
      posicion = i+1
    else:
      continue
    posicion = str(posicion)
    maximo = str(maximo)
    resultado = [posicion, maximo]
    return (" ".join(resultado))

def proporcion_porcentual(lista_inicial, lista_final):#Funcion que saca la proporcion porcentual
  pos = 0                                             #de medicamentos inicial respecto a los entregados
  resultado = []
  for elemento in lista_inicial:
    resta = elemento - lista_final[pos]
    proporcion = (100/elemento)*resta
    resultado.append(proporcion)
    pos += 1
  return resultado
  

"""======================================CUERPO================================="""

while bandera:
  entrada = input()#recibe n=cantidad de sucursales y m=cantidad de pacientes
  entrada = entrada.split()#separa los dos valores y hacce a entrada una lista
                           #donde el elemento del indice 0 es n 
                           #y el elemento del indice 1 es m 
  entrada = cambiar_tipo_int(entrada)#funcion que cambia los str de una lista a tipo  int
  if entrada[0] >= 1:
    bandera = False
    for i in range(entrada[0]):
      siwtch = True
      while siwtch:
        valor_1 = int(input())#cantidad de medicamentos de 1 a n sucursales
        if valor_1 >= 1:
          n.append(valor_1)
          siwtch =False
        else:
          siwtch = True

n_inicial = n[:]#copia de la cantidad inicial de medicamentos por sucursales

for p in range(entrada[1]):
  m = (input())#Le pide el numero de la sucursal y las presiones al paciente
  m = m.split()
  cambiar_tipo_int(m)
  
  if m[0] in range(1,len(n)+1):#si m[0]=sucursal ingresada por el paciente; esta en el rango de 1 hasta len(n)
    if (m[1] < 90) and (m[2] < 70): #Medicamento 1 (Categoria: Hipotension) 
                                    #m[1]=presion sistolica
                                    #m[2]=presion diastolica
        n[m[0]-1]-=15               #la cantidad de elemento que esta en la posicion de la variable sucursal 
                                    #en la lista de n se le resta el valor corespondiente
    elif (90 <= m[1] < 130) and (70 <= m[2] < 90): #Ningun Medicamento (Categoria: Optima)
        continue
    elif (130 <= m[1] < 140) and (90 <= m[2] < 95): #Ningun Medicamento (Categoria: Normal)
        continue
    elif (140 <= m[1] < 150) and (95 <= m[2] < 100): #Medicamento 1 (Categoria: Normal-alta)
        n[m[0]-1]-=10
    elif (150 <= m[1] < 170) and (100 <= m[2] < 110): #Medicamento 1 (Categoria: HTA Grado 1)
        n[m[0]-1]-=10
    elif (170 <= m[1] < 190) and (110 <= m[2] < 120): #Medicamento 1 (Categoria: HTA Grado 2)
        n[m[0]-1]-=20
    elif (m[1] >= 190) and (m[2] >= 120): #Medicamento 1 (Categoria: HTA Grado 3)
        n[m[0]-1]-=50
    elif (m[1] >= 150) and (m[2] < 100): #Medicamento 1 (Categoria: HTA Sitolica Aislada)
        n[m[0]-1]-=20
    else: #Sin categoria
      continue



  
  
"""======================================SALIDAS=================================""" 

menor = sucursal_min(n)
mayor = sucursal_max(n)
print(menor)#numero de la sucursal, con la cantidad minima de medicamentos;respuesta 1
print(mayor)#numero de la sucursal, con la cantidad maxima de medicamentos;respuesta 2

pp = proporcion_porcentual(n_inicial,n)#Calcula una lista de porcentajes de medicamentos segun sucursales

for x in range(len(pp)):#Imprime los porcentajes de cada sucursal demanera acendente;respuesta 3
  pp[x] = "{0:.2f}".format(pp[x])
  print(x+1, pp[x], "%")