# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:04:20 2021

@author: riber
"""
#ej1
total = int(input("¿Cuantas camisas usted va a llevar?: "))
if (total <= 0):
    print("Digite una cantidad valida!")
elif (total <= 2):
    print("Usted tendra un descuento del 10% amigo!")
else:
    print("Usted tendra un descuento del 30% en el total de su compra")
    
#ej2
numP = int(input("Digite un numero al alzar para obtener su promoción!: "))
if (numP <= 0):
    print("Un numero!")x
elif (numP <= 73):
    print("Usted tendra un descuento del 15%!")
else:
    print("Usted tendra un descuento del 20%!")
