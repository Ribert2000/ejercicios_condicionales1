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

#ej5
precio = int(input("Digite el valor del carro que desea comprar: "))
incTerreno = int(input("Digite el incremento anual del terreno en porcentaje: "))
bajonAuto = int(input("Digite la devaluacion del auto anualmente  en porcentaje: "))

inc = (((precio * incTerreno)/100)*3)/2
dec = ((precio * bajonAuto)/100)*3

if inc > dec:
    print("No le solicito comprar el auto")
else:
    print("Si usted quiere podria comprar el auto tranquilamente!")
    
#ej6
pcT=int(input("¿Cuantas computadores desea llevar?: "))
valorPc = 11000

if (pcT >= 1 and pcT <= 4):
    cuenta = (pcT * valorPc)
    descuento = (cuenta * 0.10)
    totalC = (cuenta - descuento)
    print("Su total a pagar es: {}".format(totalC)) 
elif (pcT >= 5 and pcT <= 9):
    cuenta = (pcT * valorPc)
    descuento = (cuenta * 0.20)
    totalC = (cuenta - descuento)
    print("Su total a pagar es: {}".format(totalC)) 
elif (pcT > 10):
    cuenta = (pcT * valorPc)
    descuento = (cuenta * 0.40)
    totalC = (cuenta - descuento)
    print("Su total a pagar es: {}".format(totalC)) 
else:
   print("Digite una cantidad de computadores valida!")
