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
    print("Un numero!")
elif (numP <= 73):
    print("Usted tendra un descuento del 15%!")
else:
    print("Usted tendra un descuento del 20%!")
    
#ej3
montoF = int(input("Digite el monto para la fianza: "))
if (montoF <= 0):
    print("No se puede determinar la cuota que debe pagar!")
elif (montoF <= 49999):
    print("El cliente debera pagar la cuota por un valor de: ",(montoF * 0.03))
else:
    print("El cliente debera pagar la cuota por un valor de: ",(montoF * 0.02))
    
#ej4
puntosF = int(input("Digite cuantos puntos cree que tiene su fabrica: "))
if (puntosF <= 0):
    print("Digite un valor valida!")
elif (puntosF <= 169):
    print("Su fabrica no tendra sancion ni multa.")
else:
    print("Usted sera sancionado con parar su produccion por una semana y una multa del 50% cuando no se detiene la produccion")

