# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:59:25 2022

@author: Utilizador
"""
import math
def square_odds(values):
    lista=values.split(",")
    nova_lista=[]
    print(lista)
    for i in lista:
        if int(i)%2!=0:
            nova_lista.append(str(int(i)**2))
    return ",".join(nova_lista)

x=math.sqrt(8759)
print(x)
