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
